---
title: "2026-10-14 Crossplane로 시작하는 Infrastructure as Code"
date: 2026-10-14T09:50:35.939805+09:00
tags: ["crossplane", "iac", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 글은 실제 밋업 발표 대신, Crossplane을 중심으로 Kubernetes 기반 Infrastructure as Code(IaC) 생태계를 정리한 브리프입니다. Crossplane은 Kubernetes API를 확장해 클라우드 리소스를 쿠버네티스 커스텀 리소스처럼 선언적으로 관리할 수 있게 해주는 도구로, Terraform과 비교되곤 합니다. 함께 알아두면 좋은 관련 기술로 GitOps 도구인 Argo CD, 정책 관리 도구인 Kyverno, 클러스터 간 네트워킹을 위한 Cilium을 함께 다룹니다. 전체적으로 플랫폼 엔지니어링과 self-service 인프라 제공이라는 큰 흐름 속에서 Crossplane의 위치를 설명합니다.

## 🔑 핵심 요점

- Crossplane은 Kubernetes API를 확장해 클라우드 인프라를 쿠버네티스 리소스처럼 선언적으로 관리하는 도구이다.
- Terraform과 달리 Crossplane은 클러스터 내에서 지속적으로 상태를 reconcile하는 컨트롤러 기반 방식을 사용한다.
- Composition 기능을 통해 여러 클라우드 리소스를 묶어 하나의 커스텀 API로 추상화할 수 있다.
- Argo CD와 결합하면 GitOps 방식으로 인프라 변경 사항을 Git 저장소 기반으로 관리할 수 있다.
- Kyverno 같은 정책 엔진을 함께 쓰면 인프라 리소스 생성 시점에 거버넌스 규칙을 강제할 수 있다.
- 플랫폼 엔지니어링 관점에서 Crossplane은 개발자에게 self-service 인프라 제공을 위한 핵심 빌딩 블록으로 주목받고 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 CNCF 프로젝트로, Kubernetes API를 확장하여 AWS, GCP, Azure 등 클라우드 리소스를 쿠버네티스 커스텀 리소스(CRD)로 표현하고 관리할 수 있게 해줍니다. kubectl이나 YAML 매니페스트로 데이터베이스, VPC 같은 인프라를 선언적으로 정의할 수 있습니다.

**왜 필요한가** — 애플리케이션과 인프라를 동일한 쿠버네티스 선언적 모델과 도구 체인으로 관리하여, 별도의 IaC 툴과 워크플로우를 유지하는 부담을 줄이기 위해 사용합니다.

**발표에서는** — IaC의 대표 사례로 제시되며, Kubernetes 네이티브 방식으로 클라우드 리소스를 다루는 핵심 도구로 소개됩니다.

### Argo CD

Argo CD는 Kubernetes용 GitOps 지속적 배포 도구로, Git 저장소에 선언된 상태를 클러스터에 자동으로 동기화합니다.

**왜 필요한가** — 인프라와 애플리케이션 배포 변경 이력을 Git으로 추적하고, 수동 kubectl apply 없이 자동화된 배포 파이프라인을 구축하기 위해 사용합니다.

**발표에서는** — Crossplane 리소스를 Git 기반으로 관리할 때 함께 조합하는 GitOps 도구로 언급됩니다.

### Kyverno

Kyverno는 Kubernetes 전용 정책 엔진으로, YAML 기반 정책을 통해 리소스 생성/수정 시 검증, 변형, 생성 규칙을 적용합니다.

**왜 필요한가** — 인프라 리소스가 조직의 보안 및 거버넌스 기준을 벗어나지 않도록 자동으로 강제하기 위해 사용합니다.

**발표에서는** — Crossplane으로 생성되는 클라우드 리소스에 정책을 적용하는 보완 도구로 다뤄집니다.

### Cilium

Cilium은 eBPF 기반의 Kubernetes 네트워킹 및 보안 솔루션으로, CNI 플러그인, 네트워크 정책, 관찰성 기능을 제공합니다.

**왜 필요한가** — 멀티 클러스터/멀티 클라우드 환경에서 인프라가 확장될 때 네트워크 연결성과 보안을 세밀하게 제어하기 위해 사용합니다.

**발표에서는** — Crossplane으로 프로비저닝된 여러 클러스터를 연결하는 네트워킹 레이어 사례로 소개됩니다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 self-service 인프라** — Crossplane의 Composition 기능을 통해 플랫폼 팀이 복잡한 클라우드 리소스를 단순한 커스텀 API로 추상화하면, 애플리케이션 개발자는 세부 구현을 몰라도 필요한 인프라를 셀프서비스로 요청할 수 있습니다. 이는 플랫폼을 내부 제품처럼 설계하는 플랫폼 엔지니어링 흐름과 맞닿아 있습니다.
- **GitOps로의 통합** — 인프라 관리를 Argo CD 같은 GitOps 도구와 결합함으로써, 애플리케이션 배포와 인프라 프로비저닝을 동일한 워크플로우와 승인 프로세스로 다룰 수 있게 되는 방향이 강조됩니다.
- **정책 기반 거버넌스 내재화** — Kyverno와 같은 정책 엔진을 인프라 레이어에도 적용하여, 보안과 컴플라이언스 검증을 리소스 생성 이전 단계로 앞당기는 shift-left 경향이 나타납니다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(kind, minikube 등)에 Crossplane을 설치하고 공식 Get Started 가이드를 따라 provider 하나를 연결해 봅니다.
2. 간단한 Composition을 작성해 클라우드 리소스 하나를 추상화된 커스텀 API로 노출시켜 봅니다.
3. Argo CD 공식 문서를 참고해 Crossplane 리소스 매니페스트를 Git 저장소 기반으로 동기화하는 GitOps 파이프라인을 구성해 봅니다.
4. Kyverno 공식 문서의 정책 예제를 참고해 Crossplane 리소스 생성 시 적용할 간단한 정책을 작성해 봅니다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념과 Composition, Provider 등 핵심 기능을 설명하는 공식 자료
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 동기화 방식을 이해하기 위한 공식 문서
- [Kyverno 공식 홈페이지](https://kyverno.io) — Kubernetes 정책 엔진으로 거버넌스를 적용하는 방법에 대한 공식 자료
- [Cilium 공식 홈페이지](https://cilium.io) — eBPF 기반 네트워킹/보안 솔루션에 대한 공식 자료
- [CNCF 공식 홈페이지](https://www.cncf.io) — Crossplane을 포함한 클라우드 네이티브 생태계 전반의 프로젝트 현황을 확인할 수 있는 자료
