---
title: "2026-09-14 Crossplane으로 시작하는 Infrastructure as Code"
date: 2026-09-14T08:52:03.770036+09:00
tags: ["crossplane", "infrastructure-as-code", "kubernetes", "tech-brief"]
---
## 오늘의 기술 토픽

> **Infrastructure as Code with Crossplane**

이 브리프는 Crossplane을 중심으로 Kubernetes 네이티브 방식의 Infrastructure as Code 생태계를 정리한다. Crossplane은 클라우드 리소스를 Kubernetes CRD로 선언하고 관리할 수 있게 해주는 프로젝트로, Terraform과 달리 컨트롤 루프 기반으로 지속적인 리컨실리에이션을 수행한다는 점이 특징이다. 함께 알아두면 좋은 GitOps 도구인 Argo CD, 정책 관리를 담당하는 Kyverno, 시크릿 및 인증서 자동화를 돕는 cert-manager도 관련 생태계로 함께 소개한다. 플랫폼 엔지니어링 팀이 자체 서비스형 플랫폼을 구축할 때 이 조합이 표준적인 선택지로 자리잡고 있는 흐름을 짚는다.

## 🔑 핵심 요점

- Crossplane은 클라우드 인프라를 Kubernetes CRD와 컨트롤러로 관리하는 Infrastructure as Code 도구다.
- Terraform 같은 기존 IaC 도구는 실행 시점에만 상태를 적용하지만 Crossplane은 컨트롤 루프로 지속적으로 원하는 상태를 유지한다.
- Crossplane의 Composition 기능을 활용하면 여러 클라우드 리소스를 하나의 커스텀 API로 추상화해 개발자에게 제공할 수 있다.
- GitOps 도구인 Argo CD와 결합하면 인프라 변경도 Git 커밋을 통해 선언적으로 관리할 수 있다.
- Kyverno 같은 정책 엔진을 함께 사용하면 플랫폼 팀이 만든 리소스가 조직의 규칙을 준수하는지 자동으로 검증할 수 있다.
- cert-manager는 인증서 발급과 갱신을 자동화해 Crossplane으로 관리되는 인프라의 보안 운영 부담을 줄여준다.
- 이러한 조합은 개발자가 클라우드 전문 지식 없이도 셀프서비스로 인프라를 프로비저닝하는 플랫폼 엔지니어링 흐름을 뒷받침한다.

## 🛠 핵심 기술 쉽게 이해하기

### Crossplane

Crossplane은 Kubernetes 클러스터 위에서 동작하는 오픈소스 프로젝트로, AWS, GCP, Azure 같은 클라우드의 실제 리소스(DB, 네트워크, 스토리지 등)를 Kubernetes의 커스텀 리소스(CRD)로 정의하고 kubectl이나 GitOps 워크플로로 관리할 수 있게 해준다.

**왜 필요한가** — 여러 클라우드와 도구별로 흩어진 인프라 관리 방식을 Kubernetes API 하나로 통일하고, 개발자에게는 표준화된 셀프서비스 인터페이스를 제공하기 위해 사용한다.

**발표에서는** — Infrastructure as Code의 핵심 도구로 소개되며 Kubernetes 네이티브 방식의 인프라 관리 접근법을 대표하는 사례로 다뤄졌다.

### Argo CD

Argo CD는 Kubernetes를 위한 GitOps 지속적 배포 도구로, Git 저장소에 선언된 상태를 클러스터에 자동으로 동기화한다.

**왜 필요한가** — 인프라와 애플리케이션 변경 이력을 Git으로 추적하고, 수동 배포 실수를 줄이기 위해 사용한다.

**발표에서는** — Crossplane으로 정의한 인프라 리소스를 Git 기반으로 배포·관리하는 GitOps 파트너 도구로 함께 언급되었다.

### Kyverno

Kyverno는 Kubernetes 네이티브 정책 엔진으로, YAML로 정책을 작성해 클러스터에 생성되는 리소스를 검증하거나 자동 수정할 수 있다.

**왜 필요한가** — 플랫폼 팀이 만든 셀프서비스 인프라 리소스가 보안 및 컴플라이언스 규칙을 지키는지 자동으로 강제하기 위해 사용한다.

**발표에서는** — Crossplane 기반 플랫폼에서 리소스 생성 규칙을 강제하는 정책 계층으로 소개되었다.

### cert-manager

cert-manager는 Kubernetes 클러스터 내에서 TLS 인증서의 발급, 갱신, 관리를 자동화하는 컨트롤러다.

**왜 필요한가** — 수동으로 인증서를 관리하며 발생하는 만료 사고와 운영 부담을 줄이기 위해 사용한다.

**발표에서는** — Crossplane으로 프로비저닝된 인프라의 보안 운영을 자동화하는 보조 도구로 함께 다뤄졌다.

## 🧭 추구 방향과 흐름

- **플랫폼 엔지니어링과 셀프서비스** — 개발자가 클라우드 인프라 전문 지식 없이도 표준화된 API를 통해 필요한 리소스를 직접 프로비저닝할 수 있도록 하는 방향이다. Crossplane의 Composition을 통해 플랫폼 팀이 복잡한 인프라를 추상화된 커스텀 API로 제공하는 접근이 이를 뒷받침한다.
- **Kubernetes 중심의 통합 제어 평면** — 클라우드 리소스, 애플리케이션 배포, 정책, 보안까지 모두 Kubernetes API와 컨트롤 루프 패턴으로 일원화하는 흐름이다. Crossplane, Argo CD, Kyverno, cert-manager가 모두 Kubernetes CRD/컨트롤러 방식을 공유하는 점이 이를 보여준다.
- **선언적 인프라 관리와 지속적 리컨실리에이션** — 한 번 실행하고 끝나는 방식이 아니라 원하는 상태를 지속적으로 감시하고 자동 복구하는 방향으로 IaC가 진화하고 있다. Crossplane의 컨트롤 루프 기반 동작이 대표적인 예다.

## 🚀 바로 활용하기

1. 로컬 환경에 Kubernetes 클러스터(kind, minikube 등)를 띄우고 Crossplane 공식 Get Started 가이드를 따라 설치해본다.
2. 간단한 클라우드 Provider(AWS, GCP 등) 하나를 연결해 Crossplane으로 실제 리소스(예: 스토리지 버킷)를 하나 생성해본다.
3. Crossplane Composition 문서를 읽고 여러 리소스를 묶은 커스텀 API를 만들어본다.
4. Argo CD를 함께 설치해 Crossplane 리소스 정의를 Git 저장소 기반 GitOps 워크플로로 배포해본다.

## 🔗 참고 자료

- [Crossplane 공식 사이트](https://www.crossplane.io) — Crossplane의 개념, 설치, Composition 등 핵심 문서를 제공한다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 워크플로를 Crossplane과 함께 구성할 때 참고할 수 있다.
- [Kyverno 공식 사이트](https://kyverno.io) — Kubernetes 정책 엔진 개념과 정책 작성법을 확인할 수 있다.
- [cert-manager 공식 사이트](https://cert-manager.io) — 인증서 자동화 컨트롤러의 설치와 사용법을 설명한다.
- [CNCF 공식 사이트](https://www.cncf.io) — Crossplane을 비롯한 클라우드 네이티브 프로젝트들의 생태계 맥락을 확인할 수 있다.
