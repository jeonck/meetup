---
title: "2026-11-03 Crossplane로 시작하는 Infrastructure as Code"
date: 2026-11-03T12:16:54.032280+09:00
tags: ["crossplane", "infrastructure-as-code", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

Crossplane은 Kubernetes API를 확장해 클라우드 리소스를 쿠버네티스 오브젝트처럼 선언적으로 관리할 수 있게 해주는 오픈소스 프로젝트다. 기존 Terraform 중심의 IaC 워크플로우와 달리, 상태 관리와 리소스 프로비저닝을 쿠버네티스 컨트롤러 패턴으로 통합한다는 점이 특징이다. 이 브리핑은 Crossplane이 어떤 문제를 풀기 위해 등장했는지, 그리고 GitOps·플랫폼 엔지니어링 흐름과 어떻게 맞물리는지를 정리한다. 관련 기술로 Terraform, Argo CD, 쿠버네티스 Operator 패턴을 함께 다룬다.

## 🔑 핵심 요점

- Crossplane은 클라우드 리소스(DB, VPC, 버킷 등)를 쿠버네티스 커스텀 리소스(CRD)로 선언하고 관리하게 해준다.
- Terraform이 별도의 state 파일과 CLI 실행에 의존하는 반면, Crossplane은 쿠버네티스 컨트롤러가 지속적으로 원하는 상태(desired state)를 수렴시킨다.
- Composition 기능을 통해 여러 저수준 리소스를 묶어 하나의 '플랫폼 API'로 추상화할 수 있다.
- Argo CD 같은 GitOps 도구와 결합하면 애플리케이션과 인프라를 동일한 Git 기반 워크플로우로 관리할 수 있다.
- 이런 접근은 플랫폼 엔지니어링(Internal Developer Platform) 트렌드, 즉 개발자에게 self-service 인프라를 제공하려는 흐름과 맞닿아 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 쿠버네티스 API를 확장해 AWS, GCP, Azure 같은 클라우드 제공자의 리소스를 쿠버네티스 커스텀 리소스(CRD)로 정의하고 관리할 수 있게 해주는 오픈소스 프레임워크다. Provider라는 플러그인을 통해 실제 클라우드 API와 통신하며, 쿠버네티스 컨트롤러 패턴으로 리소스 상태를 지속적으로 맞춰준다.

**왜 필요한가** — 클라우드 인프라 관리를 애플리케이션 배포와 동일한 쿠버네티스 선언적 방식으로 통합하고, 플랫폼 팀이 자체 API를 만들어 개발자에게 제공할 수 있게 하기 위해 사용한다.

**발표에서는** — 이번 브리핑의 중심 주제로, 쿠버네티스 네이티브 방식의 IaC가 어떻게 동작하는지 기본 개념 위주로 다룬다.

### Terraform

Terraform은 HCL이라는 선언적 언어로 인프라를 코드로 작성하고, plan/apply 사이클을 통해 클라우드 리소스를 생성·변경·삭제하는 대표적인 IaC 도구다.

**왜 필요한가** — 수동으로 콘솔에서 리소스를 만드는 대신 코드로 재현 가능하고 버전 관리 가능한 인프라를 구성하기 위해 쓰인다.

**발표에서는** — Crossplane과 비교 대상으로 언급되며, CLI 기반 실행 모델과 쿠버네티스 컨트롤러 기반 모델의 차이를 설명하는 데 활용된다.

### Argo CD

Argo CD는 Git 리포지토리에 선언된 상태를 쿠버네티스 클러스터에 자동으로 동기화하는 GitOps 전용 CD 도구다.

**왜 필요한가** — 배포 이력을 Git으로 추적하고, 클러스터의 실제 상태와 원하는 상태의 드리프트를 자동으로 감지·교정하기 위해 사용한다.

**발표에서는** — Crossplane으로 정의한 인프라 리소스를 Git 기반으로 함께 관리하는 조합 사례로 언급된다.

### Kubernetes Operator Pattern

Operator 패턴은 쿠버네티스 커스텀 컨트롤러가 특정 도메인의 리소스를 지속적으로 감시하며 원하는 상태로 수렴시키는 설계 방식이다.

**왜 필요한가** — 애플리케이션이나 인프라의 운영 지식을 코드로 자동화해 사람의 수동 개입을 줄이기 위해 쓰인다.

**발표에서는** — Crossplane이 내부적으로 의존하는 기반 원리로, 왜 Crossplane 리소스가 '선언 후 자동 수렴'하는지를 설명하는 맥락에서 다뤄진다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링(Internal Developer Platform)** — Crossplane의 Composition 기능은 저수준 클라우드 리소스를 조합해 팀 내부용 '플랫폼 API'를 만드는 데 초점을 둔다. 이는 개발자가 인프라 세부사항을 몰라도 self-service로 필요한 리소스를 받을 수 있게 하려는 플랫폼 엔지니어링 트렌드와 일치한다.
- **GitOps로의 통합** — 인프라 정의를 쿠버네티스 매니페스트 형태로 관리할 수 있게 되면서, Argo CD 같은 GitOps 도구와 자연스럽게 결합할 수 있다. 애플리케이션과 인프라를 하나의 Git 기반 파이프라인으로 다루는 방향으로 이어진다.
- **선언적 상태 수렴 모델 확산** — Terraform의 명령형 실행(plan/apply) 방식과 달리, Crossplane은 쿠버네티스 컨트롤러 루프를 통해 지속적으로 상태를 맞춘다. 이런 '컨트롤 루프' 방식이 인프라 관리 전반으로 확산되는 흐름이 나타난다.

## 🚀 바로 활용하기

1. 로컬 환경(kind 또는 minikube)에 쿠버네티스 클러스터를 띄우고 Helm으로 Crossplane을 설치해본다.
2. 원하는 클라우드용 Provider(예: provider-aws, provider-gcp)를 설치하고 간단한 리소스(S3 버킷 등) 하나를 CRD로 선언해 생성해본다.
3. Composition 예제를 따라 여러 리소스를 묶어 하나의 커스텀 API로 추상화해본다.
4. Argo CD 공식 문서를 참고해 Crossplane 리소스를 Git 리포지토리 기반으로 동기화하는 흐름을 구성해본다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 핵심 개념(Provider, Composition 등)과 설치 가이드를 확인할 수 있다.
- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 컨트롤러 패턴 등 Crossplane이 기반하는 쿠버네티스 개념을 이해하는 데 필요하다.
- [Terraform 공식 홈페이지](https://www.terraform.io) — Crossplane과 비교되는 전통적 IaC 도구의 동작 방식을 확인할 수 있다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — Crossplane 리소스를 GitOps 방식으로 동기화하는 방법을 다룬다.
- [CNCF](https://www.cncf.io) — Crossplane과 Argo CD를 포함한 클라우드 네이티브 프로젝트들의 생태계와 트렌드를 확인할 수 있다.
