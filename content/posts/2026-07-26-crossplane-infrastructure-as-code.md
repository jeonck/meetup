---
title: "2026-07-26 Crossplane으로 시작하는 Infrastructure as Code"
date: 2026-07-26T07:52:23.595493+09:00
tags: ["crossplane", "iac", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 글에서는 실제 밋업 발표 대신, Crossplane을 중심으로 한 Infrastructure as Code(IaC) 생태계를 정리한다. Crossplane은 Kubernetes API를 확장해 클라우드 리소스를 선언적으로 관리할 수 있게 해주는 도구로, Terraform과 같은 전통적 IaC 도구와 비교되며 최근 플랫폼 엔지니어링 진영에서 주목받고 있다. Crossplane과 함께 자주 언급되는 Argo CD, Terraform, Kubernetes Operator 패턴을 함께 살펴보고, 이 생태계가 어디로 향하고 있는지 정리한다.

## 🔑 핵심 요점

- Crossplane은 Kubernetes Custom Resource와 Controller 패턴을 이용해 클라우드 인프라를 코드로 관리하는 오픈소스 프로젝트다.
- 기존 Terraform이 CLI와 상태 파일 기반이라면, Crossplane은 Kubernetes API 서버를 통해 리소스를 선언적으로 관리한다는 차이가 있다.
- Crossplane의 Composition 기능을 사용하면 여러 클라우드 리소스를 하나의 커스텀 API로 추상화해 팀 내부에 제공할 수 있다.
- Argo CD와 결합하면 GitOps 방식으로 인프라 변경 사항을 자동 배포할 수 있다.
- 플랫폼 엔지니어링 트렌드에서 Crossplane은 '내부 개발자 플랫폼(IDP)'을 만드는 핵심 빌딩 블록으로 자리잡고 있다.
- 처음 시작할 때는 Provider 설치와 간단한 Managed Resource 생성부터 연습하는 것이 좋다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes API를 확장하여 AWS, GCP, Azure 같은 클라우드 리소스를 Kubernetes 커스텀 리소스처럼 선언적으로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트다. Kubernetes를 다뤄본 사람이라면 익숙한 YAML 매니페스트로 인프라를 표현할 수 있다.

**왜 필요한가** — 여러 클라우드에 흩어진 인프라를 하나의 API로 통합 관리하고, 애플리케이션과 인프라를 같은 방식(Kubernetes 선언적 모델)으로 다루기 위해 사용한다.

**발표에서는** — 이번 글의 중심 주제로, Kubernetes 네이티브 방식의 IaC 도구로 소개된다.

### Terraform

Terraform은 HashiCorp에서 만든 대표적인 IaC 도구로, HCL이라는 자체 언어로 인프라를 코드로 작성하고 상태 파일(state file)을 통해 리소스를 관리한다.

**왜 필요한가** — 수동으로 콘솔에서 인프라를 클릭해 만드는 대신, 코드로 버전 관리하며 반복 가능하게 인프라를 구축하기 위해 쓰인다.

**발표에서는** — Crossplane과 비교 대상으로 언급되며, Kubernetes API 기반 접근과 CLI/상태 파일 기반 접근의 차이를 설명하는 데 활용된다.

### Argo CD

Argo CD는 Kubernetes를 위한 GitOps 배포 도구로, Git 저장소에 정의된 상태를 클러스터에 자동으로 동기화한다.

**왜 필요한가** — 인프라와 애플리케이션 변경 사항을 Git을 단일 진실 공급원(source of truth)으로 삼아 자동화된 방식으로 배포하기 위해 사용한다.

**발표에서는** — Crossplane과 결합해 인프라 변경까지 GitOps 파이프라인에 포함시키는 조합으로 소개된다.

### Kubernetes Operator Pattern

Operator 패턴은 Kubernetes Controller가 커스텀 리소스의 원하는 상태(desired state)를 지속적으로 감시하고 실제 상태를 맞춰가는 설계 방식이다.

**왜 필요한가** — 복잡한 운영 작업(백업, 스케일링, 리소스 프로비저닝 등)을 사람이 아닌 소프트웨어가 자동으로 수행하게 하기 위해 사용한다.

**발표에서는** — Crossplane이 내부적으로 이 패턴을 기반으로 동작한다는 맥락에서 함께 다뤄진다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 내부 개발자 플랫폼(IDP)** — 인프라 관리를 중앙 팀이 커스텀 API로 추상화해 애플리케이션 개발자에게 셀프서비스로 제공하는 흐름이 강화되고 있다. Crossplane의 Composition 기능이 이런 추상화를 가능하게 하는 핵심 요소로 다뤄진다.
- **GitOps로의 통합** — 애플리케이션 배포뿐 아니라 인프라 프로비저닝까지 Git 기반 워크플로우로 통합하는 방향이 뚜렷해지고 있으며, Crossplane과 Argo CD의 조합이 그 대표 사례로 언급된다.
- **Kubernetes를 인프라 관리의 표준 API로 삼는 흐름** — 클라우드 리소스, 애플리케이션, 정책 등을 모두 Kubernetes API 하나로 다루려는 경향이 커지고 있으며, Crossplane은 이 흐름의 대표적인 구현체로 자리잡고 있다.

## 🚀 바로 활용하기

1. 로컬에 kind나 minikube로 Kubernetes 클러스터를 띄운 뒤 Crossplane을 설치해본다.
2. AWS나 GCP Provider를 설치하고 간단한 Managed Resource(S3 버킷 등)를 하나 생성해본다.
3. Crossplane 공식 문서의 Composition 튜토리얼을 따라 커스텀 API를 하나 만들어본다.
4. Argo CD를 함께 설치해 Crossplane 리소스 정의를 GitOps 방식으로 배포하는 흐름을 연습해본다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane 프로젝트 개요와 시작 가이드를 확인할 수 있다.
- [Crossplane 공식 문서](https://docs.crossplane.io) — Provider 설치, Managed Resource, Composition 개념을 상세히 설명한다.
- [Terraform 공식 홈페이지](https://www.terraform.io) — 전통적인 IaC 도구인 Terraform과의 비교 맥락을 이해하는 데 도움이 된다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 도구로서 Crossplane과의 연계 방식을 참고할 수 있다.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Crossplane이 속한 클라우드 네이티브 생태계 전반의 프로젝트 현황을 확인할 수 있다.
