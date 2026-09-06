---
title: "2026-09-07 Platform Engineering 입문 가이드"
date: 2026-09-07T08:27:19.563127+09:00
tags: ["platform-engineering", "crossplane", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Platform Engineering**

Platform Engineering은 개발자가 인프라 복잡성에 신경 쓰지 않고 셀프서비스로 배포와 운영을 할 수 있도록 플랫폼 팀이 내부 개발자 플랫폼(IDP)을 제품처럼 만드는 접근 방식이다. Kubernetes 생태계가 성숙하면서 각 조직마다 반복적으로 구축하던 배포 파이프라인, 인프라 프로비저닝, 정책 관리 도구들을 표준화된 셀프서비스 플랫폼으로 통합하려는 흐름이 커지고 있다. Crossplane, Argo CD, Backstage 같은 도구들이 이 흐름의 핵심 구성 요소로 자리잡고 있다. 궁극적으로는 개발자 경험(DevEx)을 높이고 인지 부하를 줄이는 것이 목표다.

## 🔑 핵심 요점

- Platform Engineering은 인프라 팀이 개발자를 위한 '내부 제품'을 만드는 활동이다.
- 핵심 목표는 개발자의 인지 부하(cognitive load)를 줄이는 것이다.
- 셀프서비스 포털과 표준화된 골든 패스(golden path)가 대표적인 구현 방식이다.
- Crossplane 같은 도구로 인프라 프로비저닝을 API화하는 것이 많이 쓰인다.
- Argo CD 등 GitOps 도구와 결합해 배포 자동화를 완성한다.
- Backstage 같은 개발자 포털이 플랫폼의 진입점 역할을 한다.

## 🛠 핵심 기술 쉽게 이해하기

### Platform Engineering

Platform Engineering은 소프트웨어 개발팀이 셀프서비스로 인프라와 배포 도구를 사용할 수 있도록, 플랫폼 팀이 재사용 가능한 도구와 워크플로우를 '제품'처럼 설계하고 운영하는 분야다. 단순히 인프라를 관리하는 것을 넘어 개발자 경험(Developer Experience)을 최우선으로 고려한다.

**왜 필요한가** — 각 팀이 개별적으로 Kubernetes, CI/CD, 클라우드 리소스를 배우고 설정해야 하는 부담을 줄이고, 조직 전체의 생산성과 일관성을 높이기 위해 등장했다.

**발표에서는** — 오늘 주제로 다뤄진 핵심 개념으로, 개발자가 인프라 세부사항 대신 비즈니스 로직에 집중할 수 있게 하는 방향성이 소개됐다.

### Crossplane

Crossplane은 Kubernetes API를 확장해 클라우드 인프라(데이터베이스, 네트워크, 스토리지 등)를 Kubernetes 리소스처럼 선언적으로 관리할 수 있게 해주는 오픈소스 프로젝트다.

**왜 필요한가** — 개발자가 클라우드 콘솔이나 Terraform 문법을 몰라도 kubectl apply만으로 인프라를 요청할 수 있게 해, 셀프서비스 프로비저닝을 실현한다.

**발표에서는** — Platform Engineering의 핵심 구성 요소 중 하나로, 인프라를 API화하는 대표적인 도구로 언급되는 맥락에서 다뤄질 수 있는 기술이다.

### Argo CD

Argo CD는 Git 저장소에 선언된 상태를 기준으로 Kubernetes 클러스터에 애플리케이션을 자동 배포하고 동기화하는 GitOps 기반 배포 도구다.

**왜 필요한가** — 수동 배포로 인한 실수를 줄이고, Git을 단일 진실 공급원(single source of truth)으로 삼아 배포 이력을 추적 가능하게 만든다.

**발표에서는** — 플랫폼의 배포 파이프라인을 표준화하는 도구로, 셀프서비스 플랫폼 구축 시 자주 짝을 이루는 도구로 언급되는 맥락이다.

### Backstage

Backstage는 Spotify가 오픈소스로 공개한 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿을 한곳에서 제공한다.

**왜 필요한가** — 여러 팀에 흩어진 서비스와 도구 정보를 통합해, 개발자가 새 프로젝트를 시작하거나 기존 서비스를 찾을 때 겪는 혼란을 줄인다.

**발표에서는** — Platform Engineering 구현체의 대표 사례로, 셀프서비스 진입점 역할을 하는 도구로 함께 언급될 수 있는 맥락이다.

## 🧭 추구 방향과 흐름

- **Platform as a Product** — 플랫폼을 단순한 내부 인프라가 아니라 개발자를 고객으로 삼는 '제품'으로 취급하는 흐름이다. 사용자(개발자)의 피드백을 받아 지속적으로 개선하고, 문서화와 온보딩 경험을 제품 수준으로 관리하는 것이 핵심이다.
- **Self-Service Infrastructure** — 개발자가 티켓을 발행하지 않고도 필요한 인프라를 스스로 프로비저닝할 수 있게 하는 방향이다. Crossplane 같은 도구로 인프라를 Kubernetes API 수준에서 추상화하는 것이 이 흐름의 기술적 기반이다.
- **Golden Path 표준화** — 조직 내에서 검증된 배포 및 개발 방식을 '황금 경로(golden path)'로 정의해, 모든 팀이 매번 처음부터 아키텍처를 설계하지 않고 표준 템플릿을 따르게 하는 방향이다.

## 🚀 바로 활용하기

1. Team Topologies와 Platform Engineering 개념을 다룬 자료를 읽고 자신의 조직에 적용 가능한 부분을 파악해본다.
2. 로컬 Kubernetes 클러스터(minikube, kind 등)에 Crossplane을 설치해 간단한 리소스를 선언적으로 프로비저닝해본다.
3. Argo CD를 설치해 Git 저장소 기반 배포 파이프라인을 직접 구성해본다.
4. Backstage 데모 사이트나 공식 문서를 통해 개발자 포털이 제공하는 서비스 카탈로그 기능을 체험해본다.

## 🔗 참고 자료

- [CNCF Platforms White Paper](https://www.cncf.io) — CNCF가 정의한 Platform Engineering 및 플랫폼 성숙도 모델의 공식 출처다.
- [Crossplane 공식 문서](https://www.crossplane.io) — Kubernetes 기반 인프라 프로비저닝 도구인 Crossplane의 설치 및 사용법을 다룬다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 자동화 도구인 Argo CD의 개념과 설정 방법을 설명한다.
- [Kubernetes 공식 문서](https://kubernetes.io) — Platform Engineering의 기반이 되는 Kubernetes 개념을 익힐 수 있는 시작점이다.
