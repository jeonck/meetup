---
title: "2026-11-19 Kubernetes Operator와 CRD로 보는 선언적 운영"
date: 2026-11-19T11:55:51.403864+09:00
tags: ["kubernetes-operator", "crd", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이번 브리프는 Kubernetes Operator와 Custom Resource Definition(CRD)을 중심으로, 애플리케이션과 인프라 운영을 자동화하는 패턴을 다룬다. CRD로 도메인 특화 리소스를 Kubernetes API에 추가하고, Operator가 이를 지속적으로 감시하며 원하는 상태로 맞추는 구조를 설명한다. 이어서 Operator를 직접 만들 때 쓰는 Kubebuilder, 그리고 이 패턴을 클라우드 인프라 관리까지 확장한 Crossplane을 함께 살펴본다. 전체적으로 수동 운영에서 선언적·자동화된 운영으로 옮겨가는 Kubernetes 생태계의 흐름을 정리한다.

## 🔑 핵심 요점

- Operator는 사람이 수행하던 운영 작업(설치, 업그레이드, 백업 등)을 컨트롤러 코드로 자동화한 것이다.
- CRD는 Kubernetes API에 조직만의 커스텀 리소스 타입을 추가하는 수단이다.
- Operator는 CRD로 정의된 리소스를 지속적으로 감시(reconcile)하며 실제 상태를 원하는 상태로 맞춘다.
- Kubebuilder, Operator SDK 같은 프레임워크가 Operator 개발의 진입장벽을 낮춰준다.
- Crossplane은 Operator 패턴을 애플리케이션 운영 너머 클라우드 인프라 프로비저닝까지 확장한 사례다.
- 이 흐름은 Platform Engineering에서 셀프서비스 API를 제공하는 방향과 맞닿아 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes Operator

Kubernetes 위에서 특정 애플리케이션이나 서비스의 운영 지식을 코드로 옮긴 소프트웨어다. 사람이 수동으로 하던 설치, 업그레이드, 백업, 장애 복구 같은 작업을 컨트롤러가 대신 자동으로 수행한다.

**왜 필요한가** — 복잡한 상태를 가진 애플리케이션(데이터베이스, 메시지 큐 등)을 매뉴얼 운영 대신 자동화하여 사람의 실수를 줄이고 운영 비용을 낮추기 위해 쓴다.

**발표에서는** — CRD와 컨트롤러가 결합되어 하나의 운영 패턴을 이루는 기본 구조로 소개된다.

### Custom Resource Definition (CRD)

Kubernetes API에 사용자가 정의한 새로운 리소스 타입을 추가하는 기능이다. 기본 제공되는 Pod, Deployment 외에 Database, Certificate 같은 도메인 특화 리소스를 kubectl로 다룰 수 있게 해준다.

**왜 필요한가** — 조직이나 플랫폼마다 다른 운영 요구사항을 Kubernetes API와 동일한 방식으로 표현하고 관리하기 위해 필요하다.

**발표에서는** — Operator가 감시하고 관리하는 대상 리소스를 정의하는 역할로 다뤄진다.

### Kubebuilder / Operator SDK

Go 언어로 Operator를 쉽게 만들 수 있도록 돕는 프레임워크다. CRD 스캐폴딩, 컨트롤러 로직 템플릿, 테스트 환경 구성을 자동으로 생성해준다.

**왜 필요한가** — Operator를 처음부터 직접 만들려면 Kubernetes API와 컨트롤러 패턴에 대한 깊은 이해가 필요한데, 이 도구들이 그 진입장벽을 낮춰준다.

**발표에서는** — 직접 Operator를 만들어보려는 개발자에게 추천되는 다음 학습 단계로 언급된다.

### Crossplane

CRD와 Operator 패턴을 확장해 클라우드 인프라(AWS RDS, GCP Storage 등) 자체를 Kubernetes 리소스로 선언하고 관리할 수 있게 해주는 오픈소스 프로젝트다.

**왜 필요한가** — 애플리케이션뿐 아니라 인프라까지 하나의 선언적 API로 통합 관리하려는 Platform Engineering 흐름에서 활용된다.

**발표에서는** — Operator 패턴이 애플리케이션 운영을 넘어 인프라 프로비저닝까지 확장된 대표 사례로 다뤄진다.

## 🧭 추구 방향과 흐름

- **선언적 운영(Declarative Operations)으로의 전환** — Operator와 CRD는 운영 작업을 YAML로 선언하고 컨트롤러가 지속적으로 실제 상태를 원하는 상태로 맞추는 방식을 가능하게 한다. 수동 스크립트 기반 운영 대신 Kubernetes API를 통한 자동화가 점점 표준으로 자리잡고 있다.
- **Platform Engineering과 셀프서비스 확장** — CRD를 통해 플랫폼 팀이 사내 개발자에게 커스텀 API를 제공하면, 개발자는 복잡한 인프라 지식 없이 필요한 리소스를 선언만으로 요청할 수 있다. Crossplane은 이 방향을 인프라 영역까지 밀어붙인 대표적 사례다.
- **애플리케이션 운영에서 인프라 전체로 확장** — 초기 Operator들은 데이터베이스나 메시지 큐 같은 애플리케이션 운영에 집중했지만, 최근에는 클라우드 리소스 프로비저닝까지 Operator 패턴이 확장되는 추세다.

## 🚀 바로 활용하기

1. minikube나 kind로 로컬 클러스터를 띄우고 간단한 CRD를 직접 정의해 kubectl apply로 만들어보기
2. Kubebuilder 공식 튜토리얼을 따라 최소 기능의 Operator를 처음부터 구현해보기
3. Prometheus Operator 같은 잘 알려진 Operator의 소스코드를 읽으며 reconcile 로직 구조 파악하기
4. Crossplane 공식 문서의 Getting Started를 따라 클라우드 리소스를 CRD로 관리하는 흐름을 경험해보기

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 컨트롤러 개념에 대한 공식 설명을 확인할 수 있다.
- [Kubebuilder](https://kubebuilder.io) — Go로 Operator를 만드는 공식 프레임워크 문서다.
- [Operator Framework](https://operatorframework.io) — Operator SDK를 포함한 Operator 개발 생태계의 공식 프로젝트 홈페이지다.
- [Crossplane](https://www.crossplane.io) — Operator 패턴을 클라우드 인프라 관리로 확장한 프로젝트의 공식 홈페이지다.
- [CNCF](https://www.cncf.io) — Kubernetes, Crossplane 등 관련 프로젝트들이 속한 클라우드 네이티브 재단이다.
