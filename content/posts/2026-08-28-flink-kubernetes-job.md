---
title: "2026-08-28 Flink 데이터 플랫폼과 Kubernetes 유지보수 시대응 Job 스케줄러"
date: 2026-08-28T09:57:48.057133+09:00
tags: ["kubernetes", "apache-flink", "job-scheduling"]
---
## 📋 밋업 한눈에 보기

인도에서 온 발표자가 자신의 팀이 스트리밍 데이터 처리에 Apache Flink를 어떻게 활용하는지 소개하며 발표를 시작했다. 이어서 Kubernetes 클러스터를 여러 zone으로 나누어 한 번에 일부씩 순차적으로 점검하는 rolling 유지보수 방식과, 그 과정에서 몇 시간에서 며칠씩 실행되는 외부(external) job이 갑자기 끊기지 않도록 보호하는 자체 스케줄러/컨트롤러 설계를 설명했다. Kubernetes custom resource와 leader election, checkpoint를 활용해 job 상태를 추적하고 중단 시 재개할 수 있도록 만든 구조가 핵심 내용이었다. Apache Airflow와 유사한 스케줄링 개념도 함께 언급되었다.

## 🔑 핵심 요점

- Apache Flink는 스트리밍 처리와 머신러닝 워크로드에 강점이 있어 데이터 처리 job에 널리 쓰인다.
- Kubernetes 클러스터는 유지보수를 위해 여러 zone으로 나누고 한 번에 일부(예: 5%)씩만 순차적으로 점검한다.
- 유지보수 중 노드가 내려가면 몇 시간~며칠씩 걸리는 장기 실행 external job이 예기치 않게 중단될 위험이 있다.
- 발표팀은 Kubernetes custom resource와 controller 패턴으로 job의 실행 ID와 상태를 추적하는 자체 플랫폼을 구축했다.
- leader election 구조를 통해 컨트롤러가 job 상태를 지속적으로 확인하고 업데이트한다.
- checkpoint 개념을 활용해 job이 중단되어도 처음부터 다시 시작하지 않고 이어서 재개할 수 있도록 설계했다.
- 스케줄링 방식은 Apache Airflow와 유사하게 우선순위/의존성에 따라 job을 생성하고 처리한다.

## 🛠 핵심 기술 쉽게 이해하기

### Apache Flink

대량의 데이터를 실시간(스트리밍) 또는 배치로 처리할 수 있는 오픈소스 분산 데이터 처리 프레임워크다.

**왜 필요한가** — 배치 처리보다 스트리밍 처리 능력이 뛰어나고 머신러닝 워크로드와의 궁합도 좋아 채택되었다.

**발표에서는** — 발표자는 팀에서 데이터 처리 job에 주로 Flink를 사용하며 업계 전반에서 널리 쓰인다고 소개했다.

### Kubernetes Operator (Custom Resource / Controller)

Kubernetes API를 확장해 custom resource(CR)를 정의하고, controller가 이를 계속 관찰(reconcile)하며 원하는 상태를 유지하도록 만드는 패턴이다.

**왜 필요한가** — 외부에서 실행되는 job의 실행 ID와 상태를 Kubernetes 네이티브 방식으로 추적·관리하기 위해 사용한다.

**발표에서는** — 발표에서 스케줄러가 job마다 custom resource를 생성하고, leader가 그 상태를 체크·업데이트하는 구조가 설명되었다.

### Apache Airflow

정해진 스케줄이나 의존관계에 따라 여러 작업을 자동으로 실행해주는 워크플로우 오케스트레이션 도구다.

**왜 필요한가** — job을 스케줄에 맞춰 생성하고 우선순위·의존성에 따라 순서대로 처리하기 위해 쓰인다.

**발표에서는** — 발표자는 스케줄러의 job 생성 및 실행 방식을 Airflow에 빗대어 설명했다.

### Kubernetes Rolling Node Maintenance

클러스터 노드를 여러 zone으로 나눈 뒤 한 번에 일부(예: 5%)씩만 순차적으로 점검·재부팅하는 유지보수 방식이다.

**왜 필요한가** — 전체 서비스를 중단하지 않고 안전하게 클러스터를 점검하기 위함이다.

**발표에서는** — 발표자는 이 방식으로 인해 장시간 실행되는 외부 job이 예기치 않게 끊길 수 있는 문제와 그 대응 로직을 다뤘다.

### Checkpoint 기반 상태 보존

실행 중인 작업의 중간 상태를 저장해두어, 중단되더라도 처음부터 다시 시작하지 않고 이어서 재개할 수 있게 하는 기법이다.

**왜 필요한가** — 유지보수나 장애로 job이 강제 종료되어도 데이터 손실이나 재작업을 최소화하기 위해 사용한다.

**발표에서는** — 발표 중 checkpoint를 활용해 job을 재개하는 흐름이 설명되었고, 청중이 checkpoint가 실제 저장소인지 파일인지 질문했다.

## 🧭 추구 방향과 흐름

- **플랫폼으로서의 안정적인 job 실행 보장** — 발표자는 팀이 사용자를 대신해 데이터 처리 job의 스케줄링과 유지보수 대응을 책임지는 내부 플랫폼을 만들고 있다고 설명했다. 사용자가 인프라 세부사항을 몰라도 job을 안정적으로 돌릴 수 있게 하는 self-service platform 방향과 맞닿아 있다.
- **무중단(Zero-downtime) 유지보수** — 클러스터를 zone 단위로 나눠 rolling 방식으로 유지보수하면서도, 장시간 실행되는 job이 끊기지 않도록 상태를 보존하고 재개시키는 것이 발표의 핵심 목표로 제시되었다.

## 🚀 바로 활용하기

1. Apache Flink 공식 문서의 튜토리얼을 따라 간단한 스트리밍 job을 직접 실행해본다.
2. kubebuilder 등으로 간단한 Custom Resource Definition(CRD)과 controller를 만들어 Kubernetes Operator 패턴을 익혀본다.
3. Apache Airflow를 로컬에 설치해 DAG 기반 스케줄링을 실습해본다.
4. Kubernetes의 cordon/drain 명령을 사용해 노드 rolling maintenance 과정을 직접 실습해본다.

## 🔗 참고 자료

- [Apache Flink](https://flink.apache.org) — 발표에서 언급된 스트리밍 데이터 처리 프레임워크의 공식 문서
- [Kubernetes](https://kubernetes.io) — custom resource, controller, 노드 유지보수 등 발표 전반의 기반이 되는 오케스트레이션 플랫폼
- [Apache Airflow](https://airflow.apache.org) — 발표에서 스케줄링 방식 비교 대상으로 언급된 워크플로우 오케스트레이션 도구
