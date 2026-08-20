---
title: "2026-08-21 Kubernetes Operator와 CRD로 시작하는 플랫폼 자동화"
date: 2026-08-21T07:22:52.859526+09:00
tags: ["kubernetes-operator", "crd", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이번 자료는 별도의 밋업 발표 없이 Kubernetes Operator와 Custom Resource Definition(CRD)을 주제로 정리한 기술 브리프입니다. Kubernetes 위에서 애플리케이션과 인프라 운영을 코드로 자동화하는 Operator 패턴의 기본 개념과, 이를 확장해 클라우드 리소스까지 선언적으로 관리하는 생태계 흐름을 다룹니다. Crossplane, Kyverno, Argo CD 같은 관련 도구들이 어떻게 CRD 기반 확장성을 공유하는지도 함께 소개합니다. 실제 청중 질의응답은 없었으며, 입문자가 바로 실습해볼 수 있는 학습 경로 위주로 구성했습니다.

## 🔑 핵심 요점

- CRD는 Kubernetes API를 사용자 정의 리소스 타입으로 확장하는 표준 방법이다.
- Operator는 CRD와 컨트롤러 로직을 결합해 사람이 하던 운영 작업을 자동화하는 패턴이다.
- Crossplane은 Operator 패턴을 클라우드 인프라 프로비저닝까지 확장한 도구다.
- Kyverno는 CRD 기반으로 정책을 선언적으로 정의하고 클러스터에 강제하는 정책 엔진이다.
- Argo CD는 Git에 정의된 상태를 클러스터에 지속적으로 동기화하는 GitOps 도구로, CRD로 애플리케이션 배포 상태를 관리한다.
- 생태계 전반이 '선언적 상태 + 자동 조정(reconciliation)' 모델로 수렴하고 있다.
- 입문자는 kubebuilder나 operator-sdk 같은 프레임워크로 간단한 Operator를 직접 만들어보는 것이 이해에 가장 효과적이다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes Operator

Operator는 Kubernetes의 컨트롤러 개념을 확장해, 특정 애플리케이션이나 서비스의 운영 지식(설치, 백업, 장애 복구 등)을 코드로 구현한 소프트웨어입니다. 사람이 수동으로 하던 반복 작업을 자동화된 컨트롤러가 대신 수행합니다.

**왜 필요한가** — 복잡한 상태 기반 애플리케이션(데이터베이스, 메시지 큐 등)을 Kubernetes 네이티브 방식으로 자동 운영하기 위해 사용합니다.

**발표에서는** — CRD와 함께 Kubernetes 확장성의 핵심 축으로 소개되며, 이후 소개되는 도구들의 기반 개념으로 다뤄집니다.

### Custom Resource Definition (CRD)

CRD는 Kubernetes API에 새로운 종류의 리소스 타입을 등록할 수 있게 해주는 기능입니다. 이를 통해 Pod나 Deployment처럼 사용자 정의 객체를 kubectl로 다룰 수 있습니다.

**왜 필요한가** — Kubernetes 코어를 수정하지 않고도 도메인 특화 리소스를 선언적으로 관리할 수 있게 해줍니다.

**발표에서는** — Operator 패턴을 구현하는 데 필요한 필수 구성 요소로 제목에서부터 강조됩니다.

### Crossplane

Crossplane은 Kubernetes CRD와 Operator 패턴을 이용해 클라우드 프로바이더(AWS, GCP, Azure 등)의 리소스를 Kubernetes 매니페스트처럼 선언적으로 프로비저닝하는 오픈소스 프로젝트입니다.

**왜 필요한가** — 인프라 프로비저닝과 애플리케이션 배포를 동일한 Kubernetes API와 GitOps 워크플로우로 통합 관리하기 위해 사용합니다.

**발표에서는** — Operator/CRD 패턴이 애플리케이션 운영을 넘어 인프라 관리로 확장된 대표 사례로 언급됩니다.

### Kyverno

Kyverno는 Kubernetes 리소스에 대한 정책을 YAML로 선언해 검증, 변경, 생성을 자동화하는 정책 엔진입니다. CRD로 정책 자체를 정의합니다.

**왜 필요한가** — 보안 및 거버넌스 규칙을 코드로 관리하고 클러스터 전체에 일관되게 적용하기 위해 사용합니다.

**발표에서는** — CRD 기반 확장의 또 다른 활용 사례로, 정책 관리 영역에서의 응용으로 소개됩니다.

### Argo CD

Argo CD는 Git 저장소에 정의된 애플리케이션 상태를 Kubernetes 클러스터에 지속적으로 동기화하는 GitOps 컨티뉴어스 딜리버리 도구입니다.

**왜 필요한가** — 배포 상태를 코드로 관리하고 클러스터 상태와 Git의 선언적 정의가 항상 일치하도록 자동 조정하기 위해 사용합니다.

**발표에서는** — Operator의 reconciliation 개념이 배포 자동화에 적용된 예시로 함께 다뤄집니다.

## 🧭 추구 방향과 흐름

- **선언적 상태와 자동 조정(reconciliation) 모델로의 수렴** — Operator, Crossplane, Kyverno, Argo CD 모두 '원하는 상태를 선언하면 컨트롤러가 실제 상태를 지속적으로 맞춰간다'는 동일한 reconciliation 루프 패턴을 공유합니다. Kubernetes API 확장성을 기반으로 애플리케이션 운영, 인프라 프로비저닝, 정책 관리, 배포까지 하나의 모델로 통합되는 흐름이 나타납니다.
- **인프라까지 아우르는 Kubernetes 중심 플랫폼화** — Crossplane 사례처럼 클라우드 인프라 관리마저 Kubernetes CRD로 흡수되면서, Kubernetes가 애플리케이션 오케스트레이션을 넘어 조직 전체의 플랫폼 컨트롤 플레인 역할로 확장되고 있습니다.
- **정책과 거버넌스의 코드화(Policy as Code)** — Kyverno와 같은 도구들은 보안·컴플라이언스 규칙을 CRD로 선언해 자동 강제함으로써, 수동 검토 대신 코드 기반의 지속적인 거버넌스를 지향하는 방향을 보여줍니다.

## 🚀 바로 활용하기

1. kubectl로 간단한 CRD를 직접 정의하고 등록해 커스텀 리소스를 만들어본다.
2. operator-sdk 또는 kubebuilder 튜토리얼을 따라 최소 기능의 Operator를 직접 작성해본다.
3. 로컬 클러스터(minikube, kind 등)에 Crossplane을 설치해 클라우드 리소스 하나를 선언적으로 프로비저닝해본다.
4. Argo CD 공식 문서의 Getting Started를 따라 Git 저장소 기반 배포 동기화를 실습해본다.

## 🔗 참고 자료

- [Kubernetes 공식 문서 - Custom Resources](https://kubernetes.io) — CRD와 Operator 패턴의 공식 개념 설명을 제공하는 루트 문서
- [Crossplane 공식 사이트](https://www.crossplane.io) — CRD 기반 클라우드 인프라 프로비저닝 도구의 공식 정보
- [Kyverno 공식 사이트](https://kyverno.io) — CRD 기반 정책 엔진의 공식 문서 루트
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 reconciliation 모델을 설명하는 공식 문서
- [CNCF 공식 사이트](https://www.cncf.io) — Operator 및 관련 프로젝트들이 속한 클라우드 네이티브 생태계 소개
