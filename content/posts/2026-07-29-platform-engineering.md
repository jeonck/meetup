---
title: "2026-07-29 Platform Engineering 입문 브리프"
date: 2026-07-29T07:55:54.378782+09:00
tags: ["platform-engineering", "backstage", "developer-experience", "tech-brief"]
---
## 오늘의 기술 토픽

> **Platform Engineering**

이번 자료는 실제 밋업 발표 대신, 최근 개발자 커뮤니티에서 화두인 Platform Engineering을 중심으로 정리한 압축 브리프입니다. Platform Engineering은 개발자가 인프라나 배포 과정을 직접 신경 쓰지 않고도 빠르게 서비스를 만들 수 있도록, 셀프서비스 플랫폼을 구축하는 접근 방식을 말합니다. Backstage, Crossplane, Kubernetes 같은 도구들이 이 플랫폼을 구성하는 대표적인 조각으로 함께 다뤄집니다. 전체 흐름은 '플랫폼을 하나의 제품처럼 만들어 내부 개발자에게 제공한다'는 방향으로 수렴합니다.

## 🔑 핵심 요점

- Platform Engineering은 개발자 경험(DevEx)을 개선하기 위해 내부 플랫폼을 하나의 제품처럼 설계하고 운영하는 접근이다.
- 핵심 목표는 개발자가 인프라 복잡도를 직접 다루지 않고도 셀프서비스로 배포/운영할 수 있게 만드는 것이다.
- Backstage 같은 개발자 포털은 여러 도구와 문서를 한곳에 모아 플랫폼 사용성을 높이는 역할을 한다.
- Crossplane은 클라우드 리소스를 Kubernetes API로 선언적으로 관리해 플랫폼 자동화의 기반이 된다.
- Kubernetes는 대부분의 Platform Engineering 사례에서 표준 실행 환경으로 자리잡고 있다.
- 골든 패스(golden path)를 제공해 팀마다 다른 방식으로 인프라를 다루는 혼란을 줄이는 것이 중요한 흐름이다.

## 🛠 핵심 기술 쉽게 이해하기

### Platform Engineering

Platform Engineering은 개발팀이 애플리케이션을 더 쉽고 빠르게 만들고 배포할 수 있도록, 별도의 플랫폼팀이 셀프서비스 도구와 표준 워크플로우를 설계하는 조직적/기술적 접근입니다. 단순히 인프라를 자동화하는 것을 넘어, 플랫폼 자체를 하나의 내부 제품처럼 관리한다는 점이 특징입니다.

**왜 필요한가** — 개발자가 매번 클라우드 설정, 배포 파이프라인, 보안 정책을 직접 다뤄야 한다면 생산성이 크게 떨어지기 때문에, 이런 반복 작업을 플랫폼 레벨에서 표준화하고 자동화하기 위해 등장했습니다.

**발표에서는** — 이번 브리프 전체의 핵심 주제로, 나머지 기술들이 이 개념을 실현하기 위한 구성 요소로 소개됩니다.

### Backstage

Backstage는 Spotify가 만들고 CNCF에 기증한 오픈소스 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿 등을 한 화면에서 볼 수 있게 해줍니다. 조직 내 여러 서비스와 도구가 흩어져 있을 때 이를 통합하는 창구 역할을 합니다.

**왜 필요한가** — 개발자가 필요한 정보와 도구를 찾기 위해 여러 시스템을 헤매는 시간을 줄이고, 새로운 서비스 생성 같은 반복 작업을 템플릿화하기 위해 사용합니다.

**발표에서는** — Platform Engineering을 실제로 구현할 때 가장 널리 쓰이는 개발자 포털 도구로 언급되는 관련 기술입니다.

### Crossplane

Crossplane은 Kubernetes API를 확장해 클라우드 리소스(예: 데이터베이스, 네트워크)를 선언적인 YAML로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다. 여러 클라우드 제공자의 리소스를 하나의 일관된 방식으로 다룰 수 있습니다.

**왜 필요한가** — 플랫폼팀이 표준화된 인프라 provisioning 인터페이스를 만들어, 개발자에게는 복잡한 클라우드 설정을 감추고 간단한 API만 제공하기 위해 사용합니다.

**발표에서는** — Platform Engineering의 자동화/셀프서비스 계층을 구현하는 대표적인 도구로 함께 다뤄지는 관련 기술입니다.

### Kubernetes

Kubernetes는 컨테이너화된 애플리케이션을 배포, 확장, 운영하기 위한 오픈소스 오케스트레이션 플랫폼입니다. 대부분의 현대적인 클라우드 네이티브 인프라의 기반 레이어로 쓰입니다.

**왜 필요한가** — 여러 서비스를 안정적으로 배포하고 자동으로 복구/확장하기 위해 필요하며, Platform Engineering 도구들(Backstage, Crossplane 등)이 그 위에서 동작하는 공통 실행 환경입니다.

**발표에서는** — 다른 도구들이 동작하는 기반 인프라로서 함께 언급되는 관련 기술입니다.

## 🧭 추구 방향과 흐름

- **플랫폼을 제품처럼 (Platform as a Product)** — 플랫폼팀이 인프라를 단순 지원 업무가 아니라 내부 고객(개발자)을 위한 제품으로 취급하는 방향입니다. Backstage 같은 포털 도구가 이 제품화 흐름을 뒷받침하는 대표 사례로 다뤄집니다.
- **셀프서비스와 골든 패스** — 개발자가 플랫폼팀에 요청하지 않고도 표준화된 '골든 패스'를 따라 스스로 배포/프로비저닝할 수 있게 만드는 흐름입니다. Crossplane 같은 선언적 리소스 관리 도구가 이 셀프서비스를 기술적으로 가능하게 합니다.
- **Kubernetes 중심의 표준화** — 여러 클라우드와 도구를 아우르는 표준 실행 환경으로 Kubernetes가 자리잡으면서, Platform Engineering 도구들이 Kubernetes API를 확장하는 방식으로 발전하고 있습니다.

## 🚀 바로 활용하기

1. platformengineering.org에서 Platform Engineering의 정의와 성숙도 모델을 읽어본다.
2. Backstage 공식 문서의 Getting Started 가이드를 따라 로컬에 데모 포털을 설치해본다.
3. Crossplane 공식 문서를 보고 간단한 클라우드 리소스(예: 스토리지 버킷)를 선언적으로 provisioning 해본다.
4. CNCF의 Platforms Working Group 자료를 살펴보며 커뮤니티가 정의하는 골든 패스 사례를 참고한다.

## 🔗 참고 자료

- [Platform Engineering 공식 사이트](https://platformengineering.org) — Platform Engineering의 정의와 개념을 뒷받침하는 커뮤니티 공식 자료
- [Backstage 공식 사이트](https://backstage.io) — Backstage 개발자 포털 도구에 대한 공식 소개와 문서
- [Crossplane 공식 사이트](https://www.crossplane.io) — Crossplane의 선언적 클라우드 리소스 관리 개념을 뒷받침하는 공식 자료
- [Kubernetes 공식 사이트](https://kubernetes.io) — Platform Engineering의 기반 실행 환경인 Kubernetes에 대한 공식 문서
- [CNCF 공식 사이트](https://www.cncf.io) — Backstage 등 Platform Engineering 관련 프로젝트를 다루는 CNCF 생태계 자료
