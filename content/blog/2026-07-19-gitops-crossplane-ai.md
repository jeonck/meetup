---
title: "2026-07-19 플랫폼 엔지니어링의 다음 단계: GitOps, Crossplane, 그리고 AI 에이전트가 만드는 셀프서비스 플랫폼"
date: 2026-07-19T08:34:05.391281+09:00
tags: ["platform-engineering", "gitops", "crossplane"]
---
## DevOps 다음은 왜 플랫폼 엔지니어링인가

DevOps는 애플리케이션 팀에게 인프라를 직접 다룰 자유를 줬지만, 그 대가로 모든 팀이 YAML과 IAM, 네트워크 정책을 각자 재발명하는 '인지 부하 폭증'을 낳았다. 이 문제를 해결하기 위해 등장한 것이 플랫폼 엔지니어링이다. CNCF는 이를 "플랫폼 팀이 제공하는 능력의 계층으로, 제품 팀이 하부 인프라에 대한 깊은 전문성 없이도 서비스를 빌드·배포·운영할 수 있게 하는 것"이라 정의하며, 골든 패스(Golden Path)를 "가드레일이지 게이트가 아니다"라고 못박는다 ([CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)). 실제로 [DORA의 2025 State of AI-assisted Software Development 보고서](https://dora.dev/dora-report-2025/)에 따르면 조직의 90%가 내부 개발자 플랫폼(IDP)을 이미 운영 중이고 76%는 전담 플랫폼 팀을 두고 있다. 더 중요한 발견은, AI 도입률이 90%에 달하는 지금 AI는 그 조직의 기존 엔지니어링 시스템을 '증폭'할 뿐이라는 점이다. 플랫폼이 부실하면 AI도 그 부실함을 그대로 증폭시킨다.

## Git을 단일 진실 공급원으로: GitOps

플랫폼을 안전하게 운영하려면 '무엇이 배포되어 있는가'에 대한 감사 가능한 기록이 필요하다. CNCF 산하 OpenGitOps 이니셔티브는 GitOps의 네 가지 원칙으로 선언적 정의, 버전 관리와 불변성, Git을 통한 자동 배포(Pull), 지속적 조정(Reconciliation)을 제시한다. Argo CD는 이 모델을 구현한 CNCF Graduated 프로젝트로, 클러스터 내부에서 컨트롤러로 동작하며 Git의 선언 상태와 실제 클러스터 상태를 지속적으로 비교해 드리프트를 감지하고 되돌린다 ([Argo CD GitHub](https://github.com/argoproj/argo-cd)). 즉 인프라 변경도 코드 리뷰와 동일한 PR 승인 절차를 거치게 되어, '누가 무엇을 언제 바꿨는지' 자체가 감사 로그가 된다.

## Kubernetes를 클라우드 전체의 제어 평면으로: Crossplane

애플리케이션 배포에는 GitOps가 표준이 됐지만, 클라우드 인프라(RDS, VPC, IAM 등) 프로비저닝은 여전히 별도 도구가 필요한 경우가 많았다. Crossplane은 Kubernetes의 CRD와 컨트롤러 패턴을 확장해 RDS 인스턴스부터 IAM 역할까지 임의의 클라우드 리소스를 Kubernetes API로 선언·관리하게 해주는 CNCF 프로젝트다 ([crossplane.io](https://www.crossplane.io/)). 플랫폼 팀은 여러 개별 리소스를 하나의 'Composition'으로 묶어 애플리케이션 팀에게는 "클러스터 하나 주세요" 같은 단순한 API만 노출할 수 있다. Terraform과 달리 Crossplane은 클러스터 내부에서 지속적으로 상태를 조정(reconcile)하므로 GitOps와 자연스럽게 맞물린다.

## 제로 트러스트와 정책의 자동 강제

플랫폼이 셀프서비스를 제공하는 만큼 보안은 사람이 아니라 정책 엔진이 담당해야 한다. eBPF 기반 CNI인 Cilium은 2023년 CNCF Graduated 등급을 받았으며, IP·포트 기반이 아니라 워크로드의 신원(서비스 어카운트, 레이블)에 기반해 통신을 인가하는 방식으로 제로 트러스트 네트워킹을 구현한다 ([Cilium Zero Trust](https://cilium.io/outcomes/zero-trust/)). 여기에 Kyverno 같은 정책 엔진을 더하면, 정책에 어긋나는 워크로드는 클러스터에 진입하기도 전에 거부된다 — 즉 보안 검토가 배포 이후가 아니라 배포 이전 단계로 '시프트 레프트'된다.

## AI 에이전트, 플랫폼의 새로운 인터페이스

최근 흐름은 이 모든 플랫폼 구성 요소를 자연어로 다루게 만드는 것이다. Solo.io가 만들고 현재 CNCF Sandbox 프로젝트인 kagent는 Kubernetes 클러스터 안에서 직접 AI 에이전트를 배포·운영하는 프레임워크로, MCP(Model Context Protocol)와 Agent-to-Agent 통신을 지원해 로그·메트릭을 조회하고 장애를 진단하는 작업을 자연어 채팅으로 처리할 수 있게 한다 ([CNCF: Kagent 소개](https://www.cncf.io/blog/2025/04/15/kagent-bringing-agentic-ai-to-cloud-native/)). 다만 DORA 보고서가 지적하듯 AI 에이전트 역시 플랫폼이라는 기반이 견고할 때만 신뢰할 수 있는 결과를 낸다.

## 실무 도입 조언

플랫폼을 도입할 때는 (1) 골든 패스를 먼저 문서화하고 CLI/API로 노출하는 것부터 시작하고, (2) GitOps로 애플리케이션과 인프라 변경 이력을 모두 Git에 남기며, (3) 정책 엔진으로 보안 가드레일을 코드화한 뒤, (4) AI 에이전트는 가장 마지막에 '이미 신뢰할 수 있는 플랫폼 위의 인터페이스'로 얹는 순서를 권한다. 순서를 거꾸로 하면, 즉 기반 없이 AI부터 얹으면 조직의 기존 무질서만 자동화되어 확대될 위험이 크다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [DORA | State of AI-assisted Software Development 2025](https://dora.dev/dora-report-2025/) — IDP 도입률 90%, 플랫폼 팀 보유율 76%, AI가 기존 엔지니어링 시스템 품질을 증폭한다는 근거
- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — 내부 개발자 플랫폼과 골든 패스의 공식 정의, '가드레일이지 게이트가 아니다'라는 원칙의 출처
- [What is platform engineering? | CNCF](https://www.cncf.io/blog/2025/11/19/what-is-platform-engineering/) — 플랫폼 엔지니어링을 사람·프로세스·정책·기술을 포괄하는 실천으로 규정하는 CNCF 공식 설명
- [Argo CD GitHub (argoproj/argo-cd)](https://github.com/argoproj/argo-cd) — Argo CD가 CNCF Graduated 프로젝트이며 Git과 클러스터 상태를 지속 비교/조정한다는 근거
- [Crossplane 공식 사이트](https://www.crossplane.io/) — Crossplane이 Kubernetes CRD/컨트롤러로 클라우드 인프라 전체를 제어 평면화한다는 근거
- [Cilium Zero Trust Networking](https://cilium.io/outcomes/zero-trust/) — Cilium이 eBPF와 워크로드 신원 기반 정책으로 제로 트러스트를 구현한다는 근거
- [CNCF: Kagent, Bringing Agentic AI to Cloud Native](https://www.cncf.io/blog/2025/04/15/kagent-bringing-agentic-ai-to-cloud-native/) — kagent가 Solo.io 기원의 CNCF Sandbox 프로젝트이며 MCP/A2A를 지원한다는 근거
- [GitHub cncf/sandbox Issue #360 (kagent)](https://github.com/cncf/sandbox/issues/360) — kagent의 CNCF Sandbox 편입 심사 및 프로젝트 개요
