---
title: "2026-09-23 Microsoft Copilot Studio로 본 기업용 AI 에이전트 도입의 현재와 함정"
date: 2026-09-23T00:09:41.536685+09:00
tags: ["copilot-studio", "ai-agents", "enterprise-ai"]
---
## '한 사람이 다 하지 않는다' — 전문화된 에이전트라는 발상

최근 열린 Microsoft Copilot Studio 실습 밋업에서 강사는 집을 짓는 비유를 들었다. 전기공, 배관공, 목수가 각자의 전문 영역을 맡듯, AI도 하나의 범용 챗봇이 모든 일을 처리하는 대신 특정 업무에 특화된 여러 에이전트가 협업하는 구조로 가야 한다는 것이다. 이는 실제로 Microsoft Copilot Studio가 밀고 있는 방향과 정확히 일치한다. [Microsoft Learn의 멀티에이전트 오케스트레이션 가이드](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/multi-agent-patterns)는 오케스트레이터 에이전트가 사용자 의도를 파악해 라우팅하고, 각 전문 에이전트가 자신의 도메인만 책임지는 패턴을 권장한다. [Microsoft Copilot 블로그](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/multi-agent-orchestration-maker-controls-and-more-microsoft-copilot-studio-announcements-at-microsoft-build-2025/)에 따르면 2025년 Build 행사부터 에이전트 간 통신(A2A)이 정식 기능으로 자리잡았고, 한 에이전트가 다른 에이전트를 호출해 작업을 위임하는 구조가 일반화되고 있다. 이는 조직 단위로 도메인 팀이 각자의 전문 에이전트를 소유·운영하면서도 전체적으로는 하나의 통합된 업무 엔진처럼 작동하게 만드는 거버넌스 모델이기도 하다.

## 노코드 Agent Builder와 지식 소스(Grounding)

밋업에서 참가자들이 직접 만든 '고객지원 에이전트'는 [Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder)를 통해 코드 없이 이름, 설명, 지시문(instructions)만으로 완성됐다. Microsoft Learn은 이 기능을 "자연어로 에이전트를 설명하면 Copilot이 대신 만들어주는" 방식으로 소개한다. 여기서 핵심은 지식 소스(knowledge source)다. [Microsoft Learn의 지식 소스 문서](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio)에 따르면 Copilot Studio는 RAG(검색증강생성)와 시맨틱 인덱싱으로 SharePoint, OneDrive, 공개 웹사이트 등의 콘텐츠를 검색해 답변 근거로 삼고, 실제 답변에는 출처 인용(citation)이 달린다. 밋업 실습에서도 참가자가 업로드한 정책 문서나 공개 URL을 참조해 에이전트가 출처와 함께 답변하는 장면이 나왔는데, 이는 모델의 환각을 줄이고 기업 데이터에 답변을 접지시키는 표준적인 방식이다.

## 좋은 프롬프트의 4요소: Goal-Context-Source-Expectation

강사가 강조한 프롬프트 설계 원칙도 Microsoft 공식 가이드와 일치한다. [Microsoft 365 Copilot 프롬프트 작성 가이드](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot)는 목표(Goal), 맥락(Context), 출처(Source), 기대치(Expectation) 네 요소로 프롬프트를 구성할 것을 권장한다. 무엇을 원하는지, 왜 필요한지, 어떤 자료를 참고해야 하는지, 결과물이 어떤 형태여야 하는지를 명시하면 응답의 정확도와 유용성이 크게 높아진다는 것이다. Prompt Coach 같은 사전 구축 에이전트는 이 프레임워크를 사용자에게 코칭해주는 역할을 하며, [Microsoft 고객지원 문서](https://support.microsoft.com/en-us/microsoft-365-copilot/agents-built-by-microsoft)에서 이런 Microsoft 제작 무료 에이전트 목록을 확인할 수 있다.

## 라이선싱이라는 현실의 벽

실습 중 가장 많은 시간을 잡아먹은 문제는 기술이 아니라 라이선싱이었다. 파일 업로드형 지식 소스는 기본 라이선스로는 막혀 있고, [Azure 가격 페이지](https://azure.microsoft.com/en-us/pricing/details/copilot-studio/)에 따르면 2025년 9월부터 소비 단위가 '메시지'에서 'Copilot Credit'으로 바뀌었으며, 단순 FAQ 응답은 1크레딧이지만 추론 모델 응답은 100크레딧에 달할 수 있다. Pay-as-you-go 방식은 사전 약정 없이 크레딧당 0.01달러로 과금되지만, 이는 관리자가 테넌트 단위로 활성화해야 하는 설정이라 일반 사용자가 즉석에서 켤 수 없다. 이는 곧 조직이 에이전트를 도입하기 전에 라이선스·과금 구조를 먼저 설계해야 한다는 실무적 시사점을 준다.

## 업계 전망: 기대와 현실의 간극

Gartner의 [2026 CIO 서베이](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/)에 따르면 AI 에이전트를 실제 배포한 조직은 17%에 불과하지만 60% 이상이 2년 내 도입을 계획하고 있어, 모든 신기술 중 가장 가파른 도입 곡선을 그리고 있다. 동시에 Gartner는 [2027년까지 에이전틱 AI 프로젝트의 40% 이상이 취소될 것](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)이라고 경고했는데, 원인은 모델 성능이 아니라 비용 관리 실패, 불명확한 비즈니스 가치, 미흡한 거버넌스다. Gartner는 또한 '에이전트 워싱(agent washing)', 즉 기존 챗봇이나 RPA를 에이전트로 재포장해 파는 관행이 만연해 있으며 실제 자율성을 갖춘 벤더는 극소수라고 지적한다. 따라서 기업이 Copilot Studio 같은 플랫폼으로 에이전트를 도입할 때는 화려한 데모보다 명확한 업무 범위 설정, 지식 소스의 신뢰도 검증, 크레딧 소비 예측, 그리고 실제 자율적 의사결정 여부를 냉정하게 따져보는 것이 성공의 관건이다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Official Microsoft Copilot Studio documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/) — Copilot Studio 전반의 공식 문서, 플랫폼 개요 확인
- [Multi-agent orchestration patterns and best practices](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/multi-agent-patterns) — 오케스트레이터-전문 에이전트 패턴과 도메인별 소유 모델 근거
- [Multi-agent orchestration, maker controls and more (Build 2025)](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/multi-agent-orchestration-maker-controls-and-more-microsoft-copilot-studio-announcements-at-microsoft-build-2025/) — 에이전트 간 통신(A2A) 및 연결된 에이전트 기능 발표 확인
- [Agent Builder in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder) — 노코드 Agent Builder의 작동 방식과 템플릿 구조 설명
- [Knowledge sources summary - Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) — RAG 기반 지식 소스 그라운딩 및 인용(citation) 동작 설명
- [Get started writing prompts in Microsoft Copilot](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot) — Goal-Context-Source-Expectation 프롬프트 프레임워크 출처
- [Agents built by Microsoft](https://support.microsoft.com/en-us/microsoft-365-copilot/agents-built-by-microsoft) — Idea Coach, Prompt Coach 등 사전 구축 에이전트 목록 확인
- [Copilot Studio pay as you go pricing](https://azure.microsoft.com/en-us/pricing/details/copilot-studio/) — Copilot Credit 과금 체계와 pay-as-you-go 요금 확인
- [AI Agent Adoption 2026: What the Data Shows](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/) — Gartner 2026 CIO 서베이의 에이전트 배포율(17%) 데이터
- [Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) — 프로젝트 취소 전망과 원인(비용, 가치, 거버넌스), 에이전트 워싱 언급
