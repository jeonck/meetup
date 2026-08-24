---
title: "2026-08-25 Crossplane으로 시작하는 Infrastructure as Code"
date: 2026-08-25T07:21:50.687538+09:00
tags: ["crossplane", "iac", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 브리핑은 별도 밋업 발표 없이, Crossplane을 중심으로 한 Kubernetes 기반 Infrastructure as Code(IaC) 흐름을 정리한 자료입니다. Crossplane은 Kubernetes API를 확장해 클라우드 리소스를 선언적으로 관리할 수 있게 해주는 프로젝트로, Terraform 같은 기존 IaC 도구와 비교되며 최근 플랫폼 엔지니어링 생태계에서 주목받고 있습니다. 이 브리핑에서는 Crossplane과 함께 자주 언급되는 연관 기술들을 소개하고, 생태계가 나아가는 방향과 학습을 시작하는 방법을 정리했습니다.

## 🔑 핵심 요점

- Crossplane은 Kubernetes API를 확장해 클라우드 리소스(DB, 네트워크, 스토리지 등)를 Kubernetes 오브젝트처럼 선언적으로 관리한다.
- Crossplane은 Provider를 통해 AWS, GCP, Azure 등 다양한 클라우드와 SaaS 리소스를 하나의 컨트롤 플레인에서 다룰 수 있게 해준다.
- Composition 기능을 사용하면 여러 리소스를 조합한 커스텀 API(예: '데이터베이스 하나 주세요')를 팀 내부에 제공할 수 있다.
- GitOps 도구인 Argo CD와 Crossplane을 함께 쓰면 애플리케이션 배포와 인프라 프로비저닝을 동일한 파이프라인에서 관리할 수 있다.
- 정책 관리 도구인 Kyverno를 결합하면 Crossplane으로 생성되는 리소스에 대한 거버넌스 규칙을 강제할 수 있다.
- 이러한 흐름은 개발자에게 셀프서비스 인프라를 제공하는 '플랫폼 엔지니어링' 트렌드와 맞닿아 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes API를 확장하여 클라우드 프로바이더의 리소스(가상머신, 데이터베이스, 네트워크 등)를 Kubernetes 커스텀 리소스로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다. kubectl이나 GitOps 도구로 인프라를 코드처럼 다룰 수 있습니다.

**왜 필요한가** — 여러 클라우드에 흩어진 인프라를 각기 다른 도구로 관리하는 번거로움을 없애고, Kubernetes를 단일 컨트롤 플레인으로 삼아 애플리케이션과 인프라를 통합 관리하기 위해 사용됩니다.

**발표에서는** — 이번 브리핑의 중심 주제로, Kubernetes 네이티브 방식의 IaC 도구로 소개되었습니다.

### Terraform

Terraform은 HashiCorp에서 만든 대표적인 Infrastructure as Code 도구로, HCL이라는 자체 언어로 인프라 리소스를 정의하고 프로비저닝합니다.

**왜 필요한가** — 선언적 설정 파일로 인프라 변경 이력을 코드로 관리하고, 반복 가능한 방식으로 인프라를 구축하기 위해 널리 쓰입니다.

**발표에서는** — Crossplane과 비교 대상으로 언급되는 기존 IaC 도구로, Kubernetes 네이티브 접근과의 차이를 이해하는 데 참고 기술로 다뤄졌습니다.

### Argo CD

Argo CD는 Kubernetes를 위한 GitOps 기반 지속적 배포(CD) 도구로, Git 저장소의 상태를 클러스터에 자동으로 동기화합니다.

**왜 필요한가** — 수동 배포로 인한 실수를 줄이고, Git을 단일 진실 공급원(Single Source of Truth)으로 삼아 배포와 인프라 변경을 추적 가능하게 만들기 위해 사용됩니다.

**발표에서는** — Crossplane 리소스를 GitOps 방식으로 관리할 때 함께 사용되는 도구로 언급되었습니다.

### Kyverno

Kyverno는 Kubernetes 전용 정책 엔진으로, YAML 기반으로 리소스 생성/수정 시 규칙을 검증하거나 자동으로 변경할 수 있습니다.

**왜 필요한가** — 클러스터에 생성되는 리소스(Crossplane이 만드는 클라우드 리소스 포함)가 조직의 보안 및 거버넌스 규칙을 따르도록 강제하기 위해 사용됩니다.

**발표에서는** — Crossplane과 결합해 인프라 거버넌스를 강화하는 연관 기술로 소개되었습니다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링(Platform Engineering)** — Crossplane의 Composition 기능은 개발자가 복잡한 클라우드 인프라 지식 없이도 셀프서비스로 리소스를 요청할 수 있게 해주는 방향을 지향합니다. 이는 플랫폼 팀이 표준화된 API를 제공하고 개발자는 그 위에서 빠르게 움직이는 '플랫폼을 제품처럼' 접근하는 트렌드와 일치합니다.
- **Kubernetes 중심의 통합 컨트롤 플레인** — 애플리케이션 배포(Argo CD)와 인프라 프로비저닝(Crossplane), 정책 관리(Kyverno)를 모두 Kubernetes API 위에서 처리하는 흐름이 강조됩니다. 이는 여러 도구를 따로 운영하지 않고 하나의 선언적 모델로 통합하려는 생태계 방향을 보여줍니다.
- **GitOps로의 확장** — 인프라 프로비저닝까지 Git 기반 워크플로우로 편입시켜, 코드 리뷰와 버전 관리 프로세스 안에서 인프라 변경을 다루는 방향이 나타납니다.

## 🚀 바로 활용하기

1. 로컬 환경(kind, minikube 등)에 Kubernetes 클러스터를 만들고 Crossplane을 설치해 기본 Provider(AWS/GCP 등)를 연결해본다.
2. Crossplane 공식 문서의 Get Started 가이드를 따라 간단한 Managed Resource(예: S3 버킷)를 생성해본다.
3. Composition을 사용해 여러 리소스를 조합한 커스텀 API를 하나 만들어보고, 팀 내부 셀프서비스 시나리오를 시뮬레이션해본다.
4. 기존에 Terraform으로 관리하던 리소스 중 하나를 Crossplane으로 마이그레이션해보며 차이점을 비교한다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념, Provider, Composition에 대한 공식 설명과 문서 링크를 제공한다.
- [Kubernetes 공식 문서](https://kubernetes.io) — Crossplane이 확장하는 기반 플랫폼인 Kubernetes API와 커스텀 리소스 개념을 이해하는 데 필요하다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — Crossplane 리소스를 GitOps 방식으로 관리하는 방법을 다룬다.
- [Kyverno 공식 홈페이지](https://kyverno.io) — Crossplane으로 생성되는 리소스에 정책을 적용하는 방법을 확인할 수 있다.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Crossplane을 포함한 클라우드 네이티브 생태계 전반의 프로젝트 현황을 확인할 수 있다.
