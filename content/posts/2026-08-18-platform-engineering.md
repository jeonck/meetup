---
title: "2026-08-18 Platform Engineering 입문: 셀프서비스 플랫폼으로 가는 길"
date: 2026-08-18T07:20:24.025670+09:00
tags: ["platform-engineering", "kubernetes", "gitops", "tech-brief"]
---
## 오늘의 기술 토픽

> **Platform Engineering**

이번 자료는 특정 밋업 발표가 아니라 Platform Engineering이라는 주제를 중심으로 정리한 브리프입니다. Platform Engineering은 개발자가 인프라 복잡성을 신경 쓰지 않고 빠르게 서비스를 배포할 수 있도록 내부 개발자 플랫폼(IDP)을 구축하는 접근 방식입니다. Kubernetes 생태계가 성숙하면서 운영 복잡도를 낮추기 위한 방법으로 Crossplane, Backstage, Argo CD 같은 도구들이 함께 언급됩니다. 이 브리프는 개념 이해와 학습 시작점을 제공하는 데 초점을 맞춥니다.

## 🔑 핵심 요점

- Platform Engineering은 개발자 경험(DevEx)을 개선하기 위해 내부 개발자 플랫폼을 만드는 활동입니다.
- 핵심 목표는 개발자가 인프라 세부사항을 몰라도 셀프서비스로 배포할 수 있게 만드는 것입니다.
- Crossplane 같은 도구는 클라우드 리소스를 Kubernetes API로 추상화해 플랫폼 구축을 돕습니다.
- Backstage는 여러 플랫폼 기능을 하나의 개발자 포털로 모아주는 대표적인 도구입니다.
- GitOps 도구인 Argo CD는 플랫폼의 배포 자동화 계층으로 자주 함께 쓰입니다.
- Platform as a Product라는 사고방식이 이 흐름의 핵심 철학으로 자리잡고 있습니다.

## 🛠 핵심 기술 쉽게 이해하기

### Platform Engineering

Platform Engineering은 개발팀이 애플리케이션을 더 쉽고 안전하게 배포·운영할 수 있도록 재사용 가능한 도구와 워크플로우를 갖춘 내부 플랫폼을 설계하고 운영하는 분야입니다. 인프라, CI/CD, 보안 정책 등을 표준화된 셀프서비스 형태로 제공하는 것이 핵심입니다.

**왜 필요한가** — 각 개발팀이 매번 인프라를 직접 다루면 중복 작업과 실수가 늘어나는데, 플랫폼 팀이 이를 표준화하면 개발 속도와 안정성을 동시에 높일 수 있습니다.

**발표에서는** — 이 주제 전반을 관통하는 핵심 개념으로, 아래 기술들은 모두 이 플랫폼을 구성하는 요소로 다뤄집니다.

### Crossplane

Crossplane은 클라우드 프로바이더(AWS, GCP, Azure 등)의 리소스를 Kubernetes 커스텀 리소스로 정의하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다. Kubernetes API를 확장해 인프라를 코드로 선언적으로 관리합니다.

**왜 필요한가** — 여러 클라우드 리소스를 각기 다른 콘솔이나 도구 대신 하나의 Kubernetes API로 통합 관리하고, 개발자에게는 단순화된 인터페이스만 제공하기 위해 사용됩니다.

**발표에서는** — Platform Engineering에서 인프라 프로비저닝을 자동화하는 대표적인 구성 요소로 언급됩니다.

### Backstage

Backstage는 Spotify가 만들고 CNCF에 기증한 오픈소스 개발자 포털 프레임워크로, 서비스 카탈로그, 문서, 템플릿 등을 한 곳에서 관리할 수 있게 해줍니다.

**왜 필요한가** — 여러 팀이 흩어진 도구와 문서를 오가며 시간을 낭비하지 않도록, 개발자가 필요한 모든 정보와 셀프서비스 기능을 한 화면에서 찾을 수 있게 합니다.

**발표에서는** — IDP(내부 개발자 플랫폼)의 UI 계층으로서 Platform Engineering 논의에서 자주 함께 언급되는 도구입니다.

### Argo CD

Argo CD는 Kubernetes를 위한 GitOps 기반 지속적 배포 도구로, Git 저장소에 선언된 상태를 클러스터에 자동으로 동기화합니다.

**왜 필요한가** — 배포 과정을 코드로 관리하고 이력 추적과 롤백을 쉽게 만들어, 플랫폼의 배포 자동화 계층을 담당합니다.

**발표에서는** — 플랫폼이 제공하는 셀프서비스 배포 파이프라인의 실행 엔진 역할로 다뤄집니다.

## 🧭 추구 방향과 흐름

- **Platform as a Product** — 플랫폼 팀이 인프라를 단순 관리 대상이 아니라 내부 고객(개발자)을 위한 제품으로 취급하는 방향입니다. 이는 사용자 경험, 문서화, 피드백 루프를 중시하는 접근으로 이어집니다.
- **셀프서비스 인프라** — 개발자가 티켓을 발행하고 기다리는 대신, 표준화된 템플릿과 API를 통해 스스로 인프라를 프로비저닝할 수 있게 만드는 흐름입니다. Crossplane과 같은 도구가 이를 기술적으로 뒷받침합니다.
- **GitOps 기반 자동화** — 배포와 인프라 변경을 Git을 단일 진실 공급원(source of truth)으로 삼아 관리하는 방식이 플랫폼 구축의 표준으로 자리잡고 있습니다.

## 🚀 바로 활용하기

1. Kubernetes 클러스터(minikube 또는 kind)를 로컬에 띄우고 Crossplane을 설치해 클라우드 리소스를 커스텀 리소스로 정의해보세요.
2. Backstage 공식 문서의 Getting Started 가이드를 따라 로컬에 개발자 포털을 띄워보세요.
3. Argo CD를 설치하고 간단한 Git 저장소를 연결해 GitOps 배포 흐름을 직접 경험해보세요.
4. CNCF의 Platform Engineering 관련 자료를 읽고 Platform as a Product 개념을 정리해보세요.

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — Platform Engineering의 기반이 되는 Kubernetes 개념과 아키텍처를 확인할 수 있습니다.
- [Crossplane 공식 사이트](https://www.crossplane.io) — 클라우드 리소스를 Kubernetes API로 관리하는 방법을 다루는 공식 문서입니다.
- [Argo CD 공식 문서](https://argo-cd.readthedocs.io) — GitOps 기반 배포 자동화 설정 방법을 안내합니다.
- [CNCF 공식 사이트](https://www.cncf.io) — Platform Engineering 및 관련 클라우드 네이티브 프로젝트들의 생태계 정보를 제공합니다.
