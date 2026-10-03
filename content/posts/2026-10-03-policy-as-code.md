---
title: "2026-10-03 Policy as Code로 쿠버네티스 거버넌스 자동화하기"
date: 2026-10-03T09:54:40.026059+09:00
tags: ["policy-as-code", "kyverno", "kubernetes-security", "tech-brief"]
---
## 오늘의 기술 토픽

> **Policy as Code**

이 밋업에서는 별도의 전사 트랜스크립트 없이 Policy as Code라는 주제를 중심으로 브리핑을 구성했습니다. Policy as Code는 보안, 규정 준수, 운영 규칙을 코드로 정의하고 CI/CD 파이프라인이나 쿠버네티스 클러스터 안에서 자동으로 강제하는 접근 방식입니다. Kyverno, OPA/Gatekeeper, Conftest 같은 도구들이 함께 다뤄지며, 플랫폼 팀이 수작업 리뷰 대신 코드 기반 정책으로 일관성을 확보하는 흐름을 소개합니다.

## 🔑 핵심 요점

- Policy as Code는 보안·컴플라우언스 규칙을 YAML이나 Rego 같은 코드로 작성해 자동으로 검증하는 방식입니다.
- 쿠버네티스 환경에서는 Kyverno나 OPA/Gatekeeper 같은 어드미션 컨트롤러가 정책을 실시간으로 강제합니다.
- 정책을 코드로 관리하면 Git을 통해 버전 관리, 리뷰, 롤백이 가능해집니다.
- CI 단계에서 Conftest 같은 도구로 정책을 미리 검사하면 배포 전에 문제를 조기에 발견할 수 있습니다.
- 플랫폼 팀은 정책 강제를 통해 개발자에게 안전한 셀프서비스 환경을 제공하려는 방향을 지향합니다.
- GitOps 워크플로우와 Policy as Code를 결합하면 선언적 정책 관리가 자연스럽게 이어집니다.

## 🛠 핵심 기술 쉽게 이해하기

### Kyverno

Kyverno는 쿠버네티스 네이티브 정책 엔진으로, YAML만으로 정책을 작성할 수 있어 별도의 정책 언어를 배우지 않아도 됩니다. 어드미션 컨트롤러로 동작해 리소스가 생성되거나 수정될 때 규칙을 검사하고 필요하면 거부하거나 값을 자동으로 수정합니다.

**왜 필요한가** — 쿠버네티스 매니페스트가 보안 기준이나 조직 규칙을 지키는지 자동으로 검증하기 위해 사용합니다.

**발표에서는** — Policy as Code를 쿠버네티스에 적용하는 대표적인 도구로 언급되는 맥락에서 다뤄졌습니다.

### OPA (Open Policy Agent) / Gatekeeper

OPA는 범용 정책 엔진으로 Rego라는 전용 언어로 정책을 작성하며, 쿠버네티스뿐 아니라 API 게이트웨이, 마이크로서비스 등 다양한 환경에 적용할 수 있습니다. Gatekeeper는 OPA를 쿠버네티스 어드미션 컨트롤러로 통합한 프로젝트입니다.

**왜 필요한가** — 여러 시스템에 걸쳐 일관된 정책 로직을 재사용하고 중앙에서 관리하기 위해 사용합니다.

**발표에서는** — Kyverno와 비교되는 또 다른 Policy as Code 구현체로 소개되었습니다.

### Conftest

Conftest는 Rego 정책을 이용해 YAML, JSON, Terraform 등 다양한 설정 파일을 CI 파이프라인에서 검사할 수 있게 해주는 CLI 도구입니다.

**왜 필요한가** — 배포 전에 정책 위반을 조기에 잡아내 셋째 안전망을 CI 단계에 추가하기 위해 사용합니다.

**발표에서는** — CI/CD 파이프라인에 Policy as Code를 접목하는 사례로 언급되었습니다.

### cert-manager

cert-manager는 쿠버네티스 클러스터 안에서 TLS 인증서 발급과 갱신을 자동화하는 컨트롤러입니다.

**왜 필요한가** — 인증서 관리 같은 보안 관련 운영 작업도 정책 기반 자동화의 한 축으로 다뤄질 수 있습니다.

**발표에서는** — Policy as Code와 함께 클러스터 보안 자동화 맥락에서 보조적으로 언급되는 관련 기술로 포함되었습니다.

## 🧭 추구 방향과 흐름

- **Shift-left 보안** — 정책 검증을 배포 이후가 아니라 CI 단계와 코드 리뷰 시점으로 앞당기는 흐름입니다. Conftest처럼 파이프라인 초기에 정책을 검사하는 도구들이 이 방향을 뒷받침합니다.
- **플랫폼을 제품처럼 (Platform as a Product)** — 플랫폼 팀이 정책을 코드로 미리 정의해두면 개발자는 가드레일 안에서 자유롭게 셀프서비스로 리소스를 배포할 수 있습니다. Kyverno 같은 어드미션 컨트롤러가 이 가드레일 역할을 합니다.
- **GitOps와의 결합** — 정책 자체를 Git에 선언적으로 저장하고 버전 관리하면서, Argo CD 같은 GitOps 도구와 함께 배포 파이프라인 전체를 코드로 관리하는 방향으로 나아가고 있습니다.

## 🚀 바로 활용하기

1. 로컬 쿠버네티스 클러스터(kind, minikube 등)에 Kyverno를 설치하고 샘플 정책(ClusterPolicy)을 적용해 어드미션 컨트롤이 동작하는 과정을 직접 확인해 보세요.
2. Conftest 공식 문서를 따라 간단한 Rego 정책을 작성하고, 로컬 YAML 파일을 대상으로 CI처럼 검사해 보세요.
3. Kyverno와 OPA/Gatekeeper 중 하나를 선택해 같은 정책(예: 이미지 태그 latest 금지)을 양쪽에 구현해보며 차이를 비교해 보세요.
4. 기존에 사용 중인 CI 파이프라인에 정책 검사 단계를 추가해 배포 전 자동 검증을 실험해 보세요.

## 🔗 참고 자료

- [Kyverno](https://kyverno.io) — 쿠버네티스 네이티브 Policy as Code 엔진의 공식 문서
- [Open Policy Agent](https://www.openpolicyagent.org) — 범용 정책 엔진 OPA와 Rego 언어 공식 문서
- [Kubernetes](https://kubernetes.io) — 어드미션 컨트롤러와 정책 적용 대상이 되는 쿠버네티스 공식 문서
- [Argo CD](https://argo-cd.readthedocs.io) — GitOps와 정책 관리를 결합하는 흐름의 대표 도구
- [cert-manager](https://cert-manager.io) — 클러스터 보안 자동화의 관련 기술인 인증서 관리 도구 공식 문서
- [CNCF](https://www.cncf.io) — Policy as Code 관련 도구들이 속한 클라우드 네이티브 생태계 공식 사이트
