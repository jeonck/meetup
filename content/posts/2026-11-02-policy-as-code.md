---
title: "2026-11-02 Policy as Code로 클러스터 거버넌스 자동화하기"
date: 2026-11-02T10:13:09.839202+09:00
tags: ["policy-as-code", "kubernetes", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

이 글은 Policy as Code라는 개념을 중심으로, Kubernetes 환경에서 정책을 코드로 선언하고 자동으로 검증·강제하는 흐름을 정리한다. Kyverno와 OPA/Gatekeeper 같은 도구가 어떻게 보안, 규정 준수, 리소스 관리 정책을 코드화하는지 살펴본다. 이와 함께 GitOps 도구인 Argo CD와의 연계를 통해 정책 변경도 Git 기반으로 관리하는 방향을 설명한다. 전체적으로 수동 리뷰와 체크리스트에 의존하던 거버넌스를 자동화된 코드 기반 시스템으로 전환하는 흐름을 다룬다.

## 🔑 핵심 요점

- Policy as Code는 보안·규정·운영 정책을 코드로 선언하고 자동으로 검증하는 접근 방식이다.
- Kubernetes 클러스터에서는 Kyverno나 OPA/Gatekeeper 같은 admission controller가 정책을 실시간으로 강제한다.
- 정책을 코드로 관리하면 Git을 통한 버전 관리, 리뷰, 롤백이 가능해진다.
- GitOps 도구인 Argo CD와 결합하면 정책 변경도 애플리케이션 배포와 동일한 파이프라인으로 관리할 수 있다.
- 수동 체크리스트 기반의 거버넌스보다 일관성과 재현성이 높아진다.
- 정책 위반을 사전에 차단(shift-left)함으로써 운영 중 사고를 줄이는 효과를 기대할 수 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Kyverno

Kubernetes 전용으로 설계된 정책 엔진으로, YAML 형식으로 정책을 작성할 수 있어 별도의 언어를 배우지 않아도 된다.

**왜 필요한가** — 리소스 생성·수정 시점에 보안 규칙이나 베스트 프랙티스를 자동으로 검증하고 강제하기 위해 사용한다.

**발표에서는** — Policy as Code를 실제로 구현하는 대표적인 도구로 소개되며, Kubernetes 매니페스트와 동일한 문법으로 정책을 작성할 수 있다는 점이 강조되었다.

### OPA (Open Policy Agent) / Gatekeeper

범용 정책 엔진인 OPA와 이를 Kubernetes에 통합한 Gatekeeper는 Rego라는 전용 언어로 정책을 정의한다.

**왜 필요한가** — Kubernetes뿐 아니라 다양한 시스템에 걸쳐 일관된 정책 엔진을 적용하고 싶을 때 사용한다.

**발표에서는** — Kyverno와 비교되는 대안 도구로 언급되며, 더 범용적이지만 학습 곡선이 있다는 맥락에서 다뤄졌다.

### Argo CD

Git 저장소의 상태를 Kubernetes 클러스터에 자동으로 동기화하는 GitOps 도구다.

**왜 필요한가** — 애플리케이션과 정책 설정 변경을 Git 커밋 기반으로 추적하고 자동 배포하기 위해 사용한다.

**발표에서는** — 정책 매니페스트도 애플리케이션과 동일하게 GitOps 파이프라인에 태워 배포하는 흐름을 설명하는 데 활용되었다.

### Kubernetes Admission Controller

클러스터에 리소스가 생성되기 전에 가로채서 검증하거나 수정할 수 있는 Kubernetes 확장 지점이다.

**왜 필요한가** — 정책 엔진들이 실제로 정책을 강제할 수 있는 기술적 기반을 제공하기 위해 존재한다.

**발표에서는** — Kyverno와 Gatekeeper가 동작하는 기반 메커니즘으로 설명되었다.

## 🧭 추구 방향과 흐름

- **Shift-left 거버넌스** — 정책 위반을 운영 단계가 아닌 배포 이전 단계에서 차단하려는 방향이다. 리소스가 클러스터에 적용되기 전에 admission controller가 검증하는 구조가 이를 뒷받침한다.
- **GitOps와 정책의 통합** — 정책 자체도 코드로 취급해 Git 저장소에서 버전 관리하고 Argo CD 같은 도구로 배포하는 방향으로 나아가고 있다. 애플리케이션 배포와 정책 배포의 파이프라인을 통일하려는 흐름이다.
- **셀프서비스 플랫폼에서의 안전장치** — 개발자가 직접 리소스를 배포할 수 있는 셀프서비스 환경에서, Policy as Code가 플랫폼 팀 대신 자동으로 가드레일 역할을 하는 방향으로 발전하고 있다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(kind, minikube 등)에 Kyverno를 설치하고 공식 샘플 정책을 적용해본다.
2. Kyverno 공식 문서의 Policy 예제를 따라 리소스 라벨 필수화 같은 간단한 정책부터 작성해본다.
3. 기존 Argo CD 파이프라인이 있다면 정책 매니페스트를 별도 Git 저장소로 분리해 GitOps로 배포하는 구조를 실험해본다.
4. OPA의 Rego 플레이그라운드에서 간단한 정책을 작성해보며 Kyverno와의 차이를 비교해본다.

## 🔗 참고 자료

- [Kyverno](https://kyverno.io) — Policy as Code를 YAML로 구현하는 대표 도구의 공식 문서
- [Open Policy Agent](https://www.openpolicyagent.org) — 범용 정책 엔진 OPA의 공식 홈페이지
- [Argo CD](https://argo-cd.readthedocs.io) — 정책을 GitOps 파이프라인으로 배포하는 데 쓰이는 도구의 공식 문서
- [Kubernetes](https://kubernetes.io) — Admission controller 등 정책 강제의 기반이 되는 플랫폼 공식 문서
- [CNCF](https://www.cncf.io) — Policy as Code 관련 프로젝트들이 속한 클라우드 네이티브 생태계 재단
