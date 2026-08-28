---
title: "2026-08-28 Kubernetes 위의 Apache Flink: Operator 패턴으로 스트리밍 잡을 무중단 운영하기"
date: 2026-08-28T09:59:40.978146+09:00
tags: ["apache-flink", "kubernetes", "stream-processing"]
---
## 왜 스트리밍 플랫폼은 Kubernetes로 향하는가

데이터 플랫폼 팀들은 이제 Flink 잡을 전용 클러스터가 아니라 Kubernetes 위에서 운영하는 방향으로 이동하고 있다. 조직 안에 이미 표준 오케스트레이션 계층이 존재하는데, 팀마다 별도 인프라를 두는 대신 배치·스트리밍 워크로드를 하나의 플랫폼에서 함께 관리하려는 요구가 커졌기 때문이다. Apache Flink 공식 문서는 Flink Kubernetes Operator가 "Kubernetes API를 커스텀 리소스로 확장해 Flink 애플리케이션의 생명주기(배포, 무중단 업그레이드, 오토스케일링)를 관리한다"고 설명한다([Operator Overview](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/concepts/overview/)). CNCF도 오퍼레이터 패턴 자체를 "커스텀 리소스를 도메인 지식을 가진 컨트롤러가 지속적으로 조정(reconcile)하는 확장 모델"로 정의하며, 선언적 상태와 실제 상태를 계속 수렴시키는 피드백 루프가 핵심이라고 설명한다([Kubernetes Operators 101](https://www.cncf.io/blog/2020/10/02/kubernetes-operators-101/)). 스트리밍 잡을 하나의 CR로 선언하고 컨트롤 루프가 알아서 원하는 상태로 맞춰준다는 것이, 이 흐름의 핵심 아이디어다.

## Checkpoint와 Savepoint: 장애를 전제로 설계하기

"재시작해도 데이터가 손실되면 안 된다"는 요구는 Flink의 상태 스냅샷 메커니즘과 직결된다. Flink는 Chandy-Lamport 알고리즘을 변형한 비동기 배리어 스냅샷으로 체크포인트를 자동 생성해 장애 복구에 쓰고, 사용자가 명시적으로 트리거하는 세이브포인트는 버전 업그레이드나 재배포처럼 운영자의 의도적 개입에 쓰인다는 점이 공식 문서와 Ververica의 설명에서 확인된다([Fault Tolerance](https://nightlies.apache.org/flink/flink-docs-master/docs/learn-flink/fault_tolerance/), [Savepoints vs Checkpoints](https://www.ververica.com/blog/differences-between-savepoints-and-checkpoints-in-flink)). JobManager가 죽어도 잡이 마지막 체크포인트에서 이어 재시작하려면 Flink 자체의 HA 서비스(리더 선출, 상태 공유)가 필요하며, 이는 오퍼레이터 자체의 HA(대기 replica로 컨트롤 루프 지속)와는 별개 계층이라는 점을 오퍼레이터 문서가 명확히 구분한다([High Availability](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/deployment/leader-election/)).

## 노드 유지보수와 "떠나야 하는 잡" 문제

유지보수 구간을 나눠 순차적으로 노드를 회수하는 접근은 Kubernetes의 드레인·PodDisruptionBudget(PDB) 패턴 그대로다. 공식 문서는 kubectl drain이 PDB를 인지해 동작하며, 가용성을 지키려면 노드를 비우기 전에 PDB부터 설정하라고 권고한다([Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/), [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)). 문제는 장시간 실행되는 스트리밍 태스크는 즉시 종료할 수 없다는 점인데, 실무에서는 잡이 노드 회수 시그널을 받고 스스로 체크포인트를 남긴 뒤 종료하도록 유예 시간을 주는 방식이 널리 쓰인다. AWS의 EC2 스팟 인스턴스 사례도 인터럽션 시그널 수신 시 체크포인트 후 재배치하는 전략을 소개하며, 비용 절감과 안정성을 동시에 확보하는 패턴으로 언급된다([Optimizing Flink on EKS with Spot Instances](https://aws.amazon.com/blogs/compute/optimizing-apache-flink-on-amazon-eks-using-amazon-ec2-spot-instances/)).

## 오토스케일링까지 포함한 자동화

Flink Kubernetes Operator의 오토스케일러는 백프레셔와 사용률 지표를 수집해 연산자 단위로 병렬도를 자동 조정하며, in-place 리스케일링을 위해서는 Adaptive Scheduler와 Externalized Declarative Resource Management를 활성화해야 한다([Autoscaler 문서](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/custom-resource/autoscaler/), [Elastic Scaling](https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/elastic_scaling/)). 이는 팀이 수동으로 파티션·워커 수를 튜닝하던 방식에서 벗어나, 선언적 CR과 컨트롤 루프만으로 배포·복구·확장을 아우르는 self-service 데이터 플랫폼으로 가는 흐름을 잘 보여준다.

## 도입 시 고려할 점

Flink를 Kubernetes로 옮기려는 팀은 (1) Flink 자체 HA와 오퍼레이터 HA를 분리해서 설정하고, (2) PDB·체크포인트 간격을 노드 회수 정책과 맞춰 조정하며, (3) 오토스케일러 도입 전 Adaptive Scheduler 호환성을 먼저 검증하는 순서를 권한다. 이 세 가지가 갖춰지면 노드가 사라지고 잡이 재시작되더라도 데이터는 유실되지 않는 운영 환경을 만들 수 있다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Apache Flink Kubernetes Operator Overview](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/concepts/overview/) — Flink Kubernetes Operator가 CR 기반으로 잡 생명주기 전체를 관리한다는 정의의 근거
- [Kubernetes Operators 101 (CNCF Blog)](https://www.cncf.io/blog/2020/10/02/kubernetes-operators-101/) — 오퍼레이터 패턴과 reconciliation 루프에 대한 CNCF 공식 설명
- [Apache Flink Fault Tolerance](https://nightlies.apache.org/flink/flink-docs-master/docs/learn-flink/fault_tolerance/) — 체크포인트 기반 장애 복구 메커니즘(비동기 배리어 스냅샷)의 근거
- [3 differences between Savepoints and Checkpoints in Apache Flink (Ververica)](https://www.ververica.com/blog/differences-between-savepoints-and-checkpoints-in-flink) — 체크포인트와 세이브포인트의 용도 차이(자동 복구 vs 수동 트리거) 설명
- [High Availability | Apache Flink Kubernetes Operator](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/deployment/leader-election/) — Flink 자체 HA와 오퍼레이터 HA가 별개 계층임을 뒷받침
- [Safely Drain a Node | Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) — 노드 드레인과 PodDisruptionBudget의 동작 방식 근거
- [Optimizing Apache Flink on Amazon EKS using EC2 Spot Instances (AWS)](https://aws.amazon.com/blogs/compute/optimizing-apache-flink-on-amazon-eks-using-amazon-ec2-spot-instances/) — 인터럽션 시그널 수신 후 체크포인트하고 재배치하는 스팟 인스턴스 운영 패턴의 근거
- [Autoscaler | Apache Flink Kubernetes Operator](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/custom-resource/autoscaler/) — 오토스케일러의 백프레셔 기반 자동 병렬도 조정 및 Adaptive Scheduler 요구사항 근거
