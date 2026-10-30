---
title: "2026-10-30 Kubernetes Operators와 CRD로 보는 플랫폼 자동화"
date: 2026-10-30T10:31:47.055028+09:00
tags: ["kubernetes-operator", "crd", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이번 글은 Kubernetes Operators와 CRD(Custom Resource Definition)를 중심으로 쿠버네티스 확장 패턴을 정리한다. CRD로 새로운 리소스 타입을 정의하고 Operator가 이를 지속적으로 관찰해 원하는 상태를 유지하는 원리를 다룬다. 이어서 Operator 생태계에서 자주 함께 쓰이는 Crossplane, Kubebuilder, Operator Framework 같은 도구들도 함께 소개한다. 전체적으로 '플랫폼을 코드로 다루는' 흐름 속에서 Operator 패턴이 왜 중요한지에 초점을 맞춘다.

## 🔑 핵심 요점

- CRD는 쿠버네티스 API를 확장해 사용자 정의 리소스 타입을 선언할 수 있게 해준다.
- Operator는 CRD로 정의된 커스텀 리소스를 감시하며 실제 상태를 원하는 상태로 맞추는 컨트롤러다.
- Operator 패턴은 반복적인 운영 작업(백업, 스케일링, 업그레이드 등)을 코드로 자동화하는 데 쓰인다.
- Kubebuilder와 Operator SDK 같은 프레임워크를 쓰면 Operator를 처음부터 직접 구현하지 않고 빠르게 만들 수 있다.
- Crossplane은 Operator 패턴을 클라우드 인프라 프로비저닝까지 확장한 대표적인 사례다.
- Operator/CRD 생태계는 '플랫폼을 API로 제공한다'는 Platform Engineering 흐름과 맞물려 성장하고 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes CRD (Custom Resource Definition)

CRD는 쿠버네티스 API에 새로운 리소스 종류를 추가할 수 있게 해주는 기능이다. 예를 들어 Deployment나 Service처럼 kubectl로 다룰 수 있는 나만의 리소스 타입(예: Database, Backup)을 만들 수 있다.

**왜 필요한가** — 쿠버네티스가 기본으로 제공하지 않는 도메인 특화 개념(예: 데이터베이스 인스턴스, 인증서)을 쿠버네티스 방식으로 선언적으로 관리하기 위해 사용한다.

**발표에서는** — Operator 패턴의 기반 기술로 소개되며, 커스텀 리소스를 정의하는 역할로 다뤄졌다.

### Kubernetes Operator

Operator는 CRD로 정의된 커스텀 리소스의 상태를 지속적으로 감시하고, 실제 상태가 원하는 상태(desired state)와 다르면 자동으로 조정하는 컨트롤러 프로그램이다.

**왜 필요한가** — 사람이 수동으로 하던 운영 작업(설치, 백업, 장애 복구, 업그레이드)을 자동화해 운영 부담을 줄이기 위해 쓴다.

**발표에서는** — CRD와 짝을 이루는 핵심 개념으로, 컨트롤 루프(control loop) 방식으로 상태를 맞추는 동작 원리가 설명됐다.

### Operator SDK / Kubebuilder

Operator를 밑바닥부터 구현하지 않고도 보일러플레이트 코드를 생성해주는 프레임워크다. Go 언어 기반으로 CRD 스키마와 컨트롤러 로직을 쉽게 작성할 수 있게 돕는다.

**왜 필요한가** — Operator 개발의 반복적인 설정 작업을 줄이고 표준화된 구조로 빠르게 시작할 수 있게 하기 위해 사용한다.

**발표에서는** — Operator를 직접 만들어보려는 개발자를 위한 실용적인 출발점으로 언급됐다.

### Crossplane

Crossplane은 Operator 패턴을 확장해 쿠버네티스 리소스뿐 아니라 AWS, GCP 같은 클라우드 인프라 자원까지 쿠버네티스 API로 선언적으로 관리할 수 있게 해주는 도구다.

**왜 필요한가** — 클라우드 인프라 프로비저닝을 쿠버네티스 매니페스트 방식으로 통합해, Infrastructure as Code를 플랫폼 레벨에서 다루기 위해 사용한다.

**발표에서는** — Operator/CRD 패턴의 대표적인 실전 활용 사례로 소개됐다.

## 🧭 추구 방향과 흐름

- **Platform as Code / Platform Engineering** — CRD와 Operator를 통해 플랫폼의 기능을 API 리소스로 노출하는 방식이 확산되고 있다. 이는 운영팀이 반복 작업을 코드화하고, 개발자는 쿠버네티스 API만으로 필요한 리소스를 요청할 수 있게 하는 Platform Engineering 흐름과 맞닿아 있다.
- **선언적 자동화의 확장** — Operator 패턴이 애플리케이션 운영을 넘어 Crossplane처럼 클라우드 인프라 영역까지 확장되면서, '쿠버네티스를 범용 컨트롤 플레인으로 쓰는' 방향이 강화되고 있다.
- **Operator 생태계의 표준화** — Operator SDK, Kubebuilder 같은 프레임워크가 자리잡으면서 Operator 개발의 진입장벽이 낮아지고, CNCF 생태계 안에서 유사한 패턴을 따르는 프로젝트들이 늘어나는 방향으로 가고 있다.

## 🚀 바로 활용하기

1. 로컬에서 minikube나 kind로 클러스터를 띄우고 kubectl get crd로 기존 CRD 목록을 확인해본다.
2. Kubebuilder 공식 튜토리얼을 따라 간단한 CRD와 Operator를 직접 만들어본다.
3. Crossplane을 설치해 간단한 클라우드 리소스(예: S3 버킷)를 쿠버네티스 매니페스트로 선언해 프로비저닝해본다.
4. Kubernetes 공식 문서의 Custom Resources 섹션을 읽고 CRD와 컨트롤러의 관계를 정리해본다.

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 컨트롤러 개념의 기본 개념을 다루는 공식 레퍼런스
- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Operator 패턴을 클라우드 인프라로 확장한 대표 프로젝트
- [Operator Framework](https://operatorframework.io) — Operator SDK를 포함한 Operator 개발 생태계 공식 사이트
- [CNCF](https://www.cncf.io) — CRD/Operator 패턴을 따르는 다양한 클라우드 네이티브 프로젝트의 모체 재단
