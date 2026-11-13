---
title: "2026-11-13 Crossplane로 시작하는 Infrastructure as Code"
date: 2026-11-13T11:21:32.693889+09:00
tags: ["crossplane", "infrastructure-as-code", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 밋업은 Crossplane을 중심으로 쿠버네티스 네이티브 방식의 Infrastructure as Code를 다뤘다. 클라우드 리소스를 쿠버네티스 커스텀 리소스로 선언하고 컨트롤러가 이를 조정(reconcile)하는 방식이 핵심 주제로 소개됐다. 전통적인 Terraform 기반 IaC와 비교해 GitOps, 플랫폼 엔지니어링 관점에서 어떤 장점이 있는지도 함께 논의됐다. 발표 분량이 짧아 세부 데모나 Q&A보다는 개념과 생태계 소개 위주로 진행됐다.

## 🔑 핵심 요점

- Crossplane은 클라우드 인프라를 쿠버네티스 커스텀 리소스(CRD)로 선언하고 컨트롤러가 지속적으로 실제 상태를 원하는 상태로 맞춰주는 Infrastructure as Code 도구다.
- Terraform처럼 apply 한 번으로 끝나는 방식이 아니라, 쿠버네티스 컨트롤러 패턴으로 상태를 계속 감시하고 드리프트를 교정하는 방식이 핵심 차이다.
- Provider라는 플러그인을 통해 AWS, GCP, Azure 등 다양한 클라우드 리소스를 동일한 쿠버네티스 API로 다룰 수 있다.
- Composition 기능으로 여러 리소스를 묶어 팀이 재사용할 수 있는 '커스텀 플랫폼 API'를 만들 수 있다는 점이 플랫폼 엔지니어링 트렌드와 맞물려 소개됐다.
- GitOps 도구(Argo CD 등)와 자연스럽게 연계되어 애플리케이션과 인프라를 같은 파이프라인에서 관리할 수 있다는 점이 강조됐다.
- 쿠버네티스에 익숙한 개발자/운영자에게는 별도의 IaC 언어를 새로 배우지 않고도 YAML/CRD 방식으로 인프라를 관리할 수 있다는 진입장벽 완화 효과가 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 클라우드 프로바이더(AWS, GCP, Azure 등)의 리소스를 쿠버네티스 커스텀 리소스(CRD)로 표현하고, 컨트롤러가 이를 지속적으로 관찰하며 원하는 상태로 유지해주는 오픈소스 프레임워크다. 쿠버네티스 API 서버를 확장해 '인프라도 쿠버네티스 오브젝트처럼' 다룰 수 있게 해준다.

**왜 필요한가** — Terraform 같은 별도 도구나 상태 파일 없이, 이미 익숙한 쿠버네티스 선언적 방식과 GitOps 워크플로우 안에서 클라우드 인프라를 관리하기 위해 사용한다.

**발표에서는** — 이번 밋업의 주제로서 Infrastructure as Code를 쿠버네티스 네이티브 방식으로 구현하는 핵심 도구로 소개됐다.

### Terraform

Terraform은 HCL이라는 자체 언어로 클라우드 인프라를 선언하고 상태 파일(state file)을 기반으로 변경 사항을 계산해 적용하는 대표적인 IaC 도구다.

**왜 필요한가** — 멀티 클라우드 환경에서 인프라를 코드로 관리하고 재현 가능하게 만들기 위해 널리 쓰인다.

**발표에서는** — Crossplane과 대비되는 전통적 IaC 방식으로 비교 대상으로 언급됐다.

### Argo CD

Argo CD는 Git 저장소에 선언된 상태를 쿠버네티스 클러스터에 자동으로 동기화해주는 GitOps 전용 배포 도구다.

**왜 필요한가** — 애플리케이션 배포를 Git을 기준으로 자동화하고, 클러스터 상태와 Git의 불일치를 지속적으로 감지·교정하기 위해 사용한다.

**발표에서는** — Crossplane과 함께 사용하면 애플리케이션과 인프라를 동일한 GitOps 파이프라인으로 관리할 수 있다는 연계 포인트로 언급됐다.

### Kubernetes Custom Resource Definitions (CRD)

CRD는 쿠버네티스 API를 확장해 사용자가 정의한 새로운 리소스 타입을 쿠버네티스가 네이티브 오브젝트처럼 다룰 수 있게 해주는 메커니즘이다.

**왜 필요한가** — 쿠버네티스 생태계의 도구(kubectl, RBAC, 컨트롤러 등)를 그대로 활용하면서 도메인 특화 리소스를 모델링하기 위해 쓰인다.

**발표에서는** — Crossplane이 클라우드 리소스를 표현하는 기반 기술로 설명됐다.

## 🧭 추구 방향과 흐름

- **쿠버네티스 네이티브 IaC** — 인프라 관리를 별도의 도구와 언어가 아니라 쿠버네티스 API와 컨트롤러 패턴 안으로 통합하려는 방향이 중심 흐름으로 제시됐다. 이는 운영자와 개발자가 하나의 플랫폼에서 애플리케이션과 인프라를 함께 다룰 수 있게 한다.
- **플랫폼 엔지니어링과 Platform as a Product** — Crossplane의 Composition 기능을 활용해 플랫폼 팀이 복잡한 인프라를 추상화된 '셀프서비스 API'로 제공하는 방향이 강조됐다. 개발자는 복잡한 클라우드 세부사항을 몰라도 표준화된 커스텀 리소스를 요청하는 것만으로 인프라를 프로비저닝할 수 있다.
- **GitOps 기반 통합 운영** — 인프라와 애플리케이션 배포를 하나의 Git 기반 파이프라인으로 통합하려는 흐름이 Argo CD와의 연계를 통해 제시됐다. 선언적 상태와 지속적 조정(reconciliation)이라는 공통 패턴이 전체 스택에 적용되는 방향이다.

## 🚀 바로 활용하기

1. 로컬 환경(kind, minikube 등)에 쿠버네티스 클러스터를 만들고 Crossplane을 설치해본다.
2. Crossplane 공식 문서의 Getting Started 가이드를 따라 AWS/GCP 중 하나의 Provider를 설치하고 간단한 리소스(S3 버킷 등)를 선언해 생성해본다.
3. Composition 개념을 익히기 위해 공식 문서의 예제를 따라 여러 리소스를 묶은 커스텀 API를 하나 만들어본다.
4. 이미 GitOps를 쓰고 있다면 Argo CD와 Crossplane을 연동해 인프라 변경을 Git 커밋으로 관리하는 흐름을 실습해본다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념, Provider, Composition 등 핵심 구조를 확인할 수 있는 공식 사이트.
- [Crossplane 공식 문서](https://docs.crossplane.io) — 설치 방법과 Getting Started, Composition 가이드를 포함한 공식 문서.
- [Kubernetes 공식 홈페이지](https://kubernetes.io) — CRD와 컨트롤러 패턴 등 Crossplane이 기반으로 하는 쿠버네티스 핵심 개념 문서.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — Crossplane과 연계되는 GitOps 배포 도구의 공식 문서.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Crossplane이 속한 클라우드 네이티브 생태계와 관련 프로젝트 현황을 확인할 수 있는 사이트.
