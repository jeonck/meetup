---
title: "2026-10-24 AI 에이전트 시대의 SecOps: Defender XDR·Sentinel·KQL로 그리는 통합 위협 대응 전략"
date: 2026-10-24T01:16:47.940995+09:00
tags: ["microsoft-sentinel", "ai-agent-security", "kql-threat-hunting"]
---
## AI 에이전트가 새로운 공격 표면이 되는 이유

클라우드 보안 사고는 여전히 ID 중심 공격, 즉 비밀번호 스프레이나 토큰·세션 도용이 주된 침해 경로다. 여기에 AI 에이전트가 더해지면서 공격 표면이 한층 넓어졌다. OWASP는 2026년판 LLM Top 10에서도 [prompt injection을 3년 연속 1위](https://sdtimes.com/security/prompt-injection-tops-2026-owasp-genai-llm-top-ten-vulnerabilities/)로 꼽았고, 민감정보 유출과 과도한 권한(excessive agency)이 그 뒤를 잇는다. OWASP GenAI Security Project 공동의장 Steve Wilson은 prompt injection을 완전히 제거할 엔지니어링 해법은 없다고 말하며, 이를 '제거할 취약점'이 아니라 '지속적으로 관리할 운영 리스크'로 봐야 한다고 강조한다. 간접 주입은 검색된 문서, 오염된 도구 응답, 과거 세션의 메모리 등 다양한 경로로 들어올 수 있다는 점도 실무적으로 중요하다.

## Sentinel과 Defender XDR의 수렴

Microsoft는 SIEM인 Sentinel과 XDR인 Defender XDR을 하나의 Defender 포털로 통합하고 있다. [Microsoft Learn 문서](https://learn.microsoft.com/unified-secops-platform/overview-unified-security)에 따르면 이 포털은 SIEM, SOAR, XDR, 노출 관리, 생성형 AI를 한 곳에서 제공해 엔드포인트·ID·이메일·SaaS 전 영역의 알럿과 엔티티를 하나의 인시던트로 묶어준다. 특히 [Azure 포털에서의 Sentinel 관리 기능은 2027년 3월 31일에 종료](https://learn.microsoft.com/unified-secops/whats-new)되며 이후에는 Defender 포털로 완전히 이전된다. 마이그레이션 시 레거시 Fusion 엔진이 비활성화될 수 있어 알럿 튜닝과 상관분석 로직을 사전에 재검증해야 한다.

## KQL과 ASIM: 가설 기반 헌팅의 기반

[Advanced Hunting](https://learn.microsoft.com/defender-xdr/advanced-hunting-overview)은 최대 30일치 원시 데이터를 KQL로 직접 조회하는 기능이며, 로그인 실패/성공 패턴, `schtasks.exe` 같은 영속성 기법, Defender와 Sentinel 간 ID 상관분석 등 가설 기반 쿼리를 작성하는 데 쓰인다. 이때 서로 다른 로그 소스를 하나의 스키마로 맞춰주는 것이 [ASIM(Advanced Security Information Model)](https://learn.microsoft.com/azure/sentinel/normalization-content)이다. ASIM은 OSSEM 모델을 따르는 KQL 기반 파서로 쿼리 시점에 데이터를 정규화해, 방화벽·ID 공급자·엔드포인트 등 서로 다른 제품에 대해서도 하나의 탐지 규칙을 재사용할 수 있게 한다. 효과적인 쿼리는 이후 커스텀 탐지 규칙으로 전환해 자동화할 수 있다.

## AI 에이전트 전용 ID: Entra Agent ID와 Agent 365

AI 에이전트는 사람이나 앱과는 다른 신뢰 모델이 필요하다. [Microsoft Entra Agent ID](https://learn.microsoft.com/entra/agent-id)는 에이전트에 자체 자격증명이 없는 '에이전트 ID'를 부여하고, 이를 템플릿 역할의 'blueprint'가 발급한 토큰으로 인증시킨다. blueprint 단위로 조건부 접근 정책을 적용하므로 신뢰 영역이 다른 에이전트는 별도 blueprint로 분리해 블래스트 레이디어스를 줄이는 설계가 권장된다. 세션 단위로 생성·삭제되는 ephemeral 에이전트 ID도 지원된다. 이 위에서 동작하는 [Microsoft Agent 365](https://www.daymarksi.com/blog/microsoft-agent-365-bringing-identity-governance-and-security-to-ai-agents)는 에이전트를 사용자·앱과 동등한 1급 엔터프라이즈 주체로 다루며, 인벤토리 등록·최소 권한 기반 역할 접근·Purview 데이터 거버넌스·Defender 위협 탐지를 하나의 거버넌스 레이어로 묶는다.

## 실무 적용 조언

Sentinel을 쓰고 있다면 2027년 3월 전까지 Defender 포털 전환 계획을 세우고 Fusion 기반 규칙을 KQL 커스텀 탐지로 재작성해야 한다. 새로 AI 에이전트를 도입한다면 설계 단계부터 신원 소유자·권한 범위·데이터 접근 범위를 명시하고, Entra Agent ID의 blueprint 분리 패턴으로 신뢰 영역을 나누는 것이 바람직하다. 탐지 측면에서는 prompt injection을 완전히 막기보다, 실행 결과를 지속적으로 관측(observability)하고 과도한 권한 행사를 탐지하는 쪽에 투자하는 것이 OWASP의 권고와도 부합한다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Microsoft Learn - What's new in unified security operations](https://learn.microsoft.com/unified-secops/whats-new) — Sentinel의 Azure 포털 관리 기능이 2027년 3월 31일 종료되고 Defender 포털로 통합된다는 근거
- [Microsoft Learn - Overview of unified security operations platform](https://learn.microsoft.com/unified-secops-platform/overview-unified-security) — Defender 포털이 SIEM·SOAR·XDR·노출관리·생성형 AI를 통합 제공한다는 근거
- [Microsoft Learn - Advanced hunting overview](https://learn.microsoft.com/defender-xdr/advanced-hunting-overview) — KQL 기반 Advanced Hunting이 최대 30일 원시 데이터 조회 및 커스텀 탐지 전환을 지원한다는 근거
- [Microsoft Learn - ASIM security content](https://learn.microsoft.com/azure/sentinel/normalization-content) — ASIM이 다양한 로그 소스를 하나의 스키마로 정규화해 탐지 규칙 재사용을 가능케 한다는 근거
- [Microsoft Learn - Microsoft Entra Agent ID key concepts](https://learn.microsoft.com/entra/agent-id/key-concepts) — 에이전트 ID와 blueprint의 인증 구조, ephemeral 에이전트 ID 설계 패턴 근거
- [Daymark - Microsoft Agent 365 bringing identity governance and security to AI agents](https://www.daymarksi.com/blog/microsoft-agent-365-bringing-identity-governance-and-security-to-ai-agents) — Agent 365가 에이전트를 1급 엔터프라이즈 주체로 다루며 거버넌스 레이어를 구성한다는 설명 근거
- [SD Times - Prompt Injection tops 2026 OWASP GenAI/LLM Top Ten](https://sdtimes.com/security/prompt-injection-tops-2026-owasp-genai-llm-top-ten-vulnerabilities/) — OWASP 2026 LLM Top 10에서 prompt injection이 3년 연속 1위이며 excessive agency가 상승했다는 근거
- [Software Seni - Prompt injection in production: the 2026 state of the industrial AI attack](https://www.softwareseni.com/prompt-injection-in-production-the-2026-state-of-the-industrial-ai-attack) — 간접 prompt injection이 검색 문서·도구 응답·메모리 등 다양한 경로로 유입된다는 배경 설명
