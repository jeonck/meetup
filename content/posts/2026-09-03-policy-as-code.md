---
title: "2026-09-03 Policy as Code로 시작하는 클라우드 거버넌스 자동화"
date: 2026-09-03T08:49:20.749307+09:00
tags: ["policy-as-code", "kyverno", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

이번 브리핑은 Policy as Code라는 주제를 중심으로, 정책을 코드로 정의하고 자동으로 검증·집행하는 접근 방식을 다룬다. Kubernetes 환경에서 보안, 비용, 컴플라이언스 규칙을 수동 검토 대신 선언적 정책으로 관리하는 흐름을 소개한다. Kyverno와 Open Policy Agent(OPA) 같은 도구가 이 흐름의 핵심 축으로 다뤄지며, GitOps와 결합해 배포 파이프라인에 정책 검증을 통합하는 방향을 제시한다.

## 🔑 핵심 요점

- Policy as Code는 보안·컴플라이언스 규칙을 코드로 작성해 버전 관리하고 자동으로 검증하는 방식이다.
- 수동 코드 리뷰나 사후 감사 대신 배포 파이프라인 안에서 정책 위반을 사전에 차단할 수 있다.
- Kubernetes 생태계에서는 Kyverno와 OPA/Gatekeeper가 대표적인 Policy as Code 엔진으로 쓰인다.
- 정책을 코드로 관리하면 Git을 통한 변경 이력 추적과 리뷰 프로세스를 그대로 적용할 수 있다.
- GitOps 파이프라인에 정책 검증 단계를 넣으면 클러스터에 반영되기 전에 규칙 위반을 걸러낼 수 있다.
- Policy as Code는 개별 도구보다 '정책을 코드처럼 다룬다'는 원칙에 가깝다.

## 🛠 핵심 기술 쉽게 이해하기

### Policy as Code

인프라나 애플리케이션이 지켜야 할 규칙(보안, 비용, 네이밍 컨벤션 등)을 사람이 읽는 문서가 아니라 코드로 정의하는 접근 방식이다. 이 코드는 Git에 저장되고 버전 관리되며, 자동화된 도구가 이를 읽어 실제 시스템에 적용한다.

**왜 필요한가** — 수동으로 정책을 검토하면 사람마다 기준이 다르고 누락되기 쉬운데, 코드로 정의하면 일관되고 반복 가능한 검증이 가능해진다.

**발표에서는** — 전체 주제로 다뤄졌으며, 정책을 코드화해 자동으로 집행하는 개념이 핵심으로 소개되었다.

### Kyverno

Kubernetes 전용으로 만들어진 정책 엔진으로, YAML 형식으로 정책을 작성할 수 있어 별도 언어를 배우지 않아도 된다. 리소스 생성·수정 시점에 규칙을 검증하거나 자동으로 값을 채워주는 기능을 제공한다.

**왜 필요한가** — Kubernetes 매니페스트에 익숙한 사람이라면 새로운 문법 없이 바로 정책을 작성할 수 있어 진입장벽이 낮다.

**발표에서는** — Kubernetes 환경의 Policy as Code 대표 도구로 언급되었다.

### Open Policy Agent (OPA)

범용 정책 엔진으로, Rego라는 전용 언어로 정책을 작성해 Kubernetes뿐 아니라 API, CI/CD 등 다양한 시스템에 적용할 수 있다. Kubernetes에서는 Gatekeeper라는 컴포넌트를 통해 admission controller로 동작한다.

**왜 필요한가** — 여러 시스템에 걸쳐 하나의 정책 엔진으로 통일된 규칙을 적용하고 싶을 때 유용하다.

**발표에서는** — Kyverno와 비교되는 범용 정책 엔진으로 함께 다뤄졌다.

### Argo CD

GitOps 방식으로 Kubernetes 리소스를 배포하는 도구로, Git 저장소의 상태를 클러스터와 지속적으로 동기화한다.

**왜 필요한가** — 정책 검증을 배포 파이프라인의 일부로 자동화하려면 GitOps 도구와의 연동이 필요하다.

**발표에서는** — 정책 검증을 배포 흐름에 통합하는 GitOps 파이프라인의 예시로 언급되었다.

## 🧭 추구 방향과 흐름

- **Shift-left 거버넌스** — 정책 위반을 배포 이후가 아니라 코드 리뷰나 CI 단계에서 미리 잡아내려는 흐름이다. Policy as Code를 파이프라인 앞단에 배치해 문제를 조기에 발견하는 방향이 제시되었다.
- **선언적 정책 관리** — 정책 자체를 선언적 코드로 표현해 Git으로 버전 관리하고, Kubernetes 리소스처럼 리뷰·롤백이 가능하게 만드는 방향이다.
- **자동 집행(enforcement)로의 전환** — 사람이 수동으로 검토하고 승인하는 절차 대신 admission controller나 CI 단계에서 자동으로 정책을 강제하는 흐름이 강조되었다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(minikube, kind 등)에 Kyverno를 설치하고 기본 제공되는 policy library의 예제 정책을 적용해본다.
2. OPA Playground에서 간단한 Rego 정책을 작성해보며 Kyverno의 YAML 방식과 비교해본다.
3. 기존 GitOps 파이프라인(Argo CD 등)에 정책 검증 단계를 추가하는 방법을 문서에서 찾아본다.
4. Kyverno 공식 문서의 'Policy Types'를 읽고 validate, mutate, generate 정책의 차이를 이해한다.

## 🔗 참고 자료

- [Kyverno 공식 문서](https://kyverno.io) — Kubernetes 네이티브 Policy as Code 도구의 개념과 설치 방법을 다룬다.
- [Open Policy Agent 공식 사이트](https://www.openpolicyagent.org) — 범용 정책 엔진 OPA와 Rego 언어에 대한 문서를 제공한다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 파이프라인에 정책 검증을 통합하는 배경 지식을 제공한다.
- [Kubernetes 공식 문서](https://kubernetes.io) — Admission controller와 리소스 정책의 기본 개념을 이해하는 데 필요하다.
- [CNCF 공식 사이트](https://www.cncf.io) — Kyverno, OPA 등이 속한 클라우드 네이티브 생태계의 전반적 맥락을 제공한다.
