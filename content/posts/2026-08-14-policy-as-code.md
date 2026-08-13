---
title: "2026-08-14 Policy as Code로 클라우드 네이티브 거버넌스 자동화하기"
date: 2026-08-14T07:37:44.738703+09:00
tags: ["policy-as-code", "opa", "kyverno", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

이번 브리프는 별도의 밋업 발표 없이 Policy as Code라는 주제를 중심으로 관련 생태계를 정리한 것이다. Policy as Code는 인프라와 애플리케이션에 적용할 정책을 코드로 작성하고 버전 관리하여, 사람이 수동으로 검토하던 규칙을 자동화된 파이프라인과 클러스터 안에서 강제하는 접근 방식이다. Open Policy Agent(OPA), Kyverno, OPA Gatekeeper 같은 도구들이 이 흐름을 뒷받침하며, 각각 범용 정책 엔진, Kubernetes 네이티브 정책 관리, Kubernetes admission control 통합이라는 역할을 맡는다. 전체적으로 보안·컴플라이언스 검증을 개발 초기 단계로 앞당기는 shift-left 흐름과 맞닿아 있다.

## 🔑 핵심 요점

- Policy as Code는 보안·규정 준수 정책을 코드로 작성해 Git으로 버전 관리하고 자동으로 검증하는 방식이다.
- 수동 코드 리뷰나 체크리스트에 의존하던 거버넌스를 CI/CD 파이프라인과 Kubernetes admission control 단계로 자동화할 수 있다.
- Open Policy Agent(OPA)는 Kubernetes뿐 아니라 API, 마이크로서비스, 클라우드 인프라 등 다양한 영역에 적용 가능한 범용 정책 엔진이다.
- Kyverno는 YAML 기반 정책 문법을 제공해 Rego 언어를 몰라도 Kubernetes 정책을 작성할 수 있게 해준다.
- OPA Gatekeeper는 OPA를 Kubernetes admission webhook에 통합해 리소스 생성 시점에 정책을 강제한다.
- 정책 위반을 배포 이후가 아니라 CI 단계나 클러스터 진입 시점에서 잡아내는 shift-left 검증이 핵심 방향이다.

## 🛠 핵심 기술 쉽게 이해하기

### Policy as Code

인프라 구성, 보안 규칙, 컴플라이언스 요건 등을 사람이 읽는 문서가 아니라 실행 가능한 코드로 정의하는 방식이다. 이 코드는 Git 저장소에서 버전 관리되고, 자동화 도구가 이를 읽어 실제 시스템에 정책을 적용하거나 위반 여부를 검사한다.

**왜 필요한가** — 수동 검토나 체크리스트 방식은 사람의 실수와 누락에 취약하고 확장이 어렵기 때문에, 정책을 코드화해 일관되고 반복 가능하게 강제하기 위해 사용한다.

**발표에서는** — 이번 브리프의 중심 주제로, 관련 도구들이 이 개념을 어떻게 구현하는지를 중심으로 다뤘다.

### Open Policy Agent (OPA)

CNCF의 오픈소스 범용 정책 엔진으로, Rego라는 전용 언어로 정책을 작성하고 JSON/YAML 형태의 입력 데이터에 대해 허용/거부를 판단한다. Kubernetes뿐 아니라 API 게이트웨이, 마이크로서비스, CI/CD 파이프라인 등 다양한 곳에 임베드해서 쓸 수 있다.

**왜 필요한가** — 여러 시스템에 흩어진 정책 로직을 하나의 엔진과 언어로 통일해 관리하기 위해 사용한다.

**발표에서는** — Policy as Code를 구현하는 대표적인 기반 엔진으로 소개되었다.

### Kyverno

Kubernetes 전용으로 설계된 정책 엔진으로, Rego 대신 익숙한 YAML 문법으로 정책을 작성할 수 있다. 리소스 검증(validate), 변형(mutate), 생성(generate) 같은 기능을 admission controller 형태로 제공한다.

**왜 필요한가** — OPA의 Rego 언어에 대한 학습 장벽 없이, Kubernetes 사용자가 바로 정책을 작성하고 적용할 수 있게 하기 위해 쓴다.

**발표에서는** — OPA보다 진입장벽이 낮은 Kubernetes 네이티브 대안으로 언급되었다.

### OPA Gatekeeper

OPA를 Kubernetes admission webhook과 연동하는 프로젝트로, 리소스가 클러스터에 생성되기 전에 OPA 정책을 실행해 거부하거나 감사(audit) 로그를 남긴다. ConstraintTemplate과 Constraint라는 CRD로 정책을 정의한다.

**왜 필요한가** — OPA의 범용 엔진 기능을 Kubernetes 클러스터의 실제 리소스 생성 흐름에 직접 통합하기 위해 사용한다.

**발표에서는** — OPA와 Kubernetes를 잇는 실질적인 admission control 구현체로 다뤄졌다.

## 🧭 추구 방향과 흐름

- **Shift-Left 보안 검증** — 정책 위반을 프로덕션 배포 이후가 아니라 CI 파이프라인이나 admission control 시점에서 미리 잡아내는 방향으로 나아가고 있다. Kyverno와 Gatekeeper 모두 리소스가 클러스터에 실제로 들어오기 전에 검증하는 구조를 갖는다.
- **GitOps와의 결합** — 정책 자체를 코드로 관리한다는 점에서 Policy as Code는 Git 저장소를 단일 진실 공급원(source of truth)으로 삼는 GitOps 워크플로우와 자연스럽게 맞물린다. 정책 변경도 코드 리뷰와 배포 파이프라인을 거치게 된다.
- **플랫폼 엔지니어링의 가드레일화** — 개발자에게 자유로운 self-service 권한을 주면서도 조직의 규칙을 강제해야 하는 상황에서, 정책 엔진이 사람이 아닌 자동화된 가드레일 역할을 맡는 방향으로 발전하고 있다.

## 🚀 바로 활용하기

1. OPA 공식 사이트의 Rego Playground에서 간단한 정책을 직접 작성하고 실행해본다.
2. 로컬 kind 또는 minikube 클러스터에 Kyverno를 설치하고, 기본 제공되는 정책 샘플(예: 특정 라벨 필수화)을 적용해본다.
3. OPA Gatekeeper 공식 문서를 따라 ConstraintTemplate과 Constraint를 만들어 실제 admission 거부 동작을 확인해본다.
4. 기존 CI 파이프라인에 정책 검사 단계를 추가해 배포 전 정책 위반 여부를 자동으로 확인하도록 구성해본다.

## 🔗 참고 자료

- [Open Policy Agent 공식 사이트](https://www.openpolicyagent.org) — OPA의 개념, Rego 언어, Playground 등을 확인할 수 있는 공식 문서 루트
- [Kyverno 공식 사이트](https://kyverno.io) — Kyverno 설치 방법과 YAML 기반 정책 예제를 제공하는 공식 문서
- [OPA Gatekeeper 공식 사이트](https://open-policy-agent.github.io/gatekeeper/website/) — Kubernetes admission control과 OPA를 연동하는 방법을 설명하는 공식 문서
- [CNCF](https://www.cncf.io) — OPA를 비롯한 Policy as Code 관련 프로젝트들이 속한 클라우드 네이티브 재단
