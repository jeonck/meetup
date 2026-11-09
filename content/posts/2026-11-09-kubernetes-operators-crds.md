---
title: "2026-11-09 Kubernetes Operators & CRDs로 쿠버네티스 확장하기"
date: 2026-11-09T10:24:19.355446+09:00
tags: ["kubernetes-operator", "crd", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이번 글은 실제 밋업 발표가 아니라 Kubernetes Operators와 CRD(Custom Resource Definition)를 중심으로 정리한 기술 브리핑이다. CRD로 쿠버네티스 API를 확장하고 Operator 패턴으로 운영 지식을 코드화하는 방식을 다룬다. 함께 Crossplane, Kubebuilder, Helm 같은 관련 생태계 도구도 소개한다. 쿠버네티스를 플랫폼화하려는 흐름 속에서 이 기술들이 어떤 역할을 하는지 살펴본다.

## 🔑 핵심 요점

- CRD는 쿠버네티스 API 서버에 새로운 리소스 타입을 등록하는 메커니즘이다.
- Operator는 CRD로 정의된 커스텀 리소스를 감시하고 원하는 상태(desired state)로 맞춰주는 컨트롤러다.
- Operator 패턴을 쓰면 복잡한 운영 작업(백업, 업그레이드, 장애 복구 등)을 사람 대신 코드가 자동으로 수행할 수 있다.
- Kubebuilder나 Operator SDK 같은 프레임워크를 쓰면 처음부터 컨트롤러를 직접 구현하지 않아도 된다.
- Crossplane은 Operator 패턴을 클라우드 인프라 프로비저닝까지 확장한 사례다.
- CRD와 Operator는 쿠버네티스를 범용 애플리케이션 플랫폼에서 도메인 특화 플랫폼으로 확장하는 핵심 도구다.

## 🛠 핵심 기술 쉽게 이해하기

### Custom Resource Definition (CRD)

CRD는 쿠버네티스 API에 사용자가 정의한 새로운 리소스 타입을 추가하는 기능이다. 예를 들어 Pod나 Deployment처럼 kubectl로 조회하고 관리할 수 있는 나만의 리소스(예: Database, Backup)를 만들 수 있다.

**왜 필요한가** — 기본 제공 리소스만으로는 표현할 수 없는 도메인 고유의 개념이나 운영 로직을 쿠버네티스 네이티브 방식으로 다루기 위해 사용한다.

**발표에서는** — 주제의 핵심 개념으로, Operator가 동작하기 위한 전제 조건으로 다뤄졌다.

### Kubernetes Operator

Operator는 CRD로 정의된 커스텀 리소스의 상태를 지속적으로 관찰하고, 실제 상태를 원하는 상태로 맞춰주는 컨트롤러(소프트웨어)다. 사람이 하던 운영 작업을 자동화된 소프트웨어 로직으로 대체한다.

**왜 필요한가** — 데이터베이스 클러스터링, 백업, 롤링 업그레이드처럼 사람의 운영 지식이 필요한 반복 작업을 자동화하기 위해 사용한다.

**발표에서는** — CRD와 짝을 이루는 핵심 패턴으로 소개되었으며, 쿠버네티스 확장의 중심 개념으로 다뤄졌다.

### Kubebuilder / Operator SDK

Kubebuilder와 Operator SDK는 Go 언어로 CRD와 Operator를 빠르게 만들 수 있도록 도와주는 프레임워크다. 보일러플레이트 코드를 자동 생성해준다.

**왜 필요한가** — Operator를 밑바닥부터 구현하는 복잡함을 줄이고 표준화된 구조로 커스텀 컨트롤러를 개발하기 위해 사용한다.

**발표에서는** — Operator를 실제로 구현할 때 사용하는 대표적인 도구로 함께 언급되었다.

### Crossplane

Crossplane은 Operator 패턴을 클라우드 인프라 프로비저닝 영역까지 확장한 오픈소스 프로젝트다. AWS, GCP 같은 클라우드 리소스를 쿠버네티스 커스텀 리소스처럼 선언적으로 관리할 수 있게 해준다.

**왜 필요한가** — 애플리케이션뿐 아니라 인프라까지 쿠버네티스 API와 GitOps 방식으로 통합 관리하기 위해 사용한다.

**발표에서는** — Operator 패턴의 응용 사례로 소개되었다.

## 🧭 추구 방향과 흐름

- **쿠버네티스의 플랫폼화** — CRD와 Operator는 쿠버네티스를 단순한 컨테이너 오케스트레이터에서 범용 플랫폼으로 확장하는 역할을 한다. 조직마다 필요한 도메인 개념을 API로 표현하고, 운영 지식을 코드로 캡슐화하는 방향으로 생태계가 발전하고 있다.
- **운영 자동화(Day-2 Operations)** — Operator는 설치 이후의 백업, 복구, 업그레이드 같은 Day-2 운영 작업을 자동화하는 데 초점을 맞춘다. 사람이 수행하던 운영 플레이북을 소프트웨어로 코드화하려는 흐름이 핵심이다.
- **인프라까지 포괄하는 선언적 관리** — Crossplane 같은 사례는 Operator 패턴이 애플리케이션 레벨을 넘어 클라우드 인프라 프로비저닝까지 확장되고 있음을 보여준다. 쿠버네티스 API를 단일 제어 평면(control plane)으로 삼으려는 방향성이 뚜렷하다.

## 🚀 바로 활용하기

1. minikube나 kind로 로컬 클러스터를 띄우고 kubectl get crd로 기존 CRD 목록을 확인해본다.
2. Kubebuilder 공식 튜토리얼을 따라 간단한 CRD와 Operator를 직접 만들어본다.
3. Helm으로 배포된 오픈소스 Operator(예: Prometheus Operator)를 설치해보고 커스텀 리소스가 어떻게 동작하는지 관찰한다.
4. Crossplane 공식 문서의 Getting Started를 따라 쿠버네티스 리소스로 클라우드 인프라를 프로비저닝해본다.

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 Operator 개념의 1차 출처
- [Kubebuilder](https://kubebuilder.io) — Operator/CRD 개발 프레임워크 공식 사이트
- [Crossplane](https://www.crossplane.io) — Operator 패턴을 인프라 프로비저닝으로 확장한 프로젝트
- [CNCF](https://www.cncf.io) — Operator 생태계 프로젝트들이 속한 상위 재단
