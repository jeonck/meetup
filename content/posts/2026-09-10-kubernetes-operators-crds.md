---
title: "2026-09-10 Kubernetes Operators & CRDs로 시작하는 플랫폼 자동화"
date: 2026-09-10T08:48:12.021365+09:00
tags: ["kubernetes-operator", "crd", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

Kubernetes Operators와 Custom Resource Definitions(CRD)는 클러스터 위에 도메인 지식을 코드로 담아 반복 운영 작업을 자동화하는 핵심 확장 메커니즘입니다. 이번 브리핑에서는 CRD로 새로운 리소스 타입을 정의하고 Operator가 이를 감시하며 원하는 상태를 유지하는 기본 원리를 정리합니다. 함께 Crossplane, Kyverno, kagent 같은 연관 생태계 도구들도 살펴보며, Kubernetes 확장 패턴이 어디로 향하고 있는지 짚어봅니다. 실무에서 바로 시도해볼 수 있는 학습 경로도 함께 제시합니다.

## 🔑 핵심 요점

- CRD는 Kubernetes API를 확장해 사용자 정의 리소스 타입을 등록하는 방법입니다.
- Operator는 컨트롤러 패턴을 이용해 CRD로 정의된 리소스의 원하는 상태(desired state)를 지속적으로 관찰하고 수렴시킵니다.
- 복잡한 애플리케이션 운영 지식(백업, 스케일링, 장애 복구 등)을 코드로 캡슐화할 수 있는 것이 Operator의 핵심 가치입니다.
- Crossplane은 CRD/Operator 패턴을 클라우드 인프라 프로비저닝까지 확장한 대표 사례입니다.
- Kyverno는 CRD 기반 정책을 통해 클러스터 리소스 생성 시점에 검증과 변형을 적용합니다.
- 생태계는 점점 더 많은 운영 업무를 선언적 리소스와 컨트롤러 루프로 옮기는 방향으로 발전하고 있습니다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes Operators & CRDs

CRD(Custom Resource Definition)는 Kubernetes API에 새로운 리소스 종류를 등록하는 방법이고, Operator는 그 리소스를 지속적으로 감시하며 실제 상태를 원하는 상태에 맞춰 조정하는 컨트롤러입니다. 예를 들어 데이터베이스를 나타내는 CRD를 만들고, Operator가 실제 데이터베이스 인스턴스를 생성·백업·복구하도록 만들 수 있습니다.

**왜 필요한가** — 사람이 반복적으로 수행하던 운영 작업(설치, 업그레이드, 장애 복구 등)을 자동화하고, 도메인 전문가의 운영 노하우를 소프트웨어로 코드화하기 위해 사용합니다.

**발표에서는** — CRD와 Operator의 기본 개념과 동작 원리가 이번 브리핑의 핵심 주제로 다뤄졌습니다.

### Crossplane

Crossplane은 Kubernetes API를 확장해 클라우드 리소스(데이터베이스, 네트워크, 스토리지 등)를 Kubernetes 커스텀 리소스로 선언하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다. Operator 패턴을 인프라 프로비저닝 영역까지 넓힌 사례로 볼 수 있습니다.

**왜 필요한가** — 여러 클라우드 제공자의 인프라를 하나의 Kubernetes API로 통일해서 관리하고, 플랫폼 팀이 셀프서비스 인프라를 제공하기 위해 사용합니다.

**발표에서는** — CRD/Operator 패턴의 실제 적용 사례로 언급되는 연관 기술로 소개되었습니다.

### Kyverno

Kyverno는 Kubernetes 네이티브 정책 엔진으로, YAML로 정책을 작성해 리소스 생성 시 검증(validation), 변형(mutation), 생성(generation)을 수행합니다. 별도의 언어 학습 없이 Kubernetes 매니페스트와 유사한 방식으로 정책을 정의할 수 있습니다.

**왜 필요한가** — 클러스터 전체에 보안 및 운영 규칙을 일관되게 강제하기 위해 사용하며, 잘못된 설정이 배포되기 전에 차단합니다.

**발표에서는** — CRD 기반 정책 관리의 연관 사례로 소개되었습니다.

### kagent

kagent는 Kubernetes 클러스터 내에서 AI 에이전트를 활용해 운영 작업을 보조하도록 설계된 프로젝트로, CRD 기반으로 에이전트의 행동과 도구를 정의합니다.

**왜 필요한가** — 클러스터 운영에서 반복되는 진단, 트러블슈팅 작업에 AI 에이전트를 결합해 운영 효율을 높이기 위해 사용됩니다.

**발표에서는** — Operator 패턴이 AI 에이전트 운영으로 확장되는 최신 흐름의 연관 사례로 언급되었습니다.

## 🧭 추구 방향과 흐름

- **운영 지식의 코드화(Operator Pattern 확산)** — 점점 더 많은 팀이 수동 운영 절차를 CRD와 Operator로 감싸 선언적 리소스로 관리하는 방향으로 이동하고 있습니다. Crossplane처럼 인프라 프로비저닝까지 이 패턴을 적용하는 사례가 늘어나는 것이 근거입니다.
- **플랫폼을 제품처럼(Platform as a Product)** — CRD로 정의된 커스텀 API를 통해 개발자에게 셀프서비스 인터페이스를 제공하는 흐름이 강화되고 있습니다. 복잡한 인프라나 정책 세부사항은 Operator와 정책 엔진 뒤로 숨기고, 개발자는 간단한 리소스 선언만으로 원하는 결과를 얻도록 하는 방향입니다.
- **정책과 거버넌스의 선언적 관리** — Kyverno와 같은 정책 엔진이 CRD 기반으로 보안·컴플라이언스 규칙을 코드화하는 흐름이 확산되고 있습니다. 이는 수동 검토 대신 자동화된 가드레일로 거버넌스를 강제하는 shift-left 방향과 맞닿아 있습니다.

## 🚀 바로 활용하기

1. 로컬에 kind나 minikube로 클러스터를 띄우고 간단한 CRD를 직접 정의해봅니다.
2. kubebuilder나 Operator SDK를 사용해 기본 Operator 스캐폴딩을 만들어보고 reconcile 루프의 동작을 관찰합니다.
3. Crossplane 공식 문서의 Getting Started를 따라 하나의 클라우드 리소스를 CRD로 프로비저닝해봅니다.
4. Kyverno를 클러스터에 설치하고 기본 정책 몇 개를 적용해 validation이 동작하는 흐름을 확인합니다.

## 🔗 참고 자료

- [Kubernetes 공식 문서 - Custom Resources](https://kubernetes.io) — CRD와 API 확장 개념의 공식 근거 자료입니다.
- [Crossplane 공식 홈페이지](https://www.crossplane.io) — CRD/Operator 패턴을 인프라 프로비저닝에 적용한 대표 프로젝트입니다.
- [Kyverno 공식 홈페이지](https://kyverno.io) — CRD 기반 정책 엔진의 공식 문서입니다.
- [CNCF 공식 홈페이지](https://www.cncf.io) — Operator 패턴과 관련 프로젝트들이 속한 클라우드 네이티브 생태계 전반을 확인할 수 있습니다.
