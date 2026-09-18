---
title: "2026-09-19 Internal Developer Platform(IDP)으로 시작하는 플랫폼 엔지니어링"
date: 2026-09-19T08:51:14.778800+09:00
tags: ["platform-engineering", "idp", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Internal Developer Platform (IDP)**

이번 자료는 별도의 밋업 발표 없이 Internal Developer Platform(IDP)이라는 주제를 중심으로 정리한 브리프다. IDP는 개발자가 인프라 세부사항을 몰라도 셀프서비스로 애플리케이션을 배포하고 운영할 수 있도록 만든 내부 플랫폼을 의미한다. Crossplane, Argo CD, Kyverno 같은 도구들이 조합되어 이런 플랫폼을 구성하는 대표적인 구성요소로 다뤄진다. 실제 발표나 청중 질의응답은 없었으므로, 개념 이해와 학습 시작점을 제공하는 데 초점을 맞췄다.

## 🔑 핵심 요점

- Internal Developer Platform(IDP)은 개발자에게 셀프서비스 방식으로 인프라 및 배포 기능을 제공하는 내부 플랫폼이다.
- IDP의 목표는 개발자가 Kubernetes나 클라우드 인프라의 복잡한 세부사항을 몰라도 애플리케이션을 배포할 수 있게 하는 것이다.
- Crossplane 같은 도구는 인프라를 Kubernetes API 형태로 추상화해 IDP의 기반이 될 수 있다.
- Argo CD는 GitOps 방식으로 배포를 자동화해 IDP의 배포 파이프라인 역할을 한다.
- Kyverno는 정책 기반으로 플랫폼 사용 규칙을 강제해 셀프서비스 환경에서도 안전성을 보장한다.
- 플랫폼 엔지니어링은 '플랫폼을 제품처럼 다룬다'는 관점에서 IDP를 지속적으로 개선하는 문화적 접근을 포함한다.

## 🛠 핵심 기술 쉽게 이해하기

### Internal Developer Platform (IDP)

IDP는 조직 내부에서 개발자가 애플리케이션을 배포, 운영, 모니터링할 때 필요한 도구와 워크플로우를 하나로 통합한 내부용 플랫폼이다. 개발자는 인프라 전문 지식 없이도 미리 정의된 셀프서비스 인터페이스를 통해 필요한 리소스를 요청하고 사용할 수 있다.

**왜 필요한가** — 각 팀이 개별적으로 인프라를 다루면 중복 작업과 실수가 늘어나고 온보딩 속도가 느려지는 문제를 해결하기 위해 사용한다.

**발표에서는** — 이번 자료의 중심 주제로, 이후 소개되는 도구들이 어떻게 IDP를 구성하는 요소가 되는지의 맥락으로 다뤄진다.

### Crossplane

Crossplane은 클라우드 인프라(가상머신, 데이터베이스, 네트워크 등)를 Kubernetes의 커스텀 리소스(CRD) 형태로 선언적으로 관리할 수 있게 해주는 오픈소스 도구다. 즉, kubectl로 클라우드 리소스를 생성하고 관리할 수 있다.

**왜 필요한가** — 여러 클라우드 프로바이더의 인프라를 일관된 Kubernetes API로 추상화해 플랫폼 팀이 표준화된 셀프서비스 인터페이스를 제공하기 위해 사용한다.

**발표에서는** — IDP를 구성하는 인프라 추상화 계층의 대표 예시로 함께 언급된다.

### Argo CD

Argo CD는 Git 저장소에 정의된 상태를 Kubernetes 클러스터에 자동으로 동기화해주는 GitOps 기반 지속적 배포 도구다.

**왜 필요한가** — 수동 배포로 인한 실수와 환경 간 불일치를 줄이고, 배포 과정을 코드로 추적 가능하게 만들기 위해 사용한다.

**발표에서는** — IDP의 배포 자동화 구성요소로 함께 소개된다.

### Kyverno

Kyverno는 Kubernetes 네이티브 정책 엔진으로, YAML 형태로 정책을 작성해 리소스 생성 시 규칙을 검증하거나 자동으로 수정할 수 있게 해준다.

**왜 필요한가** — 셀프서비스 환경에서 개발자가 자유롭게 리소스를 생성하더라도 보안 및 운영 표준을 강제하기 위해 사용한다.

**발표에서는** — IDP에서 거버넌스와 안전장치를 담당하는 구성요소로 함께 다뤄진다.

## 🧭 추구 방향과 흐름

- **Platform as a Product** — IDP를 단순 인프라 제공이 아니라 내부 고객(개발자)을 위한 제품처럼 설계하고 지속적으로 개선하는 방향이다. 이는 플랫폼 팀이 사용자 피드백을 반영해 셀프서비스 인터페이스를 다듬어야 한다는 관점에서 나온다.
- **Self-Service Infrastructure** — Crossplane과 같은 도구를 통해 개발자가 티켓 없이도 필요한 인프라를 직접 요청하고 생성할 수 있는 방향으로 나아간다. 이는 인프라팀의 병목을 줄이는 것을 목표로 한다.
- **정책 기반 거버넌스(Policy as Code)** — Kyverno처럼 정책을 코드로 관리해 자동으로 검증하는 방향이 강조된다. 셀프서비스와 안전성을 동시에 확보하기 위한 접근으로 다뤄진다.

## 🚀 바로 활용하기

1. 로컬 환경에 Kubernetes 클러스터(minikube 또는 kind)를 구성하고 Crossplane을 설치해 간단한 클라우드 리소스를 CRD로 생성해본다.
2. Argo CD 공식 문서의 Getting Started 가이드를 따라 Git 저장소와 클러스터를 동기화하는 기본 GitOps 흐름을 실습한다.
3. Kyverno를 설치하고 기본 정책 예제(예: 특정 라벨 필수화)를 적용해 정책 위반 시 어떻게 차단되는지 확인한다.
4. CNCF의 Platform Engineering 관련 자료를 읽고 IDP 설계 원칙을 정리해본다.

## 🔗 참고 자료

- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Crossplane의 개념과 설치 방법을 확인할 수 있는 공식 문서.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 자동화를 시작하기 위한 공식 가이드.
- [Kyverno 공식 홈페이지](https://kyverno.io) — Kubernetes 정책 관리 도구인 Kyverno의 개념과 예제를 확인할 수 있다.
- [Kubernetes 공식 홈페이지](https://kubernetes.io) — IDP의 기반이 되는 Kubernetes 개념을 학습할 수 있는 출발점.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Platform Engineering 및 관련 CNCF 프로젝트 생태계 전반을 살펴볼 수 있다.
