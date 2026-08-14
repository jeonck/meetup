---
title: "2026-08-15 Crossplane로 시작하는 Infrastructure as Code"
date: 2026-08-15T07:19:21.371310+09:00
tags: ["crossplane", "iac", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 브리핑은 별도의 밋업 발표 없이 Crossplane을 중심으로 한 Infrastructure as Code(IaC) 흐름을 정리한 것이다. Kubernetes API를 확장해 클라우드 리소스를 선언적으로 관리하는 Crossplane의 개념과, 이를 둘러싼 GitOps 및 플랫폼 엔지니어링 생태계를 함께 살펴본다. 실제 발표 Q&A는 없었으며, 입문자가 바로 시도해볼 수 있는 학습 경로에 초점을 맞췄다.

## 🔑 핵심 요점

- Crossplane은 Kubernetes API를 확장하여 클라우드 인프라 리소스를 Kubernetes 오브젝트처럼 선언적으로 관리할 수 있게 해준다.
- 기존 Terraform이 CLI와 상태 파일 기반이라면, Crossplane은 Kubernetes 컨트롤러 패턴으로 지속적인 리컨실리에이션을 수행한다.
- Crossplane의 Composition 기능을 사용하면 여러 클라우드 리소스를 조합한 커스텀 API를 만들어 팀에 셀프서비스로 제공할 수 있다.
- GitOps 도구(Argo CD 등)와 결합하면 인프라 변경도 애플리케이션 배포처럼 Git 저장소를 단일 진실 공급원으로 관리할 수 있다.
- 플랫폼 엔지니어링 관점에서 Crossplane은 개발자에게 인프라 복잡도를 감추고 표준화된 API만 노출하는 내부 개발자 플랫폼(IDP)의 핵심 구성요소로 활용된다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes 위에서 동작하는 오픈소스 프레임워크로, AWS, GCP, Azure 등 클라우드 리소스를 Kubernetes의 Custom Resource로 정의하고 관리할 수 있게 해준다. kubectl이나 YAML manifest로 데이터베이스, 네트워크, 스토리지 같은 클라우드 자원을 다룰 수 있다.

**왜 필요한가** — 여러 클라우드와 도구가 뒤섞인 인프라를 하나의 통일된 API와 워크플로우로 관리하고, 인프라 프로비저닝을 애플리케이션 배포와 같은 방식으로 자동화하기 위해 사용한다.

**발표에서는** — 이번 브리핑의 중심 주제로, Kubernetes 네이티브 방식의 IaC 도구로 소개되었다.

### Kubernetes

Kubernetes는 컨테이너화된 애플리케이션을 배포, 확장, 운영하기 위한 오픈소스 컨테이너 오케스트레이션 플랫폼이다.

**왜 필요한가** — Crossplane이 동작하는 기반 플랫폼으로, 선언적 API와 컨트롤러 패턴을 클라우드 인프라 관리에도 그대로 활용할 수 있게 해준다.

**발표에서는** — Crossplane의 근간이 되는 API 확장 메커니즘(CRD, 컨트롤러)의 출처로 언급되었다.

### Terraform

Terraform은 HashiCorp에서 만든 대표적인 IaC 도구로, HCL이라는 선언적 언어로 인프라를 코드로 정의하고 CLI로 적용한다.

**왜 필요한가** — Crossplane과 함께 IaC 도구를 비교할 때 자주 언급되는 기준점으로, 상태 파일 기반 접근 방식과 Kubernetes 네이티브 접근 방식의 차이를 이해하는 데 도움이 된다.

**발표에서는** — Crossplane과의 비교 대상으로 함께 다뤄졌다.

### Argo CD

Argo CD는 Kubernetes를 위한 GitOps 지속적 배포 도구로, Git 저장소의 상태를 클러스터에 자동으로 동기화한다.

**왜 필요한가** — Crossplane으로 정의한 인프라 매니페스트를 Git 기반으로 관리하고 자동 배포하기 위해 함께 사용된다.

**발표에서는** — Crossplane 매니페스트를 GitOps 방식으로 운영하는 조합으로 소개되었다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 셀프서비스 인프라** — 인프라팀이 클라우드 리소스를 직접 프로비저닝하는 대신, Crossplane의 Composition으로 표준화된 API를 만들어 개발자가 셀프서비스로 인프라를 요청하는 방향으로 나아가고 있다. 이는 내부 개발자 플랫폼(IDP) 구축의 핵심 흐름이다.
- **인프라와 애플리케이션의 GitOps 통합** — 인프라 프로비저닝도 애플리케이션 배포와 동일하게 Git을 단일 진실 공급원으로 삼아 관리하는 흐름이 강화되고 있으며, Crossplane과 Argo CD의 조합이 대표적인 사례로 다뤄진다.

## 🚀 바로 활용하기

1. 로컬 kind 또는 minikube 클러스터에 Crossplane을 설치하고 공식 Get Started 가이드를 따라 첫 Provider를 연결해본다.
2. AWS/GCP 등 하나의 Provider를 설치한 뒤 간단한 리소스(S3 버킷 등)를 Kubernetes manifest로 프로비저닝해본다.
3. Composition 문서를 읽고 여러 리소스를 조합한 커스텀 XRD(Composite Resource Definition)를 직접 만들어본다.
4. Argo CD와 Crossplane을 함께 구성해 GitOps 기반 인프라 배포 파이프라인을 실습해본다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념, 설치 방법, Get Started 가이드를 제공한다.
- [Crossplane 공식 문서](https://docs.crossplane.io) — Provider, Composition, XRD 등 핵심 개념에 대한 상세 문서.
- [Kubernetes 공식 홈페이지](https://kubernetes.io) — Crossplane이 동작하는 기반 플랫폼인 Kubernetes의 개념과 문서를 제공한다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — Crossplane과 함께 GitOps 워크플로우를 구성할 때 참고할 수 있는 공식 문서.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Crossplane이 소속된 CNCF 프로젝트 생태계와 클라우드 네이티브 트렌드를 확인할 수 있다.
