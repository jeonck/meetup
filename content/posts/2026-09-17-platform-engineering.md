---
title: "2026-09-17 Platform Engineering, 개발자 경험을 상품처럼 설계하기"
date: 2026-09-17T09:03:23.435938+09:00
tags: ["platform-engineering", "backstage", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Platform Engineering**

Platform Engineering은 여러 팀이 반복적으로 겪는 인프라·배포·보안 설정의 복잡함을 내부 플랫폼 팀이 대신 표준화해 제공하는 접근 방식이다. 핵심은 개발자가 인프라 세부사항을 몰라도 셀프서비스로 원하는 리소스를 얻을 수 있게 만드는 것이며, 이를 위해 Backstage 같은 개발자 포털, Crossplane 같은 인프라 추상화 도구, Kubernetes 기반 실행 환경이 함께 사용된다. 최근 커뮤니티는 이를 단순한 도구 도입이 아니라 '플랫폼을 제품처럼 다루는' 조직 문화의 변화로 보고 있다. 이 브리핑은 별도 밋업 발표 없이 해당 주제를 학습 관점에서 정리한 요약이다.

## 🔑 핵심 요점

- Platform Engineering은 개발자가 반복적으로 겪는 인프라 설정 부담을 줄이기 위해 내부 플랫폼 팀이 표준화된 셀프서비스 환경을 제공하는 접근이다.
- 핵심 산출물은 'Internal Developer Platform(IDP)'이라 불리는, 개발자가 UI나 CLI로 리소스를 요청하면 자동으로 provisioning되는 시스템이다.
- Backstage는 여러 도구와 문서를 한곳에 모으는 개발자 포털 역할을 하며, Crossplane은 클라우드 리소스를 Kubernetes API처럼 다루게 해준다.
- 플랫폼을 만드는 것 자체가 아니라 '플랫폼을 제품으로서 지속적으로 개선하는 것'이 커뮤니티가 강조하는 방향이다.
- 보안·컴플라이언스 정책은 Kyverno 같은 정책 엔진으로 플랫폼 레벨에서 자동 강제하는 shift-left 방식이 선호된다.
- DORA metrics 같은 지표로 플랫폼 도입 효과(배포 빈도, 리드타임 등)를 측정하는 흐름이 확산되고 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Platform Engineering

여러 개발팀이 공통으로 겪는 인프라, 배포, 모니터링 설정의 복잡함을 내부 전담 팀이 표준화된 셀프서비스 도구로 제공하는 실천 방법론이다. 개발자는 플랫폼이 제공하는 인터페이스만 사용하면 되고, 그 뒤의 클라우드·쿠버네티스 세부사항은 몰라도 된다.

**왜 필요한가** — 각 팀이 개별적으로 인프라를 구성하면 중복 작업과 설정 편차, 보안 사고 위험이 커지기 때문에 이를 중앙화된 플랫폼으로 해결한다.

**발표에서는** — 이 브리핑에서는 Platform Engineering을 전체 주제의 뼈대로 삼아, 관련 도구들이 어떤 역할을 하는지 설명하는 축으로 다룬다.

### Backstage

Spotify가 만들어 CNCF에 기증한 오픈소스 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿 기반 리소스 생성 기능을 한 화면에서 제공한다.

**왜 필요한가** — 여러 팀에 흩어진 서비스 정보와 도구를 한곳에 모아 개발자가 무엇을 어디서 찾아야 할지 헤매지 않게 해준다.

**발표에서는** — Internal Developer Platform을 구현할 때 가장 널리 쓰이는 프론트엔드 계층으로 언급되는 도구다.

### Crossplane

Kubernetes API를 확장해 클라우드 리소스(DB, 네트워크, 스토리지 등)를 쿠버네티스 매니페스트처럼 선언적으로 관리할 수 있게 해주는 오픈소스 프로젝트다.

**왜 필요한가** — 개발자가 클라우드 콘솔이나 Terraform 문법을 몰라도, 플랫폼 팀이 미리 만들어둔 'Composition'을 통해 표준화된 방식으로 인프라를 요청할 수 있게 한다.

**발표에서는** — Platform Engineering에서 인프라 추상화 계층을 만드는 대표 도구로 함께 다뤄진다.

### Kubernetes

컨테이너화된 애플리케이션을 자동으로 배포, 확장, 관리해주는 오픈소스 오케스트레이션 시스템이다.

**왜 필요한가** — 대부분의 현대 Internal Developer Platform이 그 위에서 동작하는 실행 기반이기 때문에 Platform Engineering 논의의 전제가 된다.

**발표에서는** — Backstage와 Crossplane 등 다른 도구들이 동작하는 공통 인프라 계층으로 등장한다.

## 🧭 추구 방향과 흐름

- **플랫폼을 제품으로 다루기 (Platform as a Product)** — 플랫폼 팀이 일회성 인프라 구축이 아니라, 내부 개발자를 '고객'으로 보고 지속적으로 사용성을 개선하는 제품 관리 방식을 적용하는 흐름이다. 이는 Backstage 같은 포털이 단순 문서 모음이 아니라 사용자 피드백 기반으로 계속 발전하는 이유이기도 하다.
- **셀프서비스와 골든 패스** — 개발자가 티켓을 열지 않고도 표준화된 템플릿(golden path)을 통해 스스로 환경을 만들 수 있게 하는 방향이다. Crossplane Composition과 Backstage 템플릿 기능이 이 흐름을 뒷받침한다.
- **정책 기반 shift-left 보안** — 보안·컴플라이언스 검사를 배포 이후가 아니라 플랫폼이 리소스를 생성하는 시점에 정책 엔진(Kyverno 등)으로 자동 강제하는 방향으로 이동하고 있다.
- **데이터 기반 플랫폼 효과 측정** — DORA metrics 같은 지표를 활용해 플랫폼 도입 전후의 배포 빈도, 리드타임, 장애 복구 시간을 비교함으로써 플랫폼 투자의 효과를 객관적으로 입증하려는 움직임이 커지고 있다.

## 🚀 바로 활용하기

1. platformengineering.org의 정의와 사례 문서를 읽고 Internal Developer Platform 개념부터 정리해본다.
2. 로컬 환경에 Backstage 데모(create-app)를 설치해 서비스 카탈로그 화면을 직접 만들어본다.
3. Crossplane 공식 문서의 Getting Started를 따라 간단한 Composition으로 클라우드 리소스 하나를 provisioning해본다.
4. DORA metrics 사이트에서 배포 빈도·리드타임 지표 정의를 확인하고 자신의 팀에 적용 가능한지 검토한다.

## 🔗 참고 자료

- [Platform Engineering 공식 사이트](https://platformengineering.org) — Platform Engineering의 정의와 Internal Developer Platform 개념의 출처
- [Backstage 공식 문서](https://backstage.io) — 개발자 포털 및 셀프서비스 템플릿 기능 설명
- [Crossplane 공식 사이트](https://www.crossplane.io) — Kubernetes API 기반 인프라 추상화 도구 소개
- [Kubernetes 공식 문서](https://kubernetes.io) — 플랫폼이 동작하는 기반 오케스트레이션 시스템
- [Kyverno 공식 사이트](https://kyverno.io) — shift-left 정책 강제에 사용되는 정책 엔진
- [DORA](https://dora.dev) — 플랫폼 도입 효과를 측정하는 지표(배포 빈도, 리드타임 등)의 출처
- [CNCF](https://www.cncf.io) — Backstage, Crossplane 등 관련 오픈소스 프로젝트를 호스팅하는 재단
