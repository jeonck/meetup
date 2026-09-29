---
title: "2026-09-29 Internal Developer Platform(IDP) 한눈에 보기"
date: 2026-09-29T10:26:53.405454+09:00
tags: ["idp", "platform-engineering", "backstage", "tech-brief"]
---
## 오늘의 기술 토픽

> **Internal Developer Platform (IDP)**

Internal Developer Platform(IDP)은 개발자가 인프라 세부사항을 몰라도 셀프서비스로 애플리케이션을 배포하고 운영할 수 있도록 조직 내부에 구축하는 플랫폼을 의미한다. Kubernetes와 클라우드 인프라가 복잡해지면서 플랫폼 엔지니어링 팀이 생겨났고, 이들은 IDP를 통해 반복적인 인프라 요청을 셀프서비스 포털과 템플릿으로 대체한다. 이 브리핑에서는 IDP의 개념과 함께 이를 구현하는 데 자주 쓰이는 Backstage, Crossplane, GitOps 도구들을 함께 살펴본다.

## 🔑 핵심 요점

- IDP는 개발자와 인프라 사이의 '셀프서비스 계층'으로, 반복적인 인프라 티켓 작업을 줄이는 것이 목표다.
- 플랫폼 엔지니어링 팀은 IDP를 하나의 내부 제품처럼 취급하고, 개발자를 그 제품의 사용자(고객)로 본다.
- Backstage 같은 개발자 포털과 Crossplane 같은 인프라 추상화 도구가 IDP 구현의 대표적인 조합이다.
- 골든 패스(golden path)는 조직이 권장하는 표준 배포/개발 경로로, IDP의 핵심 산출물 중 하나다.
- GitOps는 IDP에서 인프라와 애플리케이션 상태를 선언적으로 관리하는 기반 원칙으로 자주 함께 사용된다.
- IDP 도입은 도구 하나를 설치하는 문제가 아니라 조직의 워크플로와 팀 구조 변화까지 포함하는 작업이다.

## 🛠 핵심 기술 쉽게 이해하기

### Internal Developer Platform (IDP)

IDP는 개발자가 인프라, CI/CD, 관측 도구 등을 직접 다루지 않고도 셀프서비스로 애플리케이션을 배포·운영할 수 있게 해주는 내부 플랫폼이다. 보통 포털 UI, API, 템플릿, 자동화 파이프라인으로 구성된다.

**왜 필요한가** — 조직이 커질수록 인프라 요청이 늘어나 인프라팀이 병목이 되는데, IDP는 이런 반복 작업을 표준화·자동화해서 병목을 줄인다.

**발표에서는** — 이번 브리핑에서는 IDP를 플랫폼 엔지니어링의 핵심 산출물로 소개하며, 이를 실제로 구성하는 대표 도구들을 함께 정리했다.

### Backstage

Backstage는 Spotify가 만들고 CNCF에 기부한 오픈소스 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿을 한 곳에서 관리할 수 있게 해준다.

**왜 필요한가** — 여러 팀이 흩어져 만든 서비스와 문서를 한 곳에 모아 검색 가능하게 만들고, 새 서비스 생성을 템플릿화해 온보딩 속도를 높인다.

**발표에서는** — IDP의 '프론트엔드' 역할을 하는 대표 사례로 소개되었으며, 셀프서비스 포털을 구현할 때 가장 많이 언급되는 도구로 다뤄졌다.

### Crossplane

Crossplane은 Kubernetes API를 확장해 클라우드 리소스(DB, 네트워크, 스토리지 등)를 Kubernetes 오브젝트처럼 선언적으로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트다.

**왜 필요한가** — 개발자가 클라우드 콘솔이나 Terraform 문법을 몰라도, 쿠버네티스 매니페스트 형태로 인프라를 요청하고 프로비저닝할 수 있게 해준다.

**발표에서는** — IDP의 '인프라 추상화 계층'을 구현하는 도구로 언급되었으며, 개발자용 커스텀 API(Composite Resource)를 만드는 방식이 소개되었다.

### GitOps (Argo CD)

GitOps는 Git 저장소를 단일 진실 공급원(source of truth)으로 삼아 인프라와 애플리케이션 상태를 선언적으로 관리하는 운영 방식이며, Argo CD는 이를 Kubernetes 환경에서 구현하는 대표적인 도구다.

**왜 필요한가** — 수동 배포로 인한 설정 드리프트와 실수를 줄이고, 변경 이력을 Git으로 추적할 수 있게 한다.

**발표에서는** — IDP에서 배포 파이프라인을 표준화하는 기반 원칙으로 다뤄졌으며, 셀프서비스 배포 흐름의 마지막 단계로 연결되는 도구로 언급되었다.

## 🧭 추구 방향과 흐름

- **Platform as a Product** — 플랫폼 엔지니어링 팀이 IDP를 내부 '제품'으로 취급하고 개발자를 고객처럼 대하는 방향으로 가고 있다. 이는 포털 UX, 문서화, 피드백 루프를 제품 수준으로 신경 쓴다는 의미다.
- **셀프서비스와 골든 패스** — 개발자가 인프라팀에 티켓을 올리는 대신 표준화된 템플릿(golden path)을 통해 스스로 서비스를 만들고 배포하는 방향으로 나아가고 있다. Backstage 템플릿과 Crossplane Composition이 이런 흐름의 실제 구현 수단으로 쓰인다.
- **선언적 인프라와 GitOps 확산** — 인프라 프로비저닝까지 Kubernetes 선언적 API와 GitOps 워크플로로 통합하려는 흐름이 강해지고 있으며, Crossplane과 Argo CD의 조합이 그 대표적인 예시다.

## 🚀 바로 활용하기

1. 로컬 환경에 Backstage를 설치(npx @backstage/create-app)해보고 기본 서비스 카탈로그를 구성해본다.
2. Crossplane 공식 문서의 Getting Started를 따라 간단한 클라우드 리소스(Composite Resource)를 정의하고 프로비저닝해본다.
3. Argo CD를 로컬 Kubernetes 클러스터(minikube/kind)에 설치해 GitOps 배포 흐름을 직접 체험해본다.
4. CNCF의 Platform Engineering 관련 자료를 읽고 자신의 조직에 맞는 골든 패스를 스케치해본다.

## 🔗 참고 자료

- [Backstage 공식 사이트](https://backstage.io) — IDP의 프론트엔드 역할을 하는 개발자 포털 프레임워크 공식 문서
- [Crossplane 공식 사이트](https://www.crossplane.io) — Kubernetes 기반 인프라 추상화 도구의 공식 홈페이지
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 도구의 공식 문서 루트
- [Kubernetes 공식 사이트](https://kubernetes.io) — IDP와 관련 도구들이 공통으로 기반하는 오케스트레이션 플랫폼 공식 문서
- [CNCF 공식 사이트](https://www.cncf.io) — Backstage, Crossplane, Argo CD 등이 속한 클라우드 네이티브 생태계 관리 재단
