---
title: "2026-09-04 Crossplane으로 시작하는 Infrastructure as Code"
date: 2026-09-04T08:45:44.689777+09:00
tags: ["crossplane", "iac", "platform-engineering", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이번 브리프는 실제 밋업 발표 대신, Crossplane을 중심으로 한 Infrastructure as Code(IaC) 생태계를 정리한 기술 브리핑입니다. Crossplane은 Kubernetes API를 확장해 클라우드 리소스를 쿠버네티스 오브젝트처럼 선언적으로 관리할 수 있게 해주는 도구로, 플랫폼 엔지니어링과 self-service 인프라 제공의 핵심 축으로 떠오르고 있습니다. 함께 살펴볼 Terraform, Argo CD, Kyverno는 각각 IaC의 기존 표준, GitOps 배포, 정책 기반 거버넌스 측면에서 Crossplane과 맞물려 사용되는 도구들입니다.

## 🔑 핵심 요점

- Crossplane은 클라우드 리소스(예: AWS RDS, S3 등)를 Kubernetes Custom Resource로 표현하고 관리하는 오픈소스 프로젝트입니다.
- 기존 Terraform 같은 CLI 기반 IaC와 달리, Crossplane은 쿠버네티스 컨트롤러 패턴으로 지속적인 상태 조정(reconciliation)을 수행합니다.
- Composition 기능을 통해 플랫폼 팀이 애플리케이션 팀에게 단순화된 셀프서비스 API를 제공할 수 있습니다.
- GitOps 도구인 Argo CD와 결합하면 인프라 변경도 Git을 단일 진실 공급원(source of truth)으로 관리할 수 있습니다.
- Kyverno 같은 정책 엔진을 함께 쓰면 생성되는 클라우드 리소스에 조직의 보안/규정 정책을 강제할 수 있습니다.
- 플랫폼 엔지니어링(Platform Engineering) 트렌드에서 Crossplane은 '내부 개발자 플랫폼(IDP)'을 구축하는 핵심 빌딩 블록으로 주목받고 있습니다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes API를 확장해서 AWS, GCP, Azure 같은 클라우드 프로바이더의 리소스를 쿠버네티스 매니페스트(YAML)로 선언적으로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다. 즉, DB 인스턴스나 네트워크 같은 인프라도 쿠버네티스 오브젝트처럼 kubectl apply로 생성하고 관찰할 수 있습니다.

**왜 필요한가** — 여러 클라우드와 여러 도구로 흩어진 인프라 관리를 쿠버네티스라는 단일 컨트롤 플레인으로 통합하고, 팀에게 셀프서비스 인프라 API를 제공하기 위해 사용됩니다.

**발표에서는** — 이번 브리프의 중심 기술로 다뤄지며, IaC 접근 방식의 대표 사례로 소개됩니다.

### Terraform

Terraform은 HashiCorp가 만든 대표적인 IaC 도구로, HCL이라는 선언형 언어로 인프라를 정의하고 CLI 명령으로 클라우드 리소스를 생성/변경/삭제합니다.

**왜 필요한가** — 코드로 인프라를 관리해 재현성과 버전 관리를 확보하기 위한 IaC의 오랜 표준 도구입니다.

**발표에서는** — Crossplane과 비교 대상으로 언급되며, 쿠버네티스 네이티브 접근과 기존 CLI 기반 접근의 차이를 설명하는 데 쓰입니다.

### Argo CD

Argo CD는 Kubernetes용 GitOps 배포 도구로, Git 저장소에 정의된 상태를 클러스터의 실제 상태와 지속적으로 동기화합니다.

**왜 필요한가** — 애플리케이션뿐 아니라 Crossplane이 관리하는 인프라 리소스도 Git 기반으로 선언하고 배포 이력을 추적하기 위해 함께 사용됩니다.

**발표에서는** — Crossplane과 결합해 인프라까지 GitOps 워크플로에 포함시키는 방법으로 언급됩니다.

### Kyverno

Kyverno는 Kubernetes 네이티브 정책 엔진으로, YAML로 정책을 작성해 클러스터에 생성되는 리소스를 검증, 변형(mutate), 생성할 수 있습니다.

**왜 필요한가** — Crossplane으로 생성되는 클라우드 리소스에도 보안, 태깅, 비용 관리 같은 조직 정책을 강제하기 위해 사용됩니다.

**발표에서는** — Crossplane과 조합해 거버넌스를 강화하는 관련 기술로 소개됩니다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링(Platform as a Product)** — 인프라 관리를 개별 팀이 각자 하지 않고, 플랫폼 팀이 Crossplane Composition으로 표준화된 셀프서비스 API를 만들어 제공하는 방향입니다. 이는 애플리케이션 개발자가 인프라 세부사항을 몰라도 필요한 리소스를 빠르게 프로비저닝할 수 있게 합니다.
- **인프라의 GitOps화** — 애플리케이션 배포뿐 아니라 인프라 프로비저닝까지 Git을 단일 진실 공급원으로 삼아 Argo CD 같은 도구로 지속적으로 동기화하는 흐름입니다. 이는 인프라 변경의 감사 추적성과 롤백 용이성을 높입니다.
- **정책 기반 거버넌스(Policy as Code)** — 인프라 리소스 생성 시점에 Kyverno 같은 정책 엔진으로 보안/규정 준수를 자동 강제하는 방향입니다. 수동 리뷰 대신 코드화된 정책으로 일관성을 확보하려는 흐름입니다.

## 🚀 바로 활용하기

1. 로컬에 kind나 minikube로 클러스터를 띄우고 Crossplane 공식 Getting Started 가이드를 따라 첫 Provider와 Managed Resource를 설치해 보세요.
2. Crossplane Composition 예제를 따라 간단한 셀프서비스 API(예: 'Database' 커스텀 리소스)를 직접 정의해 보세요.
3. 이미 Terraform을 사용 중이라면 기존 리소스 일부를 Crossplane으로 마이그레이션해보며 두 접근 방식의 차이를 비교해 보세요.
4. Argo CD와 Crossplane을 함께 구성해 인프라 변경이 Git 커밋만으로 반영되는 흐름을 실습해 보세요.

## 🔗 참고 자료

- [Crossplane 공식 사이트](https://www.crossplane.io) — Crossplane의 개념, 아키텍처, 설치 방법을 확인할 수 있는 공식 문서 루트입니다.
- [Terraform 공식 사이트](https://www.terraform.io) — Crossplane과 비교되는 대표적인 CLI 기반 IaC 도구의 공식 문서입니다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — 인프라 GitOps 워크플로를 구성할 때 참고할 수 있는 공식 문서입니다.
- [Kyverno 공식 사이트](https://kyverno.io) — Crossplane 리소스에 정책을 적용하는 방법을 알아볼 수 있는 공식 사이트입니다.
- [CNCF](https://www.cncf.io) — Crossplane과 관련 도구들이 속한 클라우드 네이티브 생태계 전반을 살펴볼 수 있는 재단 사이트입니다.
