---
title: "2026-09-30 Kubernetes Operators와 CRD로 이해하는 확장형 클러스터 운영"
date: 2026-09-30T10:01:05.142414+09:00
tags: ["kubernetes-operator", "crd", "cloud-native", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이번 브리핑은 실제 밋업 발표가 아니라 Kubernetes Operator와 Custom Resource Definition(CRD)을 중심으로 정리한 기술 브리프이다. Operator 패턴이 왜 등장했는지, CRD가 어떻게 Kubernetes API를 확장하는지, 그리고 이를 기반으로 하는 Crossplane, Kyverno, cert-manager 같은 주변 생태계가 어떤 방향으로 발전하고 있는지를 다룬다. 결론적으로 Kubernetes는 단순 컨테이너 오케스트레이터를 넘어 선언적 API 기반의 범용 제어 평면으로 자리잡고 있다.

## 🔑 핵심 요점

- Operator는 사람이 수동으로 하던 운영 작업(백업, 장애 복구, 업그레이드 등)을 코드로 자동화하는 Kubernetes 확장 패턴이다.
- CRD(Custom Resource Definition)는 Kubernetes API 서버에 새로운 사용자 정의 리소스 타입을 등록하는 메커니즘이다.
- Operator는 내부적으로 컨트롤러 패턴을 사용하며, 원하는 상태(desired state)와 실제 상태(actual state)를 지속적으로 비교해 조정(reconcile)한다.
- CRD와 Controller를 함께 사용하면 Kubernetes 위에 도메인 특화 API를 자유롭게 만들 수 있다.
- Crossplane, Kyverno, cert-manager 등 최근 클라우드 네이티브 도구 대부분이 이 Operator 패턴 위에서 동작한다.
- Kubernetes는 이제 컨테이너 오케스트레이션 도구가 아니라 다양한 인프라 자원을 선언적으로 관리하는 범용 제어 평면(control plane)으로 확장되고 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes Operators

Operator는 특정 애플리케이션이나 인프라 자원을 운영하는 사람의 지식을 코드로 옮겨놓은 Kubernetes 컨트롤러이다. 클러스터 상태를 지속적으로 감시하면서 사용자가 선언한 원하는 상태에 맞게 자동으로 리소스를 생성, 수정, 삭제한다.

**왜 필요한가** — 데이터베이스 백업, 장애 복구, 버전 업그레이드처럼 반복적이고 실수하기 쉬운 운영 작업을 자동화해 사람의 개입을 줄이기 위해 사용한다.

**발표에서는** — 브리핑에서는 Operator가 CRD로 정의된 커스텀 리소스를 감시하고 실제 상태를 원하는 상태로 맞추는 조정 루프(reconciliation loop)로 소개되었다.

### CRD (Custom Resource Definition)

CRD는 Kubernetes API 서버에 새로운 종류의 리소스(예: Database, Certificate 등)를 등록할 수 있게 해주는 확장 기능이다. 등록된 CRD는 kubectl이나 API로 기본 리소스처럼 다룰 수 있다.

**왜 필요한가** — Kubernetes가 기본으로 제공하지 않는 개념(애플리케이션별 설정, 클라우드 리소스 등)을 선언적 API로 표현하기 위해 필요하다.

**발표에서는** — 브리핑에서는 CRD가 Operator와 짝을 이루는 핵심 구성요소로, CRD 없이는 Operator가 관리할 대상 리소스 자체가 존재하지 않는다는 점이 강조되었다.

### Crossplane

Crossplane은 CRD와 Operator 패턴을 활용해 클라우드 인프라(예: AWS RDS, S3 버킷 등)를 Kubernetes 리소스처럼 선언적으로 관리할 수 있게 해주는 오픈소스 프로젝트이다.

**왜 필요한가** — Terraform 같은 별도 도구 없이 Kubernetes API 하나로 애플리케이션과 인프라를 동시에 관리하기 위해 사용한다.

**발표에서는** — Operator/CRD 패턴을 실제 인프라 프로비저닝에 적용한 대표 사례로 언급되었다.

### cert-manager

cert-manager는 CRD로 정의한 Certificate 리소스를 통해 TLS 인증서 발급과 갱신을 자동화하는 Kubernetes Operator이다.

**왜 필요한가** — 인증서 만료로 인한 서비스 장애를 막고, 수동 갱신 작업을 없애기 위해 사용한다.

**발표에서는** — Operator 패턴이 실제 프로덕션 환경에서 널리 쓰이는 예시로 소개되었다.

### Kyverno

Kyverno는 Kubernetes 리소스에 대한 정책을 CRD 형태로 정의하고 자동으로 검증·수정·생성하는 정책 엔진이다.

**왜 필요한가** — 클러스터 전반에 보안 규칙이나 운영 규칙을 코드로 강제해 사람의 실수를 줄이기 위해 사용한다.

**발표에서는** — Operator/CRD 패턴이 정책 관리 영역까지 확장된 사례로 간단히 다뤄졌다.

## 🧭 추구 방향과 흐름

- **API 확장을 통한 범용 제어 평면화** — Kubernetes는 컨테이너 오케스트레이션을 넘어 CRD를 통해 클라우드 인프라, 인증서, 정책 등 다양한 도메인을 선언적으로 표현하는 플랫폼으로 확장되고 있다. 이는 Crossplane, cert-manager 같은 도구들이 모두 CRD/Operator 패턴을 공유한다는 점에서 근거를 찾을 수 있다.
- **운영 자동화(Operations as Code)** — Operator 패턴의 핵심은 사람의 운영 지식을 코드로 옮겨 자동화하는 것이다. 이는 수동 운영에서 선언적·자동화된 운영으로 전환하려는 클라우드 네이티브 생태계 전반의 흐름과 맞닿아 있다.
- **정책 및 거버넌스의 선언적 관리** — Kyverno 사례처럼 보안과 운영 정책마저 CRD로 선언하고 자동 검증하는 방향으로 발전하고 있어, 거버넌스도 코드로 관리하는 흐름이 강화되고 있다.

## 🚀 바로 활용하기

1. 로컬에서 kind나 minikube로 클러스터를 띄우고 kubectl get crd로 기본 제공 CRD 목록을 확인해본다.
2. Kubernetes 공식 문서의 Operator pattern과 CRD 문서를 읽고 client-go의 컨트롤러 예제를 살펴본다.
3. cert-manager를 클러스터에 설치해 Certificate CRD를 생성하고 인증서가 자동 발급되는 과정을 직접 관찰한다.
4. Crossplane 공식 문서의 Get Started 가이드를 따라 간단한 클라우드 리소스를 Kubernetes 매니페스트로 선언해본다.

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — Operator 패턴과 CRD 개념의 1차 출처
- [Crossplane 공식 홈페이지](https://www.crossplane.io) — CRD 기반 인프라 관리 도구의 공식 문서
- [Kyverno 공식 홈페이지](https://kyverno.io) — CRD 기반 정책 엔진의 공식 문서
- [CNCF 공식 홈페이지](https://www.cncf.io) — Operator/CRD 생태계 프로젝트들이 속한 클라우드 네이티브 재단 정보
