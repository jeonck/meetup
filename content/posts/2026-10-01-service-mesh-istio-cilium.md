---
title: "2026-10-01 Service Mesh 입문: Istio와 Cilium으로 보는 마이크로서비스 네트워킹"
date: 2026-10-01T10:02:50.497620+09:00
tags: ["service-mesh", "istio", "cilium", "tech-brief"]
---
## 오늘의 기술 토픽

> **Service Mesh**

이번 밋업은 별도의 발표 전사 없이 Service Mesh를 주제로 정리한 기술 브리프입니다. 마이크로서비스 환경에서 서비스 간 통신을 관리하기 위한 Service Mesh의 개념과, 이를 둘러싼 Istio, Cilium, cert-manager 등 주요 생태계 도구들을 소개합니다. 각 기술이 어떤 문제를 해결하는지와 실제로 학습을 시작하는 방법을 함께 담았습니다.

## 🔑 핵심 요점

- Service Mesh는 서비스 간 통신을 애플리케이션 코드가 아닌 인프라 레이어에서 관리하는 패턴이다.
- 대표적인 구현체로 Istio가 있으며, sidecar 또는 ambient 모드로 트래픽을 제어한다.
- Cilium은 eBPF 기반으로 네트워킹과 보안을 커널 레벨에서 처리해 sidecar 없는 mesh도 가능하게 한다.
- mTLS를 통한 서비스 간 암호화는 Service Mesh의 핵심 보안 기능 중 하나다.
- cert-manager 같은 도구는 mesh 내부 인증서 발급과 갱신을 자동화하는 데 쓰인다.
- 운영 복잡도가 높아 처음에는 작은 범위부터 도입하는 것이 권장된다.

## 🛠 핵심 기술 쉽게 이해하기

### Service Mesh

Service Mesh는 마이크로서비스들이 서로 통신할 때 라우팅, 재시도, 로드밸런싱, 암호화 같은 기능을 애플리케이션 코드 밖에서 처리해주는 인프라 계층입니다. 보통 각 서비스 옆에 proxy를 두거나 커널 레벨에서 트래픽을 가로채는 방식으로 동작합니다.

**왜 필요한가** — 서비스가 많아질수록 통신 관련 로직(재시도, 타임아웃, 인증 등)을 매번 애플리케이션에 구현하기 어려워지는 문제를 해결합니다.

**발표에서는** — 이번 브리프의 핵심 주제로, 마이크로서비스 네트워킹 전반을 이해하기 위한 출발점으로 다뤘습니다.

### Istio

Istio는 가장 널리 쓰이는 Service Mesh 구현체로, Envoy proxy를 기반으로 트래픽 관리, 보안, 관찰성을 제공합니다. 최근에는 sidecar 없이도 동작하는 ambient mesh 모드도 지원합니다.

**왜 필요한가** — 복잡한 트래픽 라우팅 규칙, mTLS 암호화, 세밀한 접근 제어가 필요한 대규모 환경에서 사용됩니다.

**발표에서는** — Service Mesh의 대표 구현체로 함께 소개했습니다.

### Cilium

Cilium은 eBPF 기술을 활용해 쿠버네티스 네트워킹과 보안 정책을 커널 레벨에서 처리하는 CNI(Container Network Interface) 프로젝트입니다. sidecar proxy 없이도 Service Mesh 기능을 제공할 수 있습니다.

**왜 필요한가** — sidecar 기반 mesh의 리소스 오버헤드와 운영 복잡성을 줄이면서도 네트워크 정책, 관찰성, 암호화를 구현하기 위해 쓰입니다.

**발표에서는** — Service Mesh와 밀접한 관련 기술로, eBPF 기반 접근 방식을 대비해 소개했습니다.

### cert-manager

cert-manager는 쿠버네티스 환경에서 TLS 인증서 발급과 갱신을 자동화해주는 도구입니다.

**왜 필요한가** — Service Mesh 내부에서 서비스 간 mTLS 통신을 위해 필요한 인증서 수명주기를 사람이 수동으로 관리하지 않도록 합니다.

**발표에서는** — mesh 내부 보안을 뒷받침하는 보조 도구로 함께 언급했습니다.

## 🧭 추구 방향과 흐름

- **Sidecar에서 Sidecar-less로** — 초기 Service Mesh는 각 pod마다 sidecar proxy를 붙이는 방식이 주류였지만, 리소스 오버헤드와 운영 복잡성 때문에 Cilium의 eBPF 방식이나 Istio ambient mesh처럼 sidecar 없는 아키텍처로 생태계가 이동하고 있습니다.
- **제로 트러스트 네트워킹** — 서비스 간 통신을 기본적으로 암호화하고 인증하는 mTLS가 표준처럼 자리잡으면서, 네트워크 내부도 신뢰하지 않는 제로 트러스트 모델로 나아가는 흐름이 뚜렷합니다.
- **운영 복잡도 관리와 플랫폼화** — Service Mesh 도입 자체가 복잡하기 때문에, 이를 플랫폼 엔지니어링 관점에서 자동화된 정책과 자동 인증서 관리(cert-manager 등)로 감싸 개발자에게는 단순한 셀프서비스 경험을 제공하려는 방향이 강조됩니다.

## 🚀 바로 활용하기

1. 로컬 쿠버네티스 클러스터(minikube, kind 등)에 Istio를 설치하고 공식 Getting Started 가이드의 Bookinfo 예제를 따라 실습해본다.
2. Cilium 공식 문서에서 eBPF 기반 네트워킹 개념을 먼저 읽고, 간단한 클러스터에 설치해 네트워크 정책을 적용해본다.
3. mTLS가 실제로 어떻게 동작하는지 확인하기 위해 cert-manager로 인증서를 발급받아 두 서비스 간 통신에 적용해본다.
4. CNCF 홈페이지에서 Service Mesh 관련 프로젝트들의 성숙도(maturity level)를 비교해본다.

## 🔗 참고 자료

- [Istio 공식 홈페이지](https://istio.io) — Istio의 개념, 아키텍처, 설치 가이드를 확인할 수 있는 공식 문서 루트입니다.
- [Cilium 공식 홈페이지](https://cilium.io) — eBPF 기반 네트워킹 및 sidecar-less mesh 접근 방식을 설명하는 공식 사이트입니다.
- [cert-manager 공식 문서](https://cert-manager.io) — 쿠버네티스 환경에서 TLS 인증서 자동화를 다루는 공식 문서입니다.
- [CNCF 홈페이지](https://www.cncf.io) — Service Mesh 관련 프로젝트들의 생태계와 성숙도를 확인할 수 있는 재단 사이트입니다.
- [Kubernetes 공식 문서](https://kubernetes.io) — Service Mesh가 동작하는 기반 플랫폼인 쿠버네티스의 공식 문서입니다.
