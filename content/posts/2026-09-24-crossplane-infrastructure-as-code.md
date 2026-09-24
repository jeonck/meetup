---
title: "2026-09-24 Crossplane으로 시작하는 Infrastructure as Code"
date: 2026-09-24T09:12:36.781806+09:00
tags: ["crossplane", "iac", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 브리프는 실제 밋업 발표 없이, Crossplane을 중심으로 한 Kubernetes 기반 Infrastructure as Code(IaC) 생태계를 정리한 자료입니다. Crossplane은 클라우드 리소스를 Kubernetes API로 관리할 수 있게 해주는 오픈소스 프로젝트로, Terraform과 같은 전통적 IaC 도구와 비교되며 최근 플랫폼 엔지니어링 흐름에서 주목받고 있습니다. 함께 살펴볼 Argo CD, Kyverno, Cilium은 Crossplane과 함께 쓰이며 GitOps 배포, 정책 관리, 네트워킹을 보완하는 도구들입니다. 전체적으로 '플랫폼을 제품처럼 만드는' 방향, 즉 개발자에게 셀프서비스 인프라를 제공하는 흐름을 짚어봅니다.

## 🔑 핵심 요점

- Crossplane은 클라우드 리소스를 Kubernetes 커스텀 리소스(CRD)로 선언적으로 관리하는 오픈소스 프로젝트입니다.
- 기존 Terraform 방식과 달리 Crossplane은 Kubernetes 컨트롤러 패턴을 사용해 리소스 상태를 지속적으로 조정(reconcile)합니다.
- Argo CD와 결합하면 Git 저장소의 매니페스트 변경만으로 인프라와 애플리케이션을 함께 GitOps 방식으로 배포할 수 있습니다.
- Kyverno 같은 정책 엔진을 함께 사용하면 Crossplane으로 생성되는 리소스에 조직의 보안·컴플라이언스 규칙을 강제할 수 있습니다.
- Cilium은 Crossplane이 프로비저닝한 네트워크 인프라 위에서 Kubernetes 네트워킹과 관측성을 담당하는 역할을 합니다.
- 이 생태계 전반은 '플랫폼 엔지니어링'과 '개발자 셀프서비스'라는 큰 흐름 속에서 서로 연결되어 있습니다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 AWS, GCP, Azure 같은 클라우드의 리소스(데이터베이스, 네트워크, 스토리지 등)를 Kubernetes의 커스텀 리소스로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다. Kubernetes API를 확장해 클라우드 인프라까지 kubectl과 YAML로 다룰 수 있게 만들어줍니다.

**왜 필요한가** — 여러 클라우드와 도구에 흩어진 인프라 관리 방식을 Kubernetes라는 하나의 컨트롤 플레인으로 통합하고, 개발자가 셀프서비스로 인프라를 요청할 수 있게 하기 위해 사용됩니다.

**발표에서는** — 이번 브리프의 핵심 주제로, IaC 도구로서 Crossplane의 개념과 Kubernetes 네이티브 접근 방식이 다뤄졌습니다.

### Argo CD

Argo CD는 Git 저장소에 정의된 상태를 Kubernetes 클러스터에 자동으로 동기화하는 GitOps 도구입니다.

**왜 필요한가** — 수동 배포로 인한 실수를 줄이고, Git을 단일 진실 공급원(source of truth)으로 삼아 배포 이력을 추적하기 위해 사용됩니다.

**발표에서는** — Crossplane과 함께 사용되어 인프라 정의까지 GitOps 워크플로에 포함시키는 방식으로 언급되었습니다.

### Kyverno

Kyverno는 Kubernetes 리소스에 정책을 정의하고 자동으로 검증·수정·생성할 수 있는 정책 엔진입니다.

**왜 필요한가** — 클러스터 내 리소스가 보안 및 조직 규칙을 준수하도록 강제하기 위해 사용됩니다.

**발표에서는** — Crossplane이 생성하는 클라우드 리소스에 정책을 적용하는 보완 도구로 소개되었습니다.

### Cilium

Cilium은 eBPF 기술을 기반으로 한 Kubernetes 네트워킹, 보안, 관측성 솔루션입니다.

**왜 필요한가** — 클러스터 내부 트래픽을 세밀하게 제어하고 네트워크 계층의 가시성을 확보하기 위해 사용됩니다.

**발표에서는** — Crossplane으로 프로비저닝된 네트워크 인프라 위에서 동작하는 연관 기술로 언급되었습니다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 셀프서비스 인프라** — Crossplane을 중심으로 한 흐름은 개발자가 인프라팀에 티켓을 넣지 않고도 Kubernetes API를 통해 필요한 리소스를 직접 요청하는 셀프서비스 플랫폼을 지향합니다. 이는 플랫폼을 내부 제품처럼 만드는 '플랫폼 as a product' 접근과 맞닿아 있습니다.
- **Kubernetes를 단일 컨트롤 플레인으로** — 애플리케이션뿐 아니라 클라우드 인프라, 정책, 네트워킹까지 모두 Kubernetes API로 관리하려는 방향입니다. Crossplane, Kyverno, Cilium이 각각 인프라·정책·네트워킹을 담당하며 하나의 생태계로 수렴합니다.
- **GitOps로의 확장** — 애플리케이션 배포에 머물던 GitOps를 인프라 프로비저닝까지 확장하려는 흐름으로, Argo CD와 Crossplane의 조합이 대표적인 사례로 언급됩니다.

## 🚀 바로 활용하기

1. Crossplane 공식 문서의 Get Started 가이드를 따라 로컬 Kubernetes 클러스터(kind, minikube 등)에 Crossplane을 설치해봅니다.
2. AWS/GCP 등 하나의 Provider를 설치하고 간단한 리소스(S3 버킷, 데이터베이스 등)를 Kubernetes 매니페스트로 선언해 생성해봅니다.
3. Argo CD를 함께 설치해 Crossplane 리소스 정의를 Git 저장소에 커밋하고 자동 동기화되는 흐름을 체험해봅니다.
4. Kyverno의 정책 예제를 참고해 Crossplane이 생성한 리소스에 간단한 검증 정책을 적용해봅니다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념과 아키텍처를 소개하는 공식 시작점
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 자동화 도구인 Argo CD의 설치 및 사용법 문서
- [Kyverno 공식 홈페이지](https://kyverno.io) — Kubernetes 정책 엔진 Kyverno의 정책 작성 가이드
- [Cilium 공식 홈페이지](https://cilium.io) — eBPF 기반 네트워킹 도구 Cilium의 개념과 문서
- [Kubernetes 공식 문서](https://kubernetes.io) — Crossplane이 확장하는 Kubernetes API 및 CRD의 기본 개념 문서
- [CNCF](https://www.cncf.io) — Crossplane, Cilium, Argo CD, Kyverno가 모두 속한 클라우드 네이티브 생태계 재단
