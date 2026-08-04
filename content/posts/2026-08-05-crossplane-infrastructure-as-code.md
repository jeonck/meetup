---
title: "2026-08-05 Crossplane로 시작하는 Infrastructure as Code"
date: 2026-08-05T08:00:12.176901+09:00
tags: ["crossplane", "infrastructure-as-code", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 브리프는 Kubernetes 위에서 클라우드 인프라를 선언적으로 관리하는 Crossplane을 중심으로 정리했다. Terraform과 달리 Crossplane은 클라우드 리소스를 Kubernetes API의 커스텀 리소스(CRD)로 다루어, 애플리케이션과 인프라를 동일한 API 서버와 GitOps 워크플로우로 관리할 수 있게 해준다. Argo CD 같은 GitOps 도구와 결합하면 인프라 변경도 Git 커밋 하나로 배포·감사할 수 있어, 플랫폼 엔지니어링 흐름과 자연스럽게 맞물린다. 초보자는 먼저 로컬 클러스터에서 Crossplane과 provider를 설치해보며 개념을 익히는 것이 좋다.

## 🔑 핵심 요점

- Crossplane은 클라우드 리소스(예: AWS RDS, S3)를 Kubernetes 커스텀 리소스로 선언하고 관리하는 오픈소스 프로젝트다.
- Terraform이 별도 상태 파일과 CLI로 인프라를 관리한다면, Crossplane은 Kubernetes API 서버 자체를 컨트롤 플레인으로 사용한다.
- Composition 기능을 이용하면 여러 클라우드 리소스를 조합해 팀이 사용할 자체 서비스 API(XRD)를 만들 수 있다.
- Argo CD와 결합하면 인프라 매니페스트도 애플리케이션 코드처럼 Git 기반으로 배포하고 추적할 수 있다.
- 플랫폼 팀이 개발자에게 셀프서비스 인프라 API를 제공하는 '플랫폼 엔지니어링' 흐름과 맞닿아 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes 클러스터 위에서 동작하는 오픈소스 컨트롤 플레인으로, AWS나 GCP 같은 클라우드 리소스를 Kubernetes 커스텀 리소스(CRD)처럼 선언적으로 정의하고 관리할 수 있게 해준다.

**왜 필요한가** — 여러 클라우드 provider의 리소스를 하나의 API와 워크플로우로 통합 관리하기 위해 사용한다.

**발표에서는** — Infrastructure as Code 도구로서 소개되며, Kubernetes 네이티브 방식으로 인프라를 관리하는 핵심 주제로 다뤄졌다.

### Terraform

Terraform은 HashiCorp이 만든 대표적인 IaC 도구로, HCL이라는 선언적 언어로 인프라를 코드로 작성하고 상태 파일을 통해 변경 사항을 추적한다.

**왜 필요한가** — 수동으로 클라우드 콘솔에서 리소스를 만드는 대신, 코드로 재현 가능하고 버전 관리되는 인프라를 구성하기 위해 쓴다.

**발표에서는** — Crossplane과 비교 대상으로 언급되며, 두 도구의 접근 방식 차이를 이해하는 데 참고가 되었다.

### Argo CD

Argo CD는 Kubernetes를 위한 GitOps 도구로, Git 저장소에 있는 매니페스트 상태를 클러스터에 자동으로 동기화해준다.

**왜 필요한가** — 배포 과정을 Git 커밋 기반으로 표준화하고, 변경 이력을 투명하게 관리하기 위해 사용한다.

**발표에서는** — Crossplane 리소스를 GitOps 방식으로 배포·관리하는 조합 사례로 언급되었다.

### Kubernetes

Kubernetes는 컨테이너화된 애플리케이션을 배포, 확장, 운영하기 위한 오픈소스 오케스트레이션 플랫폼이다.

**왜 필요한가** — Crossplane이 동작하는 기반 플랫폼이자, CRD와 컨트롤러 패턴을 통해 확장 가능한 API를 제공하기 위해 필요하다.

**발표에서는** — Crossplane이 클라우드 리소스 관리를 위해 확장하는 기반 플랫폼으로 설명되었다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 셀프서비스 인프라** — Crossplane의 Composition 기능으로 플랫폼 팀이 애플리케이션 팀에게 표준화된 인프라 API를 제공할 수 있다는 방향이 강조되었다. 개발자는 복잡한 클라우드 설정을 몰라도 팀 내부의 커스텀 리소스만 요청하면 되는 셀프서비스 모델로 나아가고 있다.
- **GitOps로의 인프라 관리 통합** — 인프라 변경도 애플리케이션 배포와 동일하게 Git 저장소를 단일 진실 공급원(source of truth)으로 삼아 Argo CD 같은 도구로 동기화하는 흐름이 방향으로 제시되었다.
- **Kubernetes API를 인프라 관리의 표준 인터페이스로** — 클라우드 provider마다 다른 API 대신, Kubernetes CRD라는 하나의 일관된 인터페이스로 인프라를 다루는 것이 생태계가 향하는 지점으로 다뤄졌다.

## 🚀 바로 활용하기

1. 로컬 kind 또는 minikube 클러스터에 Crossplane을 설치하고 공식 Getting Started 가이드를 따라 provider-aws나 provider-gcp를 연동해본다.
2. 간단한 Composition(XRD)을 작성해 하나의 커스텀 리소스로 여러 클라우드 리소스를 함께 프로비저닝해본다.
3. Argo CD를 함께 설치해 Crossplane 리소스 매니페스트를 GitOps 방식으로 배포하는 흐름을 실습해본다.
4. 기존에 Terraform을 써봤다면 동일한 리소스를 Crossplane으로 재작성하며 두 도구의 차이를 비교해본다.

## 🔗 참고 자료

- [Crossplane 공식 사이트](https://www.crossplane.io) — Crossplane 개념, 설치, Composition 문서의 시작점
- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 컨트롤러 패턴 등 Crossplane이 기반하는 개념 설명
- [Argo CD 문서](https://argo-cd.readthedocs.io) — GitOps로 Crossplane 리소스를 배포하는 방법을 익히는 데 참고
- [Terraform 공식 사이트](https://www.terraform.io) — Crossplane과 비교되는 전통적 IaC 도구의 문서
- [CNCF](https://www.cncf.io) — Crossplane이 속한 클라우드 네이티브 생태계와 프로젝트 현황 확인
