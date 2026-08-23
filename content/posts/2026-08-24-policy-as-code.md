---
title: "2026-08-24 Policy as Code로 시작하는 클라우드 네이티브 거버넌스"
date: 2026-08-24T07:17:45.329694+09:00
tags: ["policy-as-code", "kyverno", "opa", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

이번 브리핑은 실제 밋업 발표가 아니라 Policy as Code라는 주제를 중심으로 정리한 기술 브리프다. 쿠버네티스 환경에서 정책을 코드로 관리하는 접근 방식과 이를 뒷받침하는 대표 도구들을 함께 살펴본다. Kyverno, OPA/Gatekeeper, Conftest 같은 도구들이 어떻게 정책 검증을 자동화하는지, 그리고 이러한 흐름이 플랫폼 엔지니어링과 어떻게 맞닿아 있는지 정리했다. 초심자도 어떤 도구부터 시작하면 좋을지 감을 잡을 수 있도록 구성했다.

## 🔑 핵심 요점

- Policy as Code는 조직의 규칙과 보안 요구사항을 사람이 수동으로 검토하는 대신 코드로 작성해 자동 검증하는 방식이다.
- 쿠버네티스 클러스터에서는 Admission Controller를 통해 리소스가 생성되기 전에 정책을 강제할 수 있다.
- Kyverno는 YAML만으로 정책을 작성할 수 있어 쿠버네티스 사용자에게 진입장벽이 낮은 편이다.
- OPA(Open Policy Agent)와 Rego 언어는 쿠버네티스뿐 아니라 다양한 시스템에 범용적으로 적용 가능한 정책 엔진이다.
- CI/CD 파이프라인 단계에서 정책을 미리 검증하는 shift-left 접근이 점점 중요해지고 있다.
- Policy as Code는 GitOps 워크플로우와 결합될 때 정책 변경 이력 추적과 감사가 쉬워진다는 장점이 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Kyverno

쿠버네티스 전용으로 설계된 정책 엔진으로, 별도의 새로운 언어를 배우지 않고 익숙한 YAML 형식으로 정책을 작성할 수 있다. 리소스 검증, 변형(mutation), 생성(generation) 등 다양한 기능을 지원한다.

**왜 필요한가** — 쿠버네티스 리소스가 조직의 보안 및 운영 규칙을 따르는지 자동으로 검사하고, 규칙 위반 시 배포를 차단하기 위해 사용한다.

**발표에서는** — Policy as Code를 실무에 적용할 때 가장 접근성이 좋은 도구로 다뤄졌다.

### OPA (Open Policy Agent)

쿠버네티스뿐 아니라 API 게이트웨이, 마이크로서비스 등 다양한 환경에서 사용할 수 있는 범용 정책 엔진이다. Rego라는 전용 언어로 정책을 표현한다.

**왜 필요한가** — 여러 시스템에 걸쳐 일관된 정책 관리 체계를 구축하고 싶을 때 사용한다.

**발표에서는** — Kyverno와 비교되는 범용 정책 엔진으로 언급되었다.

### Gatekeeper

OPA를 쿠버네티스 Admission Controller로 통합해 사용할 수 있게 해주는 프로젝트로, CRD 형태로 정책 템플릿을 관리한다.

**왜 필요한가** — OPA의 유연함을 쿠버네티스 네이티브 방식(CRD, kubectl)으로 다루고 싶을 때 사용한다.

**발표에서는** — OPA 기반 쿠버네티스 정책 적용 사례로 함께 다뤄졌다.

### Conftest

YAML, JSON, Terraform 설정 파일 등을 OPA/Rego 정책으로 검증할 수 있는 CLI 도구다. CI 파이프라인에 쉽게 통합할 수 있다.

**왜 필요한가** — 배포 전 단계, 즉 CI 파이프라인에서 미리 정책 위반을 잡아내는 shift-left 검증을 위해 사용한다.

**발표에서는** — CI 단계에서의 정책 검증 도구로 언급되었다.

## 🧭 추구 방향과 흐름

- **Shift-Left 거버넌스** — 정책 검증 시점을 배포 이후가 아니라 CI 파이프라인이나 코드 리뷰 단계로 앞당기는 흐름이다. 문제를 더 빨리, 더 저렴하게 발견할 수 있어 Conftest 같은 CI 통합 도구의 중요성이 커지고 있다.
- **GitOps와의 결합** — 정책 자체를 Git 저장소에서 코드로 관리하면서 변경 이력을 추적하고 승인 프로세스를 거치게 하는 방향이다. 정책 변경도 일반 코드 변경과 동일한 리뷰·감사 절차를 따르게 된다.
- **플랫폼 엔지니어링과의 통합** — 개발자가 직접 정책 세부사항을 몰라도 플랫폼 팀이 정한 가드레일 안에서 자율적으로 배포할 수 있도록 하는 셀프서비스 플랫폼의 한 축으로 Policy as Code가 자리잡는 추세다.

## 🚀 바로 활용하기

1. 로컬 쿠버네티스 클러스터(kind, minikube 등)에 Kyverno를 설치하고 기본 제공되는 정책 샘플을 적용해본다.
2. Kyverno 공식 문서의 'Getting Started' 가이드를 따라 간단한 validate 정책 하나를 직접 작성해본다.
3. OPA Playground에서 Rego 문법을 간단히 실습해보고 Kyverno의 YAML 방식과 차이를 비교해본다.
4. Conftest를 사용해 기존 프로젝트의 Kubernetes manifest나 Terraform 파일에 간단한 정책 테스트를 추가해본다.

## 🔗 참고 자료

- [Kyverno 공식 사이트](https://kyverno.io) — Kyverno의 정책 작성 방식과 시작 가이드를 확인할 수 있다.
- [Open Policy Agent 공식 사이트](https://www.openpolicyagent.org) — OPA와 Rego 언어에 대한 공식 문서 루트다.
- [Kubernetes 공식 사이트](https://kubernetes.io) — Admission Controller 등 쿠버네티스 정책 강제 메커니즘의 배경 지식을 제공한다.
- [CNCF 공식 사이트](https://www.cncf.io) — Kyverno, OPA 등 Policy as Code 관련 프로젝트들의 생태계 위치를 파악할 수 있다.
