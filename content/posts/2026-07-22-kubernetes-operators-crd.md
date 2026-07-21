---
title: "2026-07-22 Kubernetes Operators와 CRD로 보는 선언적 자동화"
date: 2026-07-22T07:53:29.812325+09:00
tags: ["kubernetes-operator", "crd", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

Kubernetes Operators와 Custom Resource Definition(CRD)은 쿠버네티스 API를 확장해 애플리케이션 운영 지식을 코드로 자동화하는 핵심 패턴입니다. 반복적인 운영 작업(배포, 백업, 스케일링, 장애 복구)을 사람이 아닌 컨트롤러가 선언적 목표 상태에 맞춰 수행하도록 만드는 것이 핵심 아이디어입니다. 이 패턴은 Crossplane 같은 인프라 프로비저닝 도구, Kyverno 같은 정책 엔진 등 클라우드 네이티브 생태계 전반의 기반이 되고 있습니다. 초심자 입장에서는 CRD가 쿠버네티스 API에 새로운 리소스 타입을 추가하는 방법이고, Operator는 그 리소스를 감시하며 실제 상태를 원하는 상태로 맞추는 컨트롤러라는 것부터 이해하면 됩니다.

## 🔑 핵심 요점

- CRD는 쿠버네티스 API 서버에 새로운 리소스 타입(kind)을 등록하는 방법이다.
- Operator는 CRD로 정의된 커스텀 리소스를 지속적으로 감시하며 원하는 상태(desired state)와 실제 상태(actual state)를 일치시키는 컨트롤러다.
- 이 패턴을 쓰면 데이터베이스 백업, 인증서 갱신, 인프라 프로비저닝 같은 운영자의 도메인 지식을 코드로 캡슐화할 수 있다.
- Operator SDK나 Kubebuilder 같은 프레임워크를 쓰면 처음부터 컨트롤러 로직을 직접 짜지 않고 표준 구조 위에서 Operator를 만들 수 있다.
- Crossplane은 이 패턴을 클라우드 인프라(예: AWS RDS, GCP GKE) 프로비저닝까지 확장해 쿠버네티스 API 하나로 인프라와 애플리케이션을 함께 관리하게 해준다.
- 정책 엔진인 Kyverno도 CRD 기반으로 동작하며, 별도의 정책 언어 없이 쿠버네티스 매니페스트 형태로 정책을 정의한다.
- OperatorHub 같은 커뮤니티 카탈로그를 통해 이미 만들어진 Operator를 재사용하는 것도 처음 접근하기 좋은 방법이다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes Operators & CRDs

CRD(Custom Resource Definition)는 쿠버네티스 API에 새로운 리소스 타입을 추가하는 스키마 정의이고, Operator는 그 커스텀 리소스를 감시하면서 실제 상태를 선언된 목표 상태로 맞춰주는 컨트롤러 프로그램입니다.

**왜 필요한가** — 복잡한 애플리케이션 운영 작업(장애 복구, 스케일링, 백업 등)을 사람이 수동으로 하지 않고 쿠버네티스 API를 통해 선언적으로 자동화하기 위해 사용합니다.

**발표에서는** — 생태계 전반의 확장 패턴으로 다루며, CRD와 Operator가 쿠버네티스 위에서 동작하는 다른 도구들의 공통 기반이 된다는 점을 짚었습니다.

### Operator SDK / Kubebuilder

Go 언어 기반으로 Operator를 쉽게 만들 수 있게 해주는 프레임워크로, CRD 스캐폴딩, 컨트롤러 boilerplate, 테스트 환경 구성을 자동으로 제공합니다.

**왜 필요한가** — Operator를 밑바닥부터 구현하려면 client-go, informer, reconcile loop 등 알아야 할 것이 많은데, 이 프레임워크가 표준화된 뼈대를 제공해 진입 장벽을 낮춰줍니다.

**발표에서는** — 직접 Operator를 개발하고 싶은 사람을 위한 실전 진입점으로 언급되었습니다.

### Crossplane

쿠버네티스 CRD와 Operator 패턴을 인프라 프로비저닝으로 확장한 오픈소스 프로젝트로, AWS/GCP/Azure 같은 클라우드 리소스를 쿠버네티스 매니페스트로 선언해 생성·관리할 수 있게 해줍니다.

**왜 필요한가** — 인프라를 위한 별도의 IaC 도구(Terraform 등) 없이도 쿠버네티스 API 하나로 애플리케이션과 인프라를 통합 관리하고 싶을 때 사용합니다.

**발표에서는** — Operator 패턴이 애플리케이션 운영을 넘어 인프라 영역까지 확장된 대표 사례로 소개되었습니다.

### Kyverno

쿠버네티스 네이티브 정책 엔진으로, 별도의 정책 언어 없이 YAML 매니페스트 형태로 클러스터 리소스에 대한 검증/변경/생성 정책을 정의할 수 있습니다.

**왜 필요한가** — 보안 규칙이나 조직의 운영 가이드라인(예: 이미지 태그 고정, 리소스 제한 강제)을 클러스터 차원에서 자동으로 강제하기 위해 사용합니다.

**발표에서는** — CRD 기반 확장 패턴이 정책 관리 영역까지 적용된 사례로 함께 언급되었습니다.

## 🧭 추구 방향과 흐름

- **쿠버네티스 API를 만능 제어 평면으로** — CRD와 Operator 패턴이 확산되면서 쿠버네티스 API가 컨테이너 오케스트레이션을 넘어 인프라, 정책, 보안까지 아우르는 공통 제어 평면(control plane)으로 자리잡는 흐름이 뚜렷합니다. Crossplane과 Kyverno 모두 이 흐름의 구체적 사례입니다.
- **운영 지식의 코드화(Operational Knowledge as Code)** — 사람이 반복적으로 수행하던 운영 노하우를 Operator 컨트롤러 로직으로 캡슐화해, 장애 대응이나 백업 같은 작업을 자동화하려는 방향이 강조됩니다.
- **플랫폼 엔지니어링과 self-service 인프라** — Crossplane 같은 도구로 인프라 프로비저닝까지 쿠버네티스 API 안으로 끌어들이면, 개발자가 별도의 클라우드 콘솔 없이도 쿠버네티스 매니페스트만으로 필요한 리소스를 셀프서비스로 요청할 수 있는 플랫폼을 지향하게 됩니다.

## 🚀 바로 활용하기

1. kubectl로 kind나 minikube 등 로컬 클러스터를 띄운 뒤, 간단한 CRD를 직접 정의하고 kubectl apply로 커스텀 리소스를 생성해본다.
2. Kubebuilder 공식 튜토리얼을 따라 간단한 Operator(예: 리소스 개수를 관리하는 컨트롤러)를 처음부터 만들어본다.
3. OperatorHub.io에서 관심 있는 카테고리(DB, 모니터링 등)의 기존 Operator를 찾아 설치해보고 CRD 스펙을 살펴본다.
4. Crossplane 공식 문서의 Getting Started를 따라 클라우드 프로바이더 하나를 연결해 간단한 리소스(예: S3 버킷)를 쿠버네티스 매니페스트로 생성해본다.

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 Operator 패턴의 기반이 되는 쿠버네티스 API 개념 전반을 확인할 수 있습니다.
- [Kubebuilder](https://book.kubebuilder.io) — Operator 개발을 위한 표준 프레임워크와 튜토리얼을 제공합니다.
- [OperatorHub.io](https://operatorhub.io) — 커뮤니티가 공개한 Operator들을 검색하고 바로 설치해볼 수 있는 카탈로그입니다.
- [Crossplane](https://www.crossplane.io) — CRD/Operator 패턴을 클라우드 인프라 프로비저닝으로 확장한 프로젝트의 공식 홈페이지입니다.
- [Kyverno](https://kyverno.io) — 쿠버네티스 네이티브 정책 엔진의 공식 문서로, CRD 기반 정책 관리 방식을 설명합니다.
- [CNCF](https://www.cncf.io) — Operator, Crossplane, Kyverno 등 관련 프로젝트들이 속한 클라우드 네이티브 생태계 전반을 다룹니다.
