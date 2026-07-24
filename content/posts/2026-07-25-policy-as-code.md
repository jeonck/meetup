---
title: "2026-07-25 Policy as Code로 시작하는 정책 자동화"
date: 2026-07-25T07:58:34.694334+09:00
tags: ["policy-as-code", "kubernetes-security", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

Policy as Code는 인프라와 애플리케이션에 적용할 규칙을 코드로 작성해 버전 관리하고 자동으로 검증하는 접근 방식입니다. Kubernetes 생태계에서는 Open Policy Agent(OPA)와 Kyverno 같은 도구를 통해 리소스가 클러스터에 배포되기 전에 보안·컴플라이언스 규칙을 자동으로 검사하는 형태로 널리 쓰이고 있습니다. 수동 코드 리뷰나 문서화된 가이드라인에 의존하던 방식에서 벗어나, 정책 자체를 테스트 가능하고 재사용 가능한 코드로 관리하는 흐름으로 이동하고 있습니다.

## 🔑 핵심 요점

- Policy as Code는 조직의 규칙(보안, 비용, 네이밍 컨벤션 등)을 코드로 작성해 자동 검증하는 방법론입니다.
- Kubernetes에서는 Admission Controller를 통해 리소스가 클러스터에 생성되기 전에 정책을 적용할 수 있습니다.
- Open Policy Agent(OPA)는 범용 정책 엔진이며, Rego라는 전용 언어로 정책을 작성합니다.
- Kyverno는 YAML 기반으로 정책을 작성할 수 있어 Kubernetes 사용자에게 진입장벽이 낮은 대안입니다.
- 정책을 코드로 관리하면 Git을 통한 버전 관리, 리뷰, CI 테스트가 가능해집니다.
- GitOps 파이프라인과 결합하면 배포 이전 단계에서부터 정책 위반을 걸러낼 수 있습니다.

## 🛠 핵심 기술 쉽게 이해하기

### Policy as Code

조직이 지켜야 할 규칙(예: '모든 컨테이너는 root로 실행 금지', '퍼블릭 S3 버킷 금지')을 코드 형태로 작성하고, 이를 자동화된 도구로 검증하는 접근 방식입니다. 규칙이 문서가 아니라 코드이기 때문에 테스트하고 버전을 관리할 수 있습니다.

**왜 필요한가** — 사람이 수동으로 리뷰하던 보안·컴플라이언스 규칙을 자동화해 실수를 줄이고, 규칙 변경 이력을 명확히 추적하기 위해 사용합니다.

**발표에서는** — 인프라와 애플리케이션 배포 과정에 정책 검증을 자동으로 끼워 넣는 핵심 개념으로 소개되었습니다.

### Open Policy Agent (OPA)

다양한 시스템(Kubernetes, API 게이트웨이, CI/CD 등)에 범용적으로 적용할 수 있는 오픈소스 정책 엔진입니다. Rego라는 자체 쿼리 언어로 정책을 작성합니다.

**왜 필요한가** — 여러 시스템에 흩어져 있던 정책 로직을 하나의 엔진으로 통합해 일관되게 관리하기 위해 사용합니다.

**발표에서는** — Policy as Code를 구현하는 대표적인 엔진으로 언급되었습니다.

### Kyverno

Kubernetes 전용으로 설계된 정책 엔진으로, Rego 대신 익숙한 YAML 문법으로 정책을 작성할 수 있습니다.

**왜 필요한가** — OPA의 Rego 언어는 학습 곡선이 있는데, Kyverno는 Kubernetes 매니페스트와 유사한 방식으로 정책을 작성해 진입 장벽을 낮춥니다.

**발표에서는** — Kubernetes 사용자에게 더 접근하기 쉬운 정책 엔진 대안으로 다뤄졌습니다.

### Gatekeeper (OPA Gatekeeper)

OPA를 Kubernetes Admission Controller로 사용할 수 있게 해주는 프로젝트로, CRD 형태로 정책 템플릿과 제약조건을 정의합니다.

**왜 필요한가** — OPA 엔진을 Kubernetes 네이티브 방식(CRD, Admission Webhook)으로 통합해 클러스터 관리자가 정책을 더 쉽게 배포하고 관리하도록 돕습니다.

**발표에서는** — OPA 기반 정책을 Kubernetes에 실제로 적용하는 구현체로 언급되었습니다.

## 🧭 추구 방향과 흐름

- **Shift-Left 보안** — 정책 검증 시점을 배포 이후가 아니라 CI 파이프라인이나 코드 리뷰 단계로 앞당기는 흐름입니다. Policy as Code를 CI에 통합하면 문제가 있는 리소스가 클러스터에 도달하기 전에 걸러낼 수 있습니다.
- **GitOps와의 결합** — 정책 자체를 Git 저장소에서 코드로 관리하고, GitOps 파이프라인의 일부로 자동 적용·검증하는 방향입니다. 이를 통해 정책 변경도 애플리케이션 배포와 동일한 리뷰·승인 프로세스를 거치게 됩니다.
- **선언적 정책 관리** — Kyverno처럼 YAML 기반의 선언적 문법으로 정책을 작성하는 도구들이 늘어나면서, 전용 언어(Rego) 학습 없이도 정책을 작성할 수 있는 방향으로 생태계가 확장되고 있습니다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(minikube, kind 등)에 Kyverno를 설치하고 기본 제공 정책 샘플을 적용해 보세요.
2. OPA 공식 사이트의 Rego Playground에서 간단한 정책을 직접 작성하며 문법을 익혀보세요.
3. 기존 CI 파이프라인에 정책 검증 단계를 추가해, Pull Request 단계에서 정책 위반을 미리 확인하는 실습을 해보세요.
4. Kyverno와 OPA Gatekeeper 중 하나를 선택하기 전에, 두 도구의 정책 작성 방식(YAML vs Rego)을 비교해 보세요.

## 🔗 참고 자료

- [Open Policy Agent 공식 사이트](https://www.openpolicyagent.org) — OPA와 Rego 언어에 대한 공식 문서와 튜토리얼을 확인할 수 있습니다.
- [Kyverno 공식 사이트](https://kyverno.io) — YAML 기반 Kubernetes 정책 작성법과 설치 가이드를 제공합니다.
- [Kubernetes 공식 문서](https://kubernetes.io) — Admission Controller와 Kubernetes 리소스 모델에 대한 배경 지식을 얻을 수 있습니다.
- [CNCF](https://www.cncf.io) — OPA와 Kyverno 등 Policy as Code 관련 프로젝트들이 속한 클라우드 네이티브 생태계 전반을 살펴볼 수 있습니다.
