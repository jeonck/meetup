---
title: "2026-11-05 에이전틱 엔지니어링 시대, Platform Engineering은 Context·Execution·Governance로 다시 설계된다"
date: 2026-11-05T03:49:53.498432+09:00
tags: ["platform-engineering", "agentic-ai", "mcp"]
---
## 코드 작성은 더 이상 병목이 아니다

최근 밋업에서 나온 핵심 메시지는 명확했다. "코드를 작성하는 일은 이제 엔지니어링의 병목이 아니다." 실제로 Google의 [2025 DORA 리포트](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/)는 AI 도구 채택률이 90%까지 올라갔고, 처음으로 AI 도입이 소프트웨어 딜리버리 처리량(throughput)과 긍정적으로 연결되었다고 밝힌다. 다만 DORA는 AI를 "증폭기(amplifier)"로 규정한다 — 이미 잘 작동하는 조직의 강점은 더 키우고, 기능 장애가 있는 조직은 그 문제를 더 키운다는 것이다. AI가 코드를 쏟아내는 속도가 빨라질수록, 그것을 안전하게 받아낼 "플랫폼"의 성숙도가 실제 제약 조건이 된다.

## Platform Engineering은 AI-네이티브 시대로 넘어가고 있다

[State of Platform Engineering Volume 4](https://platformengineering.org/reports/state-of-platform-engineering-volume-4) 보고서는 이 흐름을 데이터로 보여준다. 플랫폼 엔지니어링이 클라우드 네이티브 시대를 지나 AI-네이티브 시대로 넘어가고 있다는 것이다. CNCF는 이미 2023년에 [Platform Engineering Maturity Model](https://www.cncf.io/blog/2023/11/20/announcing-the-platform-engineering-maturity-model/)을 발표하면서, 5가지 측면과 4단계 성숙도로 플랫폼을 진단하는 공개 프레임워크를 제시했다. 밋업 발표자가 강조한 Context·Execution·Governance 세 축은 이 CNCF 모델을 에이전트 중심으로 재해석한 실천적 버전에 가깝다 — 플랫폼의 '사용자'가 개발자를 넘어 자율 에이전트로 확장되고 있기 때문이다.

## Context: 조직 지식을 에이전트가 읽을 수 있는 형태로

에이전트가 안전하게 작업하려면 서비스 디스커버리, 의존성, 소유권, 인프라 정보를 스스로 조회할 수 있어야 한다. 이를 표준화하는 인터페이스가 Model Context Protocol(MCP)이다. [MCP 문서](https://modelcontextprotocol.info/docs/)는 MCP를 LLM에 컨텍스트를 제공하는 개방형 프로토콜로 설명하며 "USB-C"에 비유한다. 각 도구가 제각각 연결 방식을 만들 필요 없이 표준 인터페이스 하나로 붙을 수 있다는 뜻이다. 밋업에서 언급된 "모든 SaaS와 모든 내부 도구가 MCP 서버를 배포하고 있다"는 현장 관찰은 이 표준화 흐름이 이미 상당히 진행됐음을 보여준다.

## Execution: 골든 패스를 에이전트가 호출할 수 있게

실행 축은 전통적인 Internal Developer Platform(IDP)의 골든 패스, CI/CD, 임시(ephemeral) 테스트 환경을 사람이 클릭하는 대신 에이전트가 호출(invoke)할 수 있는 형태로 재설계하는 것이다. [CIO Dive의 보도](https://www.ciodive.com/news/enterprises-bet-coding-agents-despite-ROI/830943/)는 기업들이 ROI가 아직 불확실한 상태에서도 코딩 에이전트에 베팅하고 있다고 전한다. 실행 경로가 표준화되지 않은 조직일수록 이런 베팅의 리스크는 커진다 — 에이전트가 수작업 프로세스를 그대로 흉내 내려 하면 확장이 불가능하기 때문이다.

## Governance: 에이전트에게도 신원과 정책이 필요하다

에이전트가 과도한 권한을 갖거나 승인되지 않은 작업을 수행하는 위험은 이미 업계에서 체계적으로 다뤄지고 있다. [OWASP 계열의 Agentic AI/Non-Human Identity 가이드](https://nhimg.org/community/agentic-ai-and-nhis/explore-the-2026-owasp-top-10-for-agentic-identity-solutions/)는 과도한 권한을 가진 비인간 신원(NHI)을 에이전틱 보안의 핵심 리스크로 지목한다. 이를 막는 실무 수단이 policy as code다. [policy-as-code 설명](https://nhimg.org/glossary/policy-as-code-authorization/)에 따르면, 접근 규칙을 버전 관리되는 코드로 정의해 자동으로 테스트·강제함으로써 에이전트가 어떤 조건에서 무엇을 할 수 있는지를 사람이 매번 승인하지 않아도 되게 만든다. Gartner 전망을 인용한 [MIT Sloan Management Review Middle East 보도](https://www.mitsloanme.com/?p=10309)는 2026년 말까지 전체 엔터프라이즈 애플리케이션의 40%에 에이전트가 내장될 것으로 예상하는데, 이 정도 규모에서는 사람이 일일이 리뷰하는 거버넌스가 애초에 성립하지 않는다.

## 실무 조언: 가장 약한 축부터 메워라

세 축 중 하나라도 비어 있으면 나머지 두 축이 이를 보완해주지 못한다. 실무적으로는 조직에서 가장 성숙도가 낮은 축을 먼저 진단하고, API 하나를 만들고 테스트하고 배포하는 단일 워크플로우에서 에이전트가 전 과정을 끝까지 수행할 수 있는지 실험하는 것이 좋은 출발점이다. CNCF의 Platform Engineering Maturity Model과 DORA 리포트는 이미 이런 진단에 쓸 수 있는 공개된 벤치마크를 제공하므로, 사내 체크리스트를 처음부터 새로 만들기보다 이를 참고해 Context, Execution, Governance 각각의 현재 수준을 먼저 측정하는 것이 효율적이다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [How are developers using AI? Inside our 2025 DORA report](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/) — AI 채택률 90%, AI가 딜리버리 처리량과 긍정적으로 연결되었다는 2025년 DORA 리포트 핵심 결과, AI를 '증폭기'로 규정하는 프레이밍의 근거
- [State of Platform Engineering Report: Volume 4](https://platformengineering.org/reports/state-of-platform-engineering-volume-4) — 플랫폼 엔지니어링이 클라우드 네이티브에서 AI-네이티브 시대로 전환하고 있다는 주장의 근거
- [Announcing the Platform Engineering Maturity Model (CNCF)](https://www.cncf.io/blog/2023/11/20/announcing-the-platform-engineering-maturity-model/) — CNCF가 발표한 5가지 측면, 4단계 성숙도 모델의 공식 출처
- [Model Context Protocol documentation](https://modelcontextprotocol.info/docs/) — MCP를 LLM에 컨텍스트를 제공하는 개방형 프로토콜로 설명하는 문서, USB-C 비유의 출처
- [Enterprises bet on coding agents despite ROI uncertainty (CIO Dive)](https://www.ciodive.com/news/enterprises-bet-coding-agents-despite-ROI/830943/) — 기업들이 ROI가 불확실한 상태에서도 코딩 에이전트를 도입 중이라는 실행(Execution) 리스크 논거
- [OWASP Top 10 for Agentic Identity Solutions overview (NHI Mgmt Group)](https://nhimg.org/community/agentic-ai-and-nhis/explore-the-2026-owasp-top-10-for-agentic-identity-solutions/) — 에이전트의 과도한 권한(Non-Human Identity 리스크)을 거버넌스 핵심 위험으로 지목하는 근거
- [Policy-as-code authorization glossary (NHI Mgmt Group)](https://nhimg.org/glossary/policy-as-code-authorization/) — 접근 규칙을 코드로 정의해 자동 테스트·강제하는 policy as code 개념 설명
- [Agentic AI Set to Reshape 40% of Enterprise Applications by 2026 (MIT Sloan Management Review Middle East)](https://www.mitsloanme.com/?p=10309) — 2026년 말까지 엔터프라이즈 애플리케이션 40%에 에이전트가 내장될 것이라는 Gartner 전망 인용 근거
