---
title: "2026-10-24 Agentic AI 시대의 보안: Microsoft Defender와 Sentinel은 AI 에이전트를 어떻게 지키는가"
date: 2026-10-24T01:14:51.686923+09:00
tags: ["agentic-ai-security", "microsoft-sentinel", "defender-for-cloud"]
---
## Agentic AI가 몰고 온 새로운 공격 표면

챗봇을 넘어 스스로 계획하고 도구를 호출하며 다른 에이전트와 협업하는 'agentic AI'가 기업 워크플로의 중심으로 들어오면서, 보안 업계의 화두도 '모델 안전성'에서 '에이전트 행위 보안'으로 옮겨가고 있다. 에이전트는 자율적으로 코드를 실행하고 API를 호출하며 다른 에이전트와 통신하기 때문에, 전통적인 애플리케이션 보안 모델로는 포착하기 어려운 위험을 만든다.

## OWASP가 정의한 에이전트형 AI의 10대 위협

2025년 12월, OWASP GenAI Security Project는 100명이 넘는 보안 연구자와 NIST, 유럽연합 집행위원회, Alan Turing Institute 등이 참여한 검토를 거쳐 [Agentic AI를 위한 Top 10 위험·대응 가이드](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/)를 발표했다. Agent Goal Hijacking(목표 탈취), Tool Misuse(도구 오남용), Identity & Privilege Abuse(권한 남용)를 핵심 위협으로 꼽았는데, 이는 에이전트가 '제한된 인간 개입만으로 직접 행동하고 다른 에이전트와 조율한다'는 특성에서 비롯된다. 즉 프롬프트 자체보다 에이전트가 실행하는 행위와 그 행위에 부여된 권한을 통제하는 것이 핵심 과제가 된 것이다.

## Defender: 런타임에서 AI 워크로드를 감시하다

Microsoft는 이런 위협에 대응해 Defender for Cloud에 [AI threat protection](https://learn.microsoft.com/en-ca/azure/defender-for-cloud/ai-threat-protection) 기능을 추가했다. Azure AI Content Safety의 Prompt Shields와 위협 인텔리전스를 결합해 데이터 유출, 데이터 포이즈닝, 탈옥(jailbreak), 자격 증명 탈취 같은 시도를 실시간으로 탐지하고, 가상머신·컨테이너·관리형 AI 서비스의 런타임 신호를 지속적으로 분석한다. [Petri의 보도](https://petri.com/microsoft-defender-for-cloud-ai-threat-protection/)에 따르면 이 탐지 결과는 Defender XDR 포털로 통합돼, 보안팀이 AI 워크로드 경고를 기존 알림과 한 화면에서 관리할 수 있다.

## Sentinel과 Security Copilot: SOC 자체가 에이전트화된다

더 큰 흐름은 SIEM 자체가 에이전트 기반으로 재편되는 것이다. [The Hacker News](https://thehackernews.com/2025/09/microsoft-expands-sentinel-into-agentic.html)와 [Redmond Magazine](https://redmondmag.com/articles/2026/09/23/microsoft-brings-sentinel-and-defender-together-for-agentic-security-operations.aspx)의 보도를 보면, Microsoft는 Sentinel의 통합 데이터 레이크를 기반으로 피싱 트리아지, 사고 우선순위화, 플레이북 생성을 수행하는 전담 에이전트들을 선보이고 있다. [Cloud Wars](https://cloudwars.com/ai/with-agentic-ai-infusion-microsoft-positions-sentinel-as-unifying-security-platform/)는 이를 'Project Perception'이라는 멀티에이전트 체계로 설명하는데, 조사·정찰·공격 시뮬레이션·보안 태세 평가를 각기 다른 에이전트가 맡고 인간은 최종 봉쇄 결정만 내리는 구조다. 핵심은 통합된 데이터 기반 없이는 AI 에이전트가 제대로 작동할 수 없다는 전제이며, 이는 결국 조직의 로그·자산 데이터 품질이 Agentic SOC 성패를 좌우한다는 뜻이다.

## Entra Agent ID: 에이전트에게도 신원이 필요하다

행위를 통제하려면 먼저 '누가' 그 행위를 했는지 식별해야 한다. Microsoft는 [Entra Agent ID](https://learn.microsoft.com/en-za/entra/agent-id/whats-new-agent-id) 문서에서, 에이전트가 자체 자격 증명 없이 'agent identity blueprint'가 발급한 토큰으로 인증하며, 사용자·워크로드와 동일하게 조건부 액세스, 실시간 위험 탐지, 생명주기 관리 대상이 된다고 설명한다. OAuth 2.0, MCP, A2A 같은 표준 프로토콜을 지원해 에이전트 간 통신까지 거버넌스 범위에 포함시킨 점이 특징이다.

## 실무 도입을 위한 조언

정리하면 방향은 분명하다. 모델 안전성만으로는 부족하고, ①에이전트의 신원과 권한을 명시적으로 관리하고 ②에이전트의 도구 호출·행위를 런타임에서 모니터링하며 ③SOC 운영 자체를 에이전트로 보강해 탐지·대응 속도를 높이는 세 축이 함께 움직여야 한다. 다만 다수의 기능이 아직 preview 단계이므로, 도입 전 공식 문서에서 GA 여부를 확인하고, 벤더 보고서의 성능 수치는 참고치로만 받아들이는 신중함이 필요하다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [OWASP GenAI Security Project – Top 10 for Agentic AI Security](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/) — 에이전트형 AI의 10대 위협(목표 탈취, 도구 오남용, 권한 남용 등) 정의의 근거
- [Microsoft Learn – AI threat protection in Defender for Cloud](https://learn.microsoft.com/en-ca/azure/defender-for-cloud/ai-threat-protection) — Defender for Cloud의 AI 워크로드 런타임 탐지 기능 설명 근거
- [Petri – Microsoft Defender for Cloud AI Threat Protection](https://petri.com/microsoft-defender-for-cloud-ai-threat-protection/) — Defender XDR 통합 및 실시간 보호 보도
- [The Hacker News – Microsoft expands Sentinel into agentic](https://thehackernews.com/2025/09/microsoft-expands-sentinel-into-agentic.html) — Sentinel의 에이전트 기반 SOC 확장 발표 보도
- [Redmond Magazine – Microsoft brings Sentinel and Defender together for agentic security operations](https://redmondmag.com/articles/2026/09/23/microsoft-brings-sentinel-and-defender-together-for-agentic-security-operations.aspx) — Sentinel·Defender 통합과 Agentic SOC 전환 흐름 근거
- [Cloud Wars – With agentic AI infusion, Microsoft positions Sentinel as unifying security platform](https://cloudwars.com/ai/with-agentic-ai-infusion-microsoft-positions-sentinel-as-unifying-security-platform/) — Project Perception 멀티에이전트 구조 설명 근거
- [Microsoft Learn – What's new in Entra Agent ID](https://learn.microsoft.com/en-za/entra/agent-id/whats-new-agent-id) — 에이전트 신원·권한 관리 프레임워크(Entra Agent ID) 설명 근거
