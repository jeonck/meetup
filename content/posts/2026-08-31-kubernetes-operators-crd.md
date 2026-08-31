---
title: "2026-08-31 Kubernetes Operators & CRD로 알아보는 확장 가능한 인프라 자동화"
date: 2026-08-31T09:10:56.208604+09:00
tags: ["kubernetes-operator", "crd", "crossplane", "tech-brief"]
---
## 오늘의 기술 토픽

> **Kubernetes Operators & CRDs**

이번 브리핑은 Kubernetes의 확장 메커니즘인 Custom Resource Definition(CRD)과 Operator 패턴을 중심으로 정리했다. CRD로 Kubernetes API를 확장하고 Operator가 이를 지속적으로 감시하며 원하는 상태를 유지하는 원리를 다룬다. 함께 Crossplane, Kyverno, Argo CD 등 CRD/Operator 패턴 위에 세워진 대표 생태계 도구들도 짚어본다. Operator 패턴이 어떻게 애플리케이션 운영을 코드로 자동화하는 방향으로 발전하고 있는지 살펴본다.

## 🔑 핵심 요점

- CRD는 Kubernetes API 서버에 사용자 정의 리소스 타입을 등록하는 기능이다.
- Operator는 CRD로 정의된 커스텀 리소스를 감시하고 실제 상태를 원하는 상태로 맞춰주는 컨트롤러다.
- Operator 패턴을 이용하면 사람이 수동으로 하던 운영 작업(백업, 스케일링, 업그레이드 등)을 자동화할 수 있다.
- Crossplane은 CRD/Operator 패턴을 클라우드 인프라 프로비저닝까지 확장한 도구다.
- Kyverno는 CRD 기반 정책을 통해 클러스터 리소스를 검증하고 자동 수정하는 정책 엔진이다.
- Argo CD는 Kubernetes 리소스(및 CRD)를 GitOps 방식으로 지속적으로 동기화하는 도구다.
- 이 생태계는 결국 '플랫폼을 코드와 API로 다루는 것'이라는 공통된 방향을 향하고 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Kubernetes Operators & CRDs

CRD(Custom Resource Definition)는 Kubernetes API에 새로운 리소스 종류를 등록할 수 있게 해주는 확장 기능이고, Operator는 이렇게 정의된 커스텀 리소스를 지속적으로 감시하며 실제 상태를 원하는 상태로 맞춰주는 컨트롤러 프로그램이다. 즉 CRD가 '새로운 API 타입'을 만든다면 Operator는 그 API를 실제로 동작시키는 두뇌 역할을 한다.

**왜 필요한가** — 복잡한 애플리케이션이나 인프라 운영 지식을 코드화해서, 사람이 매번 개입하지 않아도 Kubernetes가 알아서 상태를 유지·복구·확장하게 만들기 위해 사용한다.

**발표에서는** — CRD와 Operator의 기본 개념과 동작 원리를 중심으로 다뤄졌다.

### Crossplane

Crossplane은 CRD와 Operator 패턴을 클라우드 리소스(데이터베이스, 네트워크, VM 등) 프로비저닝에 적용한 오픈소스 프로젝트다. 클라우드 인프라를 Kubernetes 리소스처럼 선언적으로 정의하고 관리할 수 있게 해준다.

**왜 필요한가** — Terraform 같은 별도 도구 없이 Kubernetes API 하나로 애플리케이션과 인프라를 함께 관리하기 위해 사용한다.

**발표에서는** — Operator 패턴이 인프라 프로비저닝 영역까지 확장된 대표 사례로 언급되었다.

### Kyverno

Kyverno는 CRD 기반의 정책(Policy) 리소스를 정의해서 클러스터에 배포되는 리소스를 검증, 변형, 생성할 수 있는 Kubernetes 네이티브 정책 엔진이다.

**왜 필요한가** — 보안 규칙이나 조직 컨벤션을 코드로 강제해서 잘못된 설정이 클러스터에 배포되는 것을 막기 위해 사용한다.

**발표에서는** — CRD를 활용한 정책 자동화 도구의 예시로 다뤄졌다.

### Argo CD

Argo CD는 Git 저장소에 정의된 Kubernetes 매니페스트(및 CRD 리소스)를 클러스터 상태와 지속적으로 비교하고 동기화하는 GitOps 도구다.

**왜 필요한가** — 인프라 변경 이력을 Git으로 관리하고, 배포를 자동화하며, 클러스터 상태를 코드와 일치시키기 위해 사용한다.

**발표에서는** — CRD 기반 리소스를 GitOps 방식으로 관리하는 도구로 언급되었다.

## 🧭 추구 방향과 흐름

- **Everything as Code / API로서의 플랫폼** — CRD와 Operator 패턴은 애플리케이션뿐 아니라 인프라, 정책, 배포까지 모두 Kubernetes API의 리소스로 다루는 흐름을 만들고 있다. Crossplane, Kyverno, Argo CD 모두 이 패턴 위에서 각자의 영역(인프라, 정책, 배포)을 확장한 사례로 볼 수 있다.
- **운영 자동화(Operational Knowledge as Code)** — Operator는 사람이 수동으로 수행하던 반복 운영 작업을 코드로 캡슐화해 자동 복구와 자가 치유(self-healing)를 가능하게 하는 방향으로 발전하고 있다.

## 🚀 바로 활용하기

1. kubectl로 간단한 CRD를 직접 만들어보고 커스텀 리소스를 생성/조회해본다.
2. Kubernetes 공식 문서의 Custom Resources 챕터를 읽고 CRD와 Operator의 차이를 정리해본다.
3. Operator SDK나 Kubebuilder로 간단한 Operator를 하나 만들어 동작 원리를 체험해본다.
4. Crossplane 공식 문서를 보고 클라우드 리소스를 CRD로 프로비저닝하는 예제를 따라해본다.

## 🔗 참고 자료

- [Kubernetes 공식 문서](https://kubernetes.io) — CRD와 Operator 개념의 기본 원리를 확인할 수 있는 공식 문서 루트
- [Crossplane](https://www.crossplane.io) — CRD/Operator 패턴을 클라우드 인프라 프로비저닝으로 확장한 프로젝트 홈페이지
- [Kyverno](https://kyverno.io) — CRD 기반 정책 엔진 Kyverno의 공식 홈페이지
- [Argo CD 문서](https://argo-cd.readthedocs.io) — GitOps 기반으로 CRD 리소스를 동기화하는 Argo CD 공식 문서
- [CNCF](https://www.cncf.io) — Operator 패턴 관련 프로젝트들을 아우르는 클라우드 네이티브 생태계 재단
