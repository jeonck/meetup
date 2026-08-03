---
title: "2026-08-04 Policy as Code로 보는 클라우드 거버넌스 자동화"
date: 2026-08-04T07:57:15.049192+09:00
tags: ["policy-as-code", "kubernetes", "kyverno", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

Policy as Code는 조직의 보안, 컴플라이언스, 운영 규칙을 코드로 작성해 시스템에 자동으로 강제하는 접근 방식이다. Kubernetes 생태계에서는 Kyverno와 Open Policy Agent(OPA)/Gatekeeper가 대표적인 구현체로 자리잡았으며, admission controller를 통해 리소스가 클러스터에 배포되기 전에 정책 위반 여부를 검사한다. CI/CD 파이프라인에 정책 검사를 포함시키는 shift-left 흐름과 맞물려, 배포 이후가 아니라 배포 이전 단계에서 문제를 걸러내는 방향으로 발전하고 있다. GitOps 도구인 Argo CD, 인프라 프로비저닝 도구인 Crossplane과 결합해 선언적 인프라 전체에 정책을 일관되게 적용하려는 시도도 늘고 있다.

## 🔑 핵심 요점

- Policy as Code는 보안/컴플라이언스 규칙을 코드로 정의해 자동으로 강제하는 방식이다.
- Kubernetes에서는 admission controller를 통해 리소스가 클러스터에 반영되기 전에 정책을 검사한다.
- Kyverno는 YAML 기반으로 정책을 작성해 별도 언어 학습 부담이 적은 것이 특징이다.
- OPA/Gatekeeper는 Rego라는 전용 언어로 더 복잡하고 범용적인 정책 표현이 가능하다.
- 정책 검사를 CI 파이프라인 초기 단계로 옮기는 shift-left 흐름이 확산되고 있다.
- GitOps, IaC 도구와 결합해 인프라 전체에 일관된 정책을 적용하려는 시도가 늘고 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Policy as Code

조직의 보안, 규정 준수, 운영 규칙을 프로그램 코드나 선언적 설정 파일로 표현하고, 이를 시스템에 자동으로 적용하는 접근 방식이다. 사람이 수동으로 리뷰하고 승인하던 규칙을 자동화된 검사 로직으로 대체한다.

**왜 필요한가** — 수동 검토는 느리고 실수가 발생하기 쉬우며 조직 규모가 커질수록 일관성을 유지하기 어렵기 때문에, 규칙을 코드화해 반복 가능하고 검증 가능한 형태로 관리하기 위해 사용한다.

**발표에서는** — 전반적인 주제로서, 정책을 코드로 관리하면 배포 전 자동 검사와 버전 관리, 리뷰가 가능해진다는 개념적 배경으로 다뤄졌다.

### Kyverno

Kubernetes 네이티브 정책 엔진으로, YAML 형식으로 정책을 작성할 수 있어 별도의 정책 언어를 배우지 않아도 된다. Kubernetes 리소스 생성, 수정, 검증, 자동 변형(mutation)까지 지원한다.

**왜 필요한가** — 쿠버네티스 사용자가 익숙한 YAML만으로 정책을 작성할 수 있게 해 진입 장벽을 낮추고, 클러스터 내 리소스 규칙 준수를 자동화하기 위해 쓰인다.

**발표에서는** — Kubernetes 환경에서 Policy as Code를 구현하는 대표적인 도구로 언급되었다.

### Open Policy Agent (OPA) / Gatekeeper

OPA는 범용 정책 엔진이며, Rego라는 전용 질의 언어로 정책을 작성한다. Gatekeeper는 OPA를 Kubernetes admission controller 형태로 통합한 프로젝트다.

**왜 필요한가** — Kubernetes뿐 아니라 API, 마이크로서비스, CI/CD 등 다양한 시스템에 동일한 정책 엔진을 적용하고 싶을 때 사용한다.

**발표에서는** — Kyverno와 대비되는 선택지로, 더 복잡한 정책 로직이 필요한 경우의 대안으로 소개되었다.

### Admission Controller

Kubernetes API 서버에 리소스 요청이 도달했을 때, 실제로 저장되기 전에 요청을 가로채 검증하거나 수정하는 확장 지점이다.

**왜 필요한가** — 정책 위반 리소스가 클러스터에 반영되는 것을 사전에 차단하기 위한 핵심 메커니즘이다.

**발표에서는** — Kyverno와 OPA/Gatekeeper가 정책을 강제하는 기반 기술로 함께 설명되었다.

### Argo CD

Git 저장소에 선언된 상태를 기준으로 Kubernetes 클러스터를 자동 동기화하는 GitOps 도구다.

**왜 필요한가** — 배포 파이프라인 전체를 Git 기반으로 관리해 변경 이력을 추적하고, 정책 검사를 배포 프로세스에 자연스럽게 통합하기 위해 함께 언급된다.

**발표에서는** — 정책 검사를 CI/CD 및 GitOps 흐름에 통합하는 맥락에서 관련 도구로 다뤄졌다.

## 🧭 추구 방향과 흐름

- **Shift-left 정책 검사** — 정책 위반을 배포 이후 런타임에서 발견하는 대신, 코드 리뷰나 CI 파이프라인 단계에서 미리 걸러내려는 흐름이다. 이렇게 하면 문제를 더 이른 시점에, 더 적은 비용으로 해결할 수 있다.
- **선언적 인프라 전반으로의 정책 확장** — Kubernetes 리소스뿐 아니라 Crossplane 같은 IaC 도구가 관리하는 클라우드 인프라 전체에도 동일한 정책 프레임워크를 적용하려는 시도가 늘고 있다. 이는 플랫폼 엔지니어링에서 일관된 거버넌스를 제공하려는 목표와 맞닿아 있다.
- **개발자 친화적인 정책 도구 선택** — Rego 같은 전용 언어 대신 YAML 기반의 Kyverno처럼 학습 곡선이 낮은 도구를 선택하는 경향이 늘고 있다. 이는 정책 관리 권한을 보안팀뿐 아니라 개발팀에도 넓히려는 self-service 지향과 연결된다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(kind, minikube 등)에 Kyverno를 설치하고 기본 제공 정책 예제를 적용해본다.
2. Kyverno 공식 문서의 policy library를 참고해 이미지 태그 검증이나 리소스 라벨 강제 같은 간단한 정책을 직접 작성해본다.
3. OPA Rego 언어 튜토리얼(Rego Playground)로 간단한 규칙을 작성해보고 Kyverno의 YAML 방식과 비교해본다.
4. CI 파이프라인에 conftest 같은 도구를 추가해 배포 전 정책 검사를 시험해본다.

## 🔗 참고 자료

- [Kyverno 공식 문서](https://kyverno.io) — YAML 기반 Kubernetes 정책 엔진의 설치 방법과 정책 작성 가이드를 제공한다.
- [Open Policy Agent 공식 사이트](https://www.openpolicyagent.org) — Rego 언어와 범용 정책 엔진 OPA의 개념 및 사용법을 설명한다.
- [Kubernetes 공식 문서](https://kubernetes.io) — admission controller와 리소스 생명주기 전반에 대한 배경 지식을 제공한다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 흐름 속에서 정책 검사를 통합하는 배포 파이프라인 구조를 이해하는 데 참고할 수 있다.
- [Crossplane 공식 사이트](https://www.crossplane.io) — Kubernetes 리소스를 넘어 클라우드 인프라 전반에 정책을 확장하는 맥락을 뒷받침한다.
- [CNCF 공식 사이트](https://www.cncf.io) — Policy as Code 관련 프로젝트들이 속한 클라우드 네이티브 생태계 전반을 조망할 수 있다.
