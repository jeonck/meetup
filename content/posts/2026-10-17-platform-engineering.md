---
title: "2026-10-17 Platform Engineering 입문: 셀프서비스 플랫폼으로 가는 길"
date: 2026-10-17T09:08:43.222946+09:00
tags: ["platform-engineering", "backstage", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Platform Engineering**

최근 개발자 커뮤니티에서는 애플리케이션 개발자가 인프라 복잡도를 신경 쓰지 않고도 빠르게 배포할 수 있도록 돕는 Platform Engineering이 꾸준히 화두로 떠오르고 있다. 이는 과거 DevOps가 모든 개발자에게 운영 지식을 요구했던 것과 달리, 플랫폼 팀이 표준화된 도구와 워크플로를 '내부 제품'처럼 제공하는 방식으로 전환하는 흐름이다. Backstage 같은 개발자 포털, Crossplane 같은 인프라 추상화 도구, Argo CD 같은 GitOps 배포 도구가 이 흐름을 뒷받침하는 핵심 생태계로 자리잡고 있다. 이 글은 Platform Engineering의 개념과 주변 기술, 그리고 처음 공부를 시작하는 사람이 밟을 수 있는 구체적인 단계를 정리한다.

## 🔑 핵심 요점

- Platform Engineering은 개발자의 인지 부하를 줄이기 위해 플랫폼 팀이 내부 플랫폼을 '제품'처럼 설계하고 운영하는 접근이다.
- Backstage는 여러 도구와 서비스 카탈로그를 한곳에 모아주는 개발자 포털로, 셀프서비스 환경의 진입점 역할을 한다.
- Crossplane은 Kubernetes API를 확장해 클라우드 인프라를 선언적으로 관리할 수 있게 해주는 도구다.
- Argo CD는 Git 저장소의 선언적 상태를 클러스터에 자동으로 동기화하는 GitOps 배포 도구다.
- Golden Path(표준 배포 경로)를 제공하면 개발자는 매번 인프라를 처음부터 설계할 필요 없이 검증된 패턴을 재사용할 수 있다.
- Platform Engineering은 단순한 도구 도입이 아니라 플랫폼을 내부 고객(개발자)을 위한 제품으로 바라보는 문화적 전환을 포함한다.

## 🛠 핵심 기술 쉽게 이해하기

### Platform Engineering

Platform Engineering은 소프트웨어 개발팀이 애플리케이션을 더 쉽고 빠르게 빌드·배포·운영할 수 있도록, 전담 플랫폼 팀이 셀프서비스 도구와 표준화된 워크플로를 제공하는 분야다. 쉽게 말해 개발자가 인프라를 직접 다루지 않고도 필요한 리소스를 '주문'만 하면 받을 수 있게 만드는 체계다.

**왜 필요한가** — 조직이 커지면 각 팀이 Kubernetes, 클라우드 인프라, CI/CD를 각자 다른 방식으로 다루면서 중복 작업과 운영 부담이 커지는 문제를 해결하기 위해 등장했다.

**발표에서는** — 이 글의 중심 주제로, 왜 조직이 플랫폼 팀을 두고 내부 플랫폼을 구축하는지와 그 배경이 되는 문제의식을 다룬다.

### Backstage

Backstage는 Spotify가 만들고 CNCF에 기증한 오픈소스 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿을 한 화면에서 볼 수 있게 해준다.

**왜 필요한가** — 조직 내에 흩어진 서비스, 도구, 문서를 개발자가 찾기 쉽게 한곳에 모아 셀프서비스 경험을 제공하기 위해 쓰인다.

**발표에서는** — Platform Engineering 생태계에서 개발자가 플랫폼 기능에 접근하는 '진입점(UI)' 역할을 하는 대표 도구로 소개된다.

### Crossplane

Crossplane은 Kubernetes의 Custom Resource를 활용해 AWS, GCP, Azure 같은 클라우드 리소스를 Kubernetes API로 선언적으로 생성·관리할 수 있게 해주는 오픈소스 프로젝트다.

**왜 필요한가** — 여러 클라우드 제공업체별 콘솔이나 Terraform 스크립트 대신, 하나의 Kubernetes 기반 인터페이스로 인프라를 관리해 플랫폼 팀이 표준화된 API를 제공할 수 있게 한다.

**발표에서는** — 플랫폼 팀이 Golden Path 뒤편에서 실제 인프라를 프로비저닝하는 엔진으로 다뤄진다.

### Argo CD

Argo CD는 Git 저장소에 선언된 애플리케이션 상태를 Kubernetes 클러스터에 자동으로 동기화해주는 GitOps 기반 지속적 배포 도구다.

**왜 필요한가** — 배포 과정을 Git 커밋 기반으로 투명하고 추적 가능하게 만들어, 수동 배포로 인한 실수와 불일치를 줄이기 위해 쓰인다.

**발표에서는** — Platform Engineering 워크플로에서 개발자가 만든 템플릿 결과물을 실제로 클러스터에 배포하는 마지막 단계로 언급된다.

## 🧭 추구 방향과 흐름

- **Platform as a Product** — 플랫폼 팀은 내부 플랫폼을 단순한 인프라 집합이 아니라 개발자를 고객으로 둔 '제품'으로 바라본다. 사용자 피드백을 받아 기능을 개선하고, 문서와 온보딩 경험을 제품처럼 다듬는 방향으로 나아가고 있다.
- **셀프서비스와 Golden Path** — 개발자가 티켓을 올리고 기다리는 대신 포털에서 템플릿을 선택해 즉시 환경을 받는 셀프서비스 모델이 확산되고 있다. 표준화된 '황금 경로'를 제공해 매번 처음부터 설계하지 않고도 안전한 기본값을 재사용하게 한다.
- **GitOps 기반 선언적 인프라** — Crossplane과 Argo CD처럼 Kubernetes API와 Git을 중심으로 인프라와 배포를 선언적으로 관리하는 방식이 표준으로 자리잡고 있다. 이는 변경 이력 추적과 재현 가능한 환경 구성을 쉽게 만들어준다.

## 🚀 바로 활용하기

1. 로컬 환경에 Backstage를 설치해 서비스 카탈로그와 소프트웨어 템플릿 기능을 직접 체험해본다.
2. Crossplane 공식 Getting Started 가이드를 따라 Kubernetes 클러스터에서 간단한 클라우드 리소스(예: S3 버킷)를 선언적으로 생성해본다.
3. Argo CD를 설치하고 Git 저장소와 연결해 애플리케이션이 자동으로 동기화되는 과정을 직접 확인한다.
4. platformengineering.org에서 Platform Engineering의 핵심 개념과 커뮤니티 자료를 읽어본다.

## 🔗 참고 자료

- [Platform Engineering 공식 커뮤니티 사이트](https://platformengineering.org) — Platform Engineering의 개념과 Platform as a Product 철학에 대한 기본 자료를 제공한다.
- [Backstage 공식 홈페이지](https://backstage.io) — 개발자 포털 도구인 Backstage의 설치 방법과 플러그인 생태계를 설명한다.
- [Crossplane 공식 홈페이지](https://www.crossplane.io) — Kubernetes API 기반 인프라 관리 도구인 Crossplane의 개념과 문서를 제공한다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 도구인 Argo CD의 설치와 사용법을 설명한다.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Backstage를 비롯한 Platform Engineering 관련 프로젝트들을 호스팅하는 재단의 자료를 제공한다.
