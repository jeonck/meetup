---
title: "2026-08-30 Internal Developer Platform(IDP) 입문 가이드"
date: 2026-08-30T08:51:49.418005+09:00
tags: ["idp", "platform-engineering", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Internal Developer Platform (IDP)**

이번 자료는 실제 밋업 발표가 아니라, 최근 플랫폼 엔지니어링 커뮤니티에서 화두가 되고 있는 Internal Developer Platform(IDP)을 중심으로 정리한 기술 브리프이다. IDP는 개발자가 인프라 지식 없이도 셀프서비스로 애플리케이션을 배포하고 운영할 수 있도록 돕는 플랫폼으로, Backstage, Crossplane, Argo CD 같은 도구들과 함께 조합되어 구축되는 경우가 많다. 이 문서는 IDP와 밀접한 주변 기술들을 함께 소개하고, 처음 학습을 시작하는 사람이 어떤 순서로 접근하면 좋을지 안내한다.

## 🔑 핵심 요점

- IDP는 개발자 셀프서비스를 목표로 인프라 복잡성을 플랫폼 뒤로 감추는 접근 방식이다.
- Backstage 같은 개발자 포털은 IDP의 UI/카탈로그 계층 역할을 한다.
- Crossplane은 클라우드 리소스를 Kubernetes API 형태로 추상화해 IDP의 인프라 프로비저닝 계층으로 자주 쓰인다.
- Argo CD 같은 GitOps 도구는 IDP에서 배포 자동화와 상태 동기화를 담당한다.
- 플랫폼 엔지니어링은 '플랫폼을 하나의 제품처럼 취급한다'는 사고방식(Platform as a Product)을 강조한다.
- IDP 도입은 도구 하나를 설치하는 문제가 아니라 조직의 워크플로우를 재설계하는 작업이다.

## 🛠 핵심 기술 쉽게 이해하기

### Internal Developer Platform (IDP)

IDP는 회사 내부 개발자들이 인프라 세부사항을 몰라도 애플리케이션을 배포, 모니터링, 운영할 수 있도록 만든 셀프서비스 플랫폼이다. 개발자는 미리 정의된 템플릿이나 UI를 통해 필요한 리소스를 요청하고, 플랫폼이 뒤에서 실제 프로비저닝과 설정을 처리한다.

**왜 필요한가** — 인프라팀에 매번 티켓을 넣고 기다리는 병목을 없애고, 개발자가 빠르게 셀프서비스로 작업할 수 있게 하기 위해 사용한다.

**발표에서는** — 이번 브리프의 중심 주제로, IDP가 왜 필요한지와 어떤 구성 요소들로 이루어지는지를 소개하는 출발점으로 다뤄진다.

### Backstage

Spotify가 만들고 CNCF에 기증한 오픈소스 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿을 한 곳에서 관리할 수 있게 해준다.

**왜 필요한가** — 여러 팀이 흩어져 관리하던 서비스 정보와 배포 템플릿을 하나의 포털로 통합해 개발자 경험을 개선하기 위해 쓰인다.

**발표에서는** — IDP를 구축할 때 프론트엔드/카탈로그 계층으로 가장 널리 채택되는 도구로 언급된다.

### Crossplane

Kubernetes API를 확장해서 클라우드 인프라(DB, 네트워크, 스토리지 등)를 Kubernetes 리소스처럼 선언적으로 관리할 수 있게 해주는 오픈소스 프로젝트다.

**왜 필요한가** — 여러 클라우드 provider의 리소스를 하나의 일관된 API로 다루면서, IDP에서 셀프서비스로 인프라를 프로비저닝하는 기반으로 쓰기 위해 사용한다.

**발표에서는** — IDP의 인프라 프로비저닝 계층을 구성하는 대표적인 관련 기술로 소개된다.

### Argo CD

Kubernetes를 위한 GitOps 지속적 배포 도구로, Git 저장소에 선언된 상태와 클러스터의 실제 상태를 지속적으로 동기화한다.

**왜 필요한가** — 수동 배포로 인한 실수를 줄이고, Git을 단일 진실 공급원(source of truth)으로 삼아 배포를 자동화하기 위해 사용한다.

**발표에서는** — IDP에서 배포 자동화 계층을 담당하는 도구로 함께 언급된다.

## 🧭 추구 방향과 흐름

- **Platform as a Product** — 플랫폼팀이 인프라를 단순 관리 대상이 아니라 내부 고객(개발자)을 위한 제품으로 취급하는 방향이다. 이는 IDP가 UI/UX, 문서화, 온보딩 경험까지 신경 써야 한다는 점을 강조한다.
- **셀프서비스와 개발자 경험(DevEx) 강화** — 개발자가 인프라팀을 거치지 않고도 필요한 리소스를 스스로 요청하고 받을 수 있게 하는 흐름이다. Backstage 같은 포털과 Crossplane 같은 추상화 계층이 이 방향을 뒷받침한다.
- **GitOps 기반 표준화** — 배포와 인프라 변경을 모두 Git을 통해 선언적으로 관리하는 흐름으로, Argo CD 같은 도구가 IDP 안에서 배포 자동화의 표준 방식으로 자리잡고 있다.

## 🚀 바로 활용하기

1. Backstage 공식 문서의 Getting Started 가이드를 따라 로컬에 개발자 포털을 하나 띄워본다.
2. Crossplane 공식 문서에서 Provider 개념과 Composition을 학습하고, 간단한 클라우드 리소스(S3 버킷 등)를 선언적으로 만들어본다.
3. Argo CD를 로컬 Kubernetes 클러스터(minikube 등)에 설치하고, Git 저장소와 동기화되는 간단한 애플리케이션을 배포해본다.
4. CNCF의 Platform Engineering 관련 자료를 읽고 자신의 조직에 맞는 IDP 구성요소를 구상해본다.

## 🔗 참고 자료

- [CNCF (Cloud Native Computing Foundation)](https://www.cncf.io) — IDP와 플랫폼 엔지니어링 관련 프로젝트들을 아우르는 상위 재단 사이트
- [Backstage 공식 사이트](https://backstage.io) — 개발자 포털 프레임워크 Backstage의 문서와 시작 가이드
- [Crossplane 공식 사이트](https://www.crossplane.io) — Kubernetes 기반 인프라 프로비저닝 도구 Crossplane의 공식 문서
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 도구 Argo CD의 설치 및 사용법 문서
