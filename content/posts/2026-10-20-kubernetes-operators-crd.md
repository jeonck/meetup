---
title: "2026-10-20 Kubernetes Operators와 CRD로 보는 선언적 운영 자동화"
date: 2026-10-20T09:54:07.395054+09:00
tags: ["kubernetes-operator", "crd", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이 브리프는 Kubernetes Operators와 Custom Resource Definitions(CRD)를 중심으로, 애플리케이션과 인프라 운영을 코드가 아닌 선언적 API로 다루는 흐름을 정리한다. CRD로 새로운 리소스 타입을 정의하고 Operator가 이를 감시하며 원하는 상태를 지속적으로 맞춰주는 패턴이 핵심이다. Operator SDK, Crossplane, OLM 등 관련 생태계 도구들이 이 패턴을 실제 운영 환경에 적용하기 쉽게 만들어주는 역할을 한다. 전체적으로 클러스터 운영 지식을 API 뒤로 숨기고 셀프서비스화하는 플랫폼 엔지니어링 방향으로 이어진다.

## 🔑 핵심 요점

- CRD는 Kubernetes API를 확장해 애플리케이션이나 인프라 고유의 리소스 타입을 정의할 수 있게 해준다.
- Operator는 CRD로 정의된 리소스를 지속적으로 감시(reconcile loop)하며 원하는 상태(desired state)를 유지하는 컨트롤러다.
- Operator 패턴은 수동 운영 지식(예: DB 백업, 업그레이드 절차)을 코드로 캡슐화해 자동화한다.
- Operator SDK나 Kubebuilder 같은 프레임워크를 쓰면 처음부터 직접 컨트롤러를 짜지 않고도 Operator를 빠르게 만들 수 있다.
- Crossplane은 Operator 패턴을 클라우드 인프라 프로비저닝까지 확장해 클러스터 API로 외부 리소스를 관리하게 해준다.
- OperatorHub나 OLM 같은 생태계는 Operator의 배포와 생명주기 관리를 표준화하려는 시도다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes CRD & Operator 패턴

CRD(Custom Resource Definition)는 Kubernetes API에 사용자 정의 리소스 타입을 추가하는 기능이고, Operator는 그 리소스를 감시하며 실제 상태를 원하는 상태로 맞춰주는 컨트롤러다. 쉽게 말해 CRD는 '새로운 명사(리소스)'를 만들고, Operator는 그 명사에 대한 '운영 로직'을 담당한다.

**왜 필요한가** — 복잡한 애플리케이션 운영 작업(설치, 업그레이드, 백업, 장애 복구 등)을 사람이 매뉴얼대로 하는 대신 Kubernetes가 자동으로 수행하게 하기 위함이다.

**발표에서는** — 전체 논의의 중심 개념으로, CRD로 리소스를 정의하고 Operator가 reconcile loop를 통해 상태를 관리하는 기본 패턴이 다뤄졌다.

### Operator SDK / Kubebuilder

Go 기반으로 Kubernetes Operator를 빠르게 만들 수 있도록 도와주는 프레임워크다. CRD 스캐폴딩, 컨트롤러 보일러플레이트, 테스트 도구 등을 자동으로 생성해준다.

**왜 필요한가** — 처음부터 client-go와 reconcile loop를 직접 구현하는 번거로움을 줄이고 표준화된 방식으로 Operator를 개발하기 위해 사용한다.

**발표에서는** — CRD와 Operator를 실제로 구현할 때 가장 널리 쓰이는 진입점 도구로 언급되었다.

### Crossplane

Kubernetes API 위에서 클라우드 인프라(DB, 네트워크, VM 등)를 CRD 형태의 리소스로 선언하고 관리할 수 있게 해주는 프로젝트다. Operator 패턴을 클러스터 외부 리소스까지 확장한 형태다.

**왜 필요한가** — 애플리케이션뿐 아니라 인프라까지 하나의 선언적 API와 GitOps 워크플로우로 통합 관리하기 위해 사용한다.

**발표에서는** — Operator 패턴이 인프라 프로비저닝 영역으로 확장되는 대표 사례로 소개되었다.

### OLM (Operator Lifecycle Manager)

클러스터에 설치된 Operator들의 설치, 업그레이드, 권한 관리, 의존성 등 생명주기를 관리해주는 도구다. OperatorHub와 함께 Operator를 패키징하고 배포하는 표준을 제공한다.

**왜 필요한가** — 여러 Operator를 운영할 때 버전 관리와 업그레이드를 안전하고 일관되게 처리하기 위함이다.

**발표에서는** — Operator를 실제 운영 환경에 배포하고 관리하는 생태계 도구로 함께 언급되었다.

## 🧭 추구 방향과 흐름

- **운영 지식의 코드화와 자동화** — 사람이 수행하던 운영 절차를 Operator라는 소프트웨어로 캡슐화해 Kubernetes가 스스로 상태를 복구하고 유지하게 만드는 방향이다. 이는 반복 작업을 줄이고 운영 실수를 줄이는 것을 목표로 한다.
- **선언적 API로의 인프라 확장** — Crossplane처럼 CRD와 Operator 패턴을 클라우드 인프라 영역까지 확장해, 애플리케이션과 인프라를 동일한 선언적 API와 GitOps 워크플로우로 관리하려는 흐름이다.
- **플랫폼 엔지니어링과 셀프서비스화** — CRD로 정의된 커스텀 API를 통해 개발자가 복잡한 내부 구현을 몰라도 리소스를 선언만 하면 플랫폼이 알아서 처리해주는 셀프서비스 플랫폼을 구축하려는 방향으로 이어진다.

## 🚀 바로 활용하기

1. Kubebuilder 공식 문서를 따라 간단한 CRD와 컨트롤러를 만들고 로컬 클러스터(kind, minikube)에 배포해본다.
2. OperatorHub.io에서 널리 쓰이는 Operator(예: Prometheus Operator)를 설치해 CRD와 reconcile 동작을 관찰한다.
3. Crossplane을 클러스터에 설치하고 간단한 클라우드 리소스(예: 스토리지 버킷)를 CRD로 선언해 프로비저닝해본다.
4. kubectl get crd와 kubectl describe로 기존 클러스터에 설치된 CRD들을 살펴보며 실제 스키마 구조를 익힌다.

## 🔗 참고 자료

- [Kubernetes 공식 문서 - Custom Resources](https://kubernetes.io) — CRD와 Operator 패턴의 공식 개념 설명을 확인할 수 있다.
- [Kubebuilder](https://book.kubebuilder.io) — CRD와 Operator를 직접 만들어보는 실습 가이드를 제공한다.
- [Operator Framework / OperatorHub](https://operatorhub.io) — 다양한 공개 Operator를 탐색하고 설치해볼 수 있다.
- [Crossplane](https://www.crossplane.io) — Operator 패턴을 인프라 프로비저닝으로 확장한 프로젝트의 공식 문서다.
- [CNCF](https://www.cncf.io) — Operator 패턴과 관련 생태계 프로젝트들의 상위 거버넌스 기관이다.
