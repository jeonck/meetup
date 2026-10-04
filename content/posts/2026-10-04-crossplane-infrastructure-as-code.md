---
title: "2026-10-04 Crossplane로 시작하는 Infrastructure as Code"
date: 2026-10-04T09:20:41.232768+09:00
tags: ["crossplane", "infrastructure-as-code", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 주제는 Crossplane을 중심으로 한 Infrastructure as Code(IaC) 접근 방식을 다룬다. Kubernetes API를 확장해 클라우드 리소스까지 선언적으로 관리하는 방법과, 기존 Terraform 기반 IaC와의 차이점이 논의의 핵심이다. 플랫폼 엔지니어링 팀이 개발자에게 셀프서비스 인프라를 제공하기 위한 수단으로 Crossplane이 주목받고 있다는 맥락에서 소개되었다.

## 🔑 핵심 요점

- Crossplane은 Kubernetes API를 확장해 클라우드 리소스를 Kubernetes 오브젝트처럼 선언적으로 관리할 수 있게 해준다.
- 기존 Terraform 중심의 IaC와 달리 Crossplane은 클러스터 내에서 지속적으로 리소스 상태를 reconcile하는 컨트롤러 기반 모델을 사용한다.
- Crossplane의 Composition 기능을 통해 여러 클라우드 리소스를 하나의 커스텀 API로 묶어 개발자에게 셀프서비스 형태로 제공할 수 있다.
- GitOps 도구(Argo CD 등)와 Crossplane을 함께 쓰면 인프라 변경도 애플리케이션 배포와 동일한 파이프라인으로 관리할 수 있다.
- 플랫폼 팀은 Crossplane을 통해 개발자가 클라우드 콘솔이나 Terraform 코드를 직접 다루지 않고도 필요한 인프라를 요청할 수 있는 내부 플랫폼을 구축하려는 방향을 지향한다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes의 컨트롤 플레인을 확장해서 클라우드 프로바이더(AWS, GCP, Azure 등)의 리소스를 Kubernetes 커스텀 리소스(CRD)로 선언하고 관리할 수 있게 해주는 오픈소스 프레임워크이다. 즉, kubectl apply 한 번으로 VPC, 데이터베이스, 버킷 같은 실제 클라우드 자원을 만들고 지속적으로 원하는 상태로 유지시킬 수 있다.

**왜 필요한가** — 클라우드 인프라를 애플리케이션과 동일한 Kubernetes API와 워크플로우로 관리하여, 별도의 IaC 도구 없이도 일관된 선언적 관리와 자동 복구(reconciliation)를 가능하게 하기 위해 사용한다.

**발표에서는** — 오늘 주제의 중심 기술로, Infrastructure as Code를 Crossplane으로 구현하는 방식이 다뤄졌다.

### Terraform

Terraform은 HashiCorp에서 만든 대표적인 IaC 도구로, HCL이라는 선언형 언어로 클라우드 리소스를 정의하고 plan/apply 명령으로 리소스를 생성·변경한다.

**왜 필요한가** — 코드로 인프라를 버전 관리하고 재현 가능하게 구성하기 위한 가장 널리 쓰이는 표준 도구다.

**발표에서는** — Crossplane과 비교 대상으로 언급되며, Kubernetes 네이티브 방식과 기존 CLI 기반 IaC 방식의 차이를 설명하는 데 쓰였다.

### Argo CD

Argo CD는 Kubernetes용 GitOps 지속적 배포(CD) 도구로, Git 저장소에 선언된 상태를 클러스터에 자동으로 동기화해준다.

**왜 필요한가** — 애플리케이션뿐 아니라 Crossplane 리소스 같은 인프라 정의도 Git을 단일 진실 소스(Single Source of Truth)로 관리하기 위해 함께 사용된다.

**발표에서는** — Crossplane 리소스를 GitOps 방식으로 배포하는 조합의 예시로 언급되었다.

### Kubernetes

Kubernetes는 컨테이너화된 애플리케이션을 배포, 확장, 관리하기 위한 오픈소스 컨테이너 오케스트레이션 플랫폼이다.

**왜 필요한가** — Crossplane이 동작하는 기반 플랫폼으로, 커스텀 리소스와 컨트롤러 패턴을 제공해 클라우드 리소스 관리까지 확장할 수 있게 한다.

**발표에서는** — Crossplane의 동작 기반이 되는 플랫폼으로서 전제 지식으로 다뤄졌다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 셀프서비스 인프라** — Crossplane의 Composition 기능을 활용해 플랫폼 팀이 복잡한 클라우드 리소스 조합을 하나의 간단한 API로 추상화하고, 개발자는 이를 셀프서비스로 요청하는 방향이 강조되었다. 이는 개발자가 클라우드 전문 지식 없이도 필요한 인프라를 빠르게 확보할 수 있게 하는 내부 개발자 플랫폼(IDP) 트렌드와 맞닿아 있다.
- **GitOps 기반 인프라 관리로의 전환** — 인프라 변경도 애플리케이션 배포와 동일하게 Git을 통해 선언하고 Argo CD 같은 도구로 동기화하는 방식이 논의되었다. 이는 인프라와 애플리케이션 관리 파이프라인을 통합하려는 흐름을 보여준다.
- **Kubernetes API를 통한 도구 통합** — 클라우드 리소스 관리를 별도 CLI 도구가 아닌 Kubernetes API로 수렴시키는 경향이 언급되었으며, 이는 모니터링, 정책, 보안 도구들이 점점 Kubernetes 네이티브 방식으로 통합되는 생태계 전반의 흐름과 일치한다.

## 🚀 바로 활용하기

1. 로컬에 kind나 minikube로 테스트 클러스터를 만들고 Crossplane 공식 문서의 Get Started 가이드를 따라 설치해본다.
2. AWS/GCP/Azure 중 하나의 Provider를 설치하고 간단한 리소스(예: S3 버킷)를 선언해 kubectl apply로 생성해본다.
3. Composition을 작성해 여러 리소스를 하나의 커스텀 API로 묶어보는 실습을 진행한다.
4. Argo CD를 함께 설치해 Crossplane 리소스 정의를 GitOps 방식으로 동기화하는 흐름을 구성해본다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념, 설치 방법, Provider/Composition 문서의 출발점
- [Kubernetes 공식 문서](https://kubernetes.io) — Crossplane이 확장하는 기반 플랫폼인 Kubernetes API와 CRD 개념 이해에 필요
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — Crossplane 리소스를 GitOps로 동기화하는 조합을 실습할 때 참고
- [CNCF](https://www.cncf.io) — Crossplane과 관련 클라우드 네이티브 프로젝트들의 생태계와 졸업 현황 확인
