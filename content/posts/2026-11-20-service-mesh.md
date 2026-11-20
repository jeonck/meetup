---
title: "2026-11-20 Service Mesh 입문: 왜 필요하고 어디로 가는가"
date: 2026-11-20T11:49:28.234928+09:00
tags: ["service-mesh", "kubernetes", "cilium", "tech-brief"]
---
## 오늘의 기술 토픽

> **Service Mesh**

이번 글은 실제 밋업 발표 녹취록 대신, Service Mesh라는 주제를 중심으로 핵심 개념과 생태계 흐름을 정리한 브리핑입니다. 마이크로서비스 환경에서 서비스 간 통신을 어떻게 안전하고 관찰 가능하게 만드는지, Istio와 Cilium 같은 대표 구현체가 어떤 차이를 보이는지 짚습니다. 최근에는 sidecar 없이 동작하는 ambient mesh 방식과 eBPF 기반 네트워킹이 주목받고 있다는 점도 함께 설명합니다.

## 🔑 핵심 요점

- Service Mesh는 마이크로서비스 간 통신에 트래픽 제어, 보안, 관찰성 기능을 애플리케이션 코드 수정 없이 추가해주는 인프라 계층입니다.
- 전통적인 Service Mesh는 각 Pod마다 sidecar proxy(Envoy)를 붙여 트래픽을 가로채는 방식으로 동작합니다.
- Istio는 가장 널리 쓰이는 Service Mesh 구현체로, 트래픽 라우팅·mTLS·관찰성 기능을 제공합니다.
- Cilium은 eBPF 기술을 활용해 sidecar 없이도 Service Mesh 기능을 구현하는 ambient mesh 방식을 지원합니다.
- sidecar 방식은 리소스 오버헤드와 운영 복잡도가 크다는 점이 꾸준히 지적되어 왔습니다.
- Gateway API는 Kubernetes 생태계에서 Ingress를 대체할 표준 트래픽 관리 API로 자리잡고 있습니다.

## 🛠 핵심 기술 쉽게 이해하기

### Service Mesh

Service Mesh는 마이크로서비스들이 서로 통신할 때 거치는 네트워크 계층으로, 서비스 코드를 건드리지 않고 트래픽 제어, 암호화, 모니터링 기능을 추가해줍니다. 보통 proxy를 통해 모든 서비스 간 트래픽을 가로채서 처리합니다.

**왜 필요한가** — 서비스 개수가 많아질수록 재시도, 타임아웃, 인증, 로깅 같은 공통 로직을 각 서비스마다 구현하기 어려워지는데, Service Mesh는 이를 인프라 레벨에서 일괄 처리합니다.

**발표에서는** — 전체 주제의 중심 개념으로, 이어지는 Istio와 Cilium 설명의 전제가 되는 개념입니다.

### Istio

Istio는 가장 대표적인 Service Mesh 오픈소스 프로젝트로, 각 Pod에 Envoy proxy를 sidecar로 배치해 트래픽을 제어합니다. 트래픽 분할, 재시도, 서비스 간 암호화(mTLS), 상세한 관찰성 지표를 제공합니다.

**왜 필요한가** — 복잡한 트래픽 라우팅 규칙과 보안 정책을 코드 변경 없이 선언적으로 적용하기 위해 사용합니다.

**발표에서는** — 전통적인 sidecar 기반 Service Mesh의 대표 사례로 다뤄집니다.

### Cilium

Cilium은 원래 eBPF 기반 CNI(네트워크 플러그인)이지만, 최근에는 sidecar 없이 커널 레벨에서 동작하는 ambient-style Service Mesh 기능까지 제공합니다.

**왜 필요한가** — sidecar proxy의 리소스 오버헤드와 운영 복잡도를 줄이면서도 Service Mesh의 핵심 기능을 유지하기 위해 쓰입니다.

**발표에서는** — sidecar 없는 차세대 Service Mesh 접근법의 사례로 소개됩니다.

### Envoy

Envoy는 고성능 L7 proxy로, Istio를 비롯한 여러 Service Mesh 구현체에서 데이터 플레인 역할을 담당합니다.

**왜 필요한가** — 서비스 간 트래픽을 실제로 가로채고 라우팅·로드밸런싱·관찰성 데이터를 수집하는 핵심 컴포넌트가 필요하기 때문입니다.

**발표에서는** — Istio의 기반 기술로 함께 언급됩니다.

## 🧭 추구 방향과 흐름

- **Sidecar에서 Sidecarless로** — 기존 Service Mesh는 Pod마다 sidecar proxy를 붙이는 방식이 표준이었지만, 리소스 오버헤드와 운영 복잡도 문제로 sidecar 없이 동작하는 ambient mesh 방식이 떠오르고 있습니다. Cilium의 eBPF 기반 접근이 대표적인 사례입니다.
- **eBPF 기반 네트워킹 확산** — 커널 레벨에서 직접 패킷을 처리하는 eBPF 기술이 CNI뿐 아니라 Service Mesh 영역까지 확장되면서, proxy 오버헤드를 줄이려는 흐름이 강해지고 있습니다.
- **표준 API로의 수렴** — Kubernetes의 Gateway API가 다양한 Mesh/Ingress 구현체 사이의 공통 인터페이스로 자리잡으면서, 특정 벤더나 프로젝트에 종속되지 않는 트래픽 관리가 가능해지는 방향으로 가고 있습니다.

## 🚀 바로 활용하기

1. 로컬 Kubernetes 클러스터(kind, minikube 등)에 istioctl로 Istio를 설치하고 demo 프로파일로 bookinfo 예제 앱을 배포해보세요.
2. Cilium 공식 문서에서 Service Mesh / ambient mode 섹션을 읽고 sidecar 방식과의 차이를 직접 비교해보세요.
3. Kubernetes Gateway API 문서를 읽고 기존 Ingress 리소스와 어떤 점이 다른지 정리해보세요.
4. Istio의 mTLS와 트래픽 라우팅(VirtualService, DestinationRule) 예제를 따라 하며 기본 개념을 체득해보세요.

## 🔗 참고 자료

- [Istio](https://istio.io) — 대표적인 sidecar 기반 Service Mesh 구현체의 공식 문서
- [Cilium](https://cilium.io) — eBPF 기반 CNI 및 sidecarless Service Mesh 기능 제공
- [Envoy Proxy](https://www.envoyproxy.io) — Istio 등에서 데이터 플레인으로 쓰이는 L7 proxy
- [Linkerd](https://linkerd.io) — 경량 Service Mesh 구현체로 비교 참고용
- [Kubernetes](https://kubernetes.io) — Service Mesh와 Gateway API가 동작하는 기반 플랫폼 공식 문서
- [CNCF](https://www.cncf.io) — Istio, Envoy, Cilium 등 관련 프로젝트들이 속한 재단
