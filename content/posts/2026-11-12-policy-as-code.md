---
title: "2026-11-12 Policy as Code로 배우는 선언형 정책 관리"
date: 2026-11-12T11:40:58.900370+09:00
tags: ["policy-as-code", "kubernetes-security", "kyverno", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

Policy as Code는 보안, 컴플라이언스, 운영 규칙을 코드로 정의하고 자동으로 검증·강제하는 접근 방식이다. 기존에는 사람이 수동으로 리뷰하던 보안 정책이나 리소스 제약을 코드화해 CI/CD와 Kubernetes 어드미션 컨트롤 단계에서 자동 검사할 수 있게 한다. Kubernetes 생태계에서는 OPA(Open Policy Agent)와 Kyverno가 대표적인 정책 엔진으로 자리잡았으며, GitOps 워크플로우와 결합되어 배포 전후 단계에서 정책 위반을 차단하는 데 널리 쓰인다. 이 브리핑에서는 Policy as Code의 핵심 개념과 함께 실무에서 자주 쓰이는 관련 도구들을 정리한다.

## 🔑 핵심 요점

- Policy as Code는 보안·컴플라이언스 규칙을 YAML이나 전용 언어로 작성해 코드처럼 버전관리하고 테스트할 수 있게 한다.
- Kubernetes 환경에서는 어드미션 컨트롤러 단계에서 정책을 평가해 잘못된 리소스가 클러스터에 생성되는 것을 사전에 막는다.
- OPA는 범용 정책 엔진으로 Rego라는 전용 쿼리 언어를 사용하며 Kubernetes뿐 아니라 API, 마이크로서비스 등 다양한 곳에 적용 가능하다.
- Kyverno는 Kubernetes 네이티브 정책 엔진으로 새로운 언어를 배우지 않고 YAML만으로 정책을 작성할 수 있어 진입 장벽이 낮다.
- Policy as Code는 GitOps 파이프라인과 결합되어 배포 전 단계에서 정책 위반을 조기에 발견하는 shift-left 보안 전략의 핵심 요소로 쓰인다.
- 조직 전체의 가드레일을 플랫폼 팀이 코드로 관리하면 개발자는 셀프서비스로 안전하게 리소스를 배포할 수 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Policy as Code

조직의 보안, 규정 준수, 운영 규칙을 코드(주로 선언형 설정 파일)로 작성해 사람이 아닌 자동화 시스템이 검증하도록 하는 방법론이다. 정책도 소스코드처럼 Git으로 버전 관리하고 리뷰·테스트할 수 있다.

**왜 필요한가** — 수동 리뷰나 체크리스트에 의존하던 보안·컴플라이언스 검증을 자동화해 실수를 줄이고 속도를 높이기 위해 사용한다.

**발표에서는** — 전체 주제의 핵심 개념으로, 이후 소개되는 OPA, Kyverno 등 구체적인 도구들이 이 방법론을 구현하는 수단으로 다뤄진다.

### Open Policy Agent (OPA)

범용 정책 엔진으로, Rego라는 전용 쿼리 언어로 정책을 정의하고 다양한 시스템(Kubernetes, API 게이트웨이, CI 파이프라인 등)에 적용할 수 있다.

**왜 필요한가** — 애플리케이션별로 흩어진 인가·검증 로직을 하나의 통합된 정책 엔진으로 모아 일관되게 관리하기 위해 쓴다.

**발표에서는** — Policy as Code를 실제로 구현하는 대표적인 범용 엔진으로 소개되며, Kubernetes 어드미션 컨트롤에 많이 활용된다는 맥락에서 다뤄진다.

### Kyverno

Kubernetes 네이티브 정책 엔진으로, 별도의 언어 없이 YAML만으로 정책을 작성할 수 있는 것이 특징이다. 리소스 검증, 변경(mutation), 생성(generation) 정책을 모두 지원한다.

**왜 필요한가** — OPA의 Rego 언어 학습 부담 없이 Kubernetes 사용자가 익숙한 YAML로 빠르게 정책을 작성하고 싶을 때 선택한다.

**발표에서는** — OPA의 대안이자 Kubernetes 환경에 특화된 정책 엔진으로 비교 대상으로 언급된다.

### OPA Gatekeeper

OPA를 Kubernetes 어드미션 컨트롤러로 통합한 프로젝트로, CustomResourceDefinition을 통해 정책을 템플릿화하고 재사용할 수 있게 해준다.

**왜 필요한가** — OPA의 강력한 Rego 기반 정책을 Kubernetes 클러스터 운영에 직접 적용하기 위해 사용한다.

**발표에서는** — OPA를 실제 클러스터 운영에 적용하는 구체적인 방법으로 소개된다.

## 🧭 추구 방향과 흐름

- **Shift-left 보안** — 정책 검증을 배포 이후가 아니라 CI 파이프라인과 어드미션 컨트롤 단계로 앞당겨, 문제가 프로덕션에 도달하기 전에 걸러내는 방향으로 발전하고 있다. Policy as Code는 이러한 조기 검증을 코드 기반으로 자동화하는 핵심 수단이다.
- **플랫폼 엔지니어링과 셀프서비스** — 플랫폼 팀이 가드레일을 정책으로 코드화해 두면, 개발자는 승인 절차 없이도 안전한 범위 내에서 리소스를 스스로 배포할 수 있다. 이는 플랫폼을 하나의 내부 제품으로 제공하는 흐름과 맞닿아 있다.
- **GitOps와의 통합** — 정책 자체도 Git 저장소에 YAML로 저장되어 코드 리뷰와 버전 관리의 대상이 되며, Argo CD 같은 GitOps 도구와 결합해 배포 파이프라인에 자동으로 적용되는 방향으로 발전하고 있다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(kind, minikube 등)에 Kyverno를 설치하고 공식 예제 정책(예: 특정 레이블 필수 지정)을 적용해본다.
2. Open Policy Agent 공식 문서의 Rego 플레이그라운드에서 간단한 정책을 작성해보며 문법을 익힌다.
3. 기존 CI 파이프라인에 OPA나 Conftest를 추가해 Kubernetes manifest나 Terraform 코드에 정책 검사를 적용해본다.
4. Kyverno와 OPA Gatekeeper의 공식 정책 예제 저장소를 비교해보며 두 도구의 작성 방식 차이를 체험해본다.

## 🔗 참고 자료

- [Open Policy Agent 공식 사이트](https://www.openpolicyagent.org) — OPA와 Rego 언어의 개념, 설치, 튜토리얼을 제공하는 공식 문서
- [Kyverno 공식 사이트](https://kyverno.io) — Kubernetes 네이티브 정책 엔진 Kyverno의 설치 가이드와 정책 예제
- [Kubernetes 공식 문서](https://kubernetes.io) — 어드미션 컨트롤러와 CustomResourceDefinition 등 정책 엔진이 동작하는 기반 개념 설명
- [CNCF 공식 사이트](https://www.cncf.io) — OPA와 Kyverno 모두 CNCF 프로젝트로서 생태계 내 위치를 확인할 수 있는 자료
