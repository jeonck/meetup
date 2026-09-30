---
title: "2026-09-30 AI가 QA를 대체하는 게 아니라 QA의 정의를 바꾼다: Agentic Testing과 Risk-Based 자동화의 현재"
date: 2026-09-30T09:54:03.784994+09:00
tags: ["agentic-ai", "software-testing", "qa-automation"]
---
## 테스트 스크립트 생성 그 다음: Agentic QA의 등장

최근 미팅업에서 오간 논쟁의 핵심은 "AI가 테스트 스크립트를 대신 써주는 것"과 "AI가 QA 업무 자체를 재정의하는 것"이 전혀 다른 이야기라는 점이었다. 업계는 이미 이 전환을 용어로도 구분하고 있다. [Katalon](https://katalon.com/resources-center/blog/what-is-agentic-qa-the-complete-guide-for-2026)은 Agentic QA를 "에이전트가 테스트 스크립트가 아니라 제품의 의도(intent)를 쥐고, 무엇을 검증할지 스스로 계획·실행·관찰·적응하는 목표 지향적 루프"로 정의한다. 즉 QA 엔지니어의 역할이 "스텝을 작성하는 일"에서 "품질이 무엇인지 정의하는 일"로 옮겨간다는 것이다. 실제로 [Forrester는 2025년 테스트 플랫폼 카테고리 명칭을 'Continuous Automation Testing Platforms'에서 'Autonomous Testing Platforms'로 변경](https://www.forrester.com/report/the-autonomous-testing-platforms-landscape-q3-2025/RES185162)했고, [Gartner는 2026년 말까지 전체 엔터프라이즈 애플리케이션의 40%가 태스크 특화 AI 에이전트를 탑재할 것으로 전망](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)했다. 2025년 기준 5% 미만이었던 수치가 1년 만에 8배 뛰는 셈이다.

## Shift-Left와 Self-Healing: 코드가 나오기 전에 테스트를 준비한다

Shift-left는 새로운 개념은 아니다. [GitHub의 정리](https://github.com/resources/articles/what-is-shift-left-testing)에 따르면 핵심은 "결함을 늦게 발견할수록 수정 비용이 커지므로 테스트 활동을 SDLC 초기로 앞당긴다"는 것이다. 다만 최근 달라진 점은 Figma 목업이나 API 스펙만으로 로케이터 없이도 자동화 스크립트를 미리 작성할 수 있는 도구들이 등장했다는 점이다. 이 흐름을 뒷받침하는 기술이 self-healing 테스트 자동화다. UI 요소가 이동하거나 라벨이 바뀌어도 AI가 과거 실행 이력과 시각적 패턴을 대조해 로케이터를 스스로 갱신한다. 다만 [QA Wolf의 분석](https://www.qawolf.com/blog/self-healing-test-automation-types)은 중요한 한계를 짚는다. 셀렉터 교체만으로 해결되는 실패는 전체 테스트 실패의 28%에 불과하며, 나머지는 타이밍 이슈, 유효하지 않은 테스트 데이터, 런타임 오류, 시각적 변화 등에서 발생한다는 것이다. 즉 self-healing을 "만능 유지보수 해결사"로 오해하면 오히려 잘못된 요소에 매칭하는 오탐이 늘어날 수 있다.

## 커버리지보다 리스크: 결함 이력 기반 테스트 생성

미팅업에서 나온 "테스트 케이스 2000개가 있어도 버그가 100개씩 나온다"는 경험담은 업계 전반의 공통된 문제의식이기도 하다. AI 테스트 생성 도구들은 단순히 요구사항 문서를 테스트로 변환하는 단계를 넘어, [코드 변경 이력·과거 결함 패턴·실행 로그를 학습해 결함 발생 가능성이 높은 영역에 테스트를 집중시키는 리스크 기반 우선순위화](https://medium.com/@sermineldek/ai-powered-risk-based-test-automation-for-optimizing-testing-processes-e3930f11459b)로 이동하고 있다. 이는 발표자가 강조한 "AI가 버그 백로그와 PR 변경 이력을 보고 어떤 메서드가 반복적으로 결함을 일으키는지 학습해야 한다"는 접근과 정확히 일치한다. 다만 모든 자료가 공통으로 지적하듯, 결함 위험 점수와 자동 생성된 테스트 케이스에는 여전히 사람의 검토가 필요하다. Katalon도 "에이전트는 제안하고 보조하는 역할에서 시작해야 하며, 테스트 범위·리스크 승인·결함 심각도 판단 같은 핵심 결정은 반드시 사람이 검토해야 한다"는 human-in-the-loop 거버넌스 모델을 강조한다.

## ROI는 '활동'이 아니라 '성과'로 증명해야 한다

경영진 앞에서 AI 도입 성과를 증명해야 하는 QA 리더들에게 가장 실질적인 조언은 측정 지표를 바꾸라는 것이다. [SD Times의 분석](https://sdtimes.com/ai/measuring-ai-roi-through-business-outcomes/)에 따르면 79%의 경영진이 AI로 생산성 향상을 체감하면서도 실제 ROI를 자신 있게 측정할 수 있는 비율은 29%에 불과하다. 원인은 명확하다. 생성된 테스트 케이스 수, 프롬프트 사용량, AI 상호작용 횟수 같은 '활동 지표'는 이사회의 관심사가 아니다. 대신 릴리스 주기 단축, 프로덕션 결함 감소, 규제 리스크 완화, 고객 만족도 같은 '비즈니스 성과 지표'로 전환해야 한다는 것이 공통된 결론이다. 특히 토큰 비용이나 라이선스 비용만 계산하는 ROI 산식은 사람의 검토 시간, 거버넌스, 인프라 통합 비용을 누락해 투자 대비 효과를 과대평가하기 쉽다는 지적도 나온다.

## 정리

AI 테스팅의 다음 단계는 "스크립트를 더 빨리 쓰는 것"이 아니라 QA의 역할 자체를 리스크 분석과 전략 설계로 재배치하는 것이다. 다만 self-healing의 28% 한계, 결함 예측의 정확도, ROI 측정의 모호함이 보여주듯 현재의 agentic testing 도구들은 여전히 사람의 검증을 전제로 설계돼 있다. 도입을 고려하는 조직이라면 도구 자체보다 '어디에 사람의 판단을 남길 것인가'를 먼저 설계하는 편이 안전하다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [QA trends for 2026: AI, agents, and the future of testing](https://www.tricentis.com/blog/qa-trends-ai-agentic-testing) — Agentic testing이 record-and-replay 모델을 대체하는 흐름을 설명
- [What Is Agentic QA? | The Complete Guide for 2026 (Katalon)](https://katalon.com/resources-center/blog/what-is-agentic-qa-the-complete-guide-for-2026) — Agentic QA의 정의와 human-in-the-loop 거버넌스 모델 근거
- [Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) — 엔터프라이즈 앱 내 AI 에이전트 채택률 통계 인용
- [The Autonomous Testing Platforms Landscape, Q3 2025 (Forrester)](https://www.forrester.com/report/the-autonomous-testing-platforms-landscape-q3-2025/RES185162) — Forrester가 테스트 도구 카테고리를 'Autonomous Testing'으로 재명명한 사실 근거
- [What is shift left testing? (GitHub Resources)](https://github.com/resources/articles/what-is-shift-left-testing) — Shift-left 테스팅의 기본 정의와 목적 설명
- [The 6 Types of AI Self-Healing in Test Automation (QA Wolf)](https://www.qawolf.com/blog/self-healing-test-automation-types) — Self-healing 로케이터의 28% 한계와 실패 유형 분류 근거
- [AI-Powered Risk-Based Test Automation for Optimizing Testing Processes](https://medium.com/@sermineldek/ai-powered-risk-based-test-automation-for-optimizing-testing-processes-e3930f11459b) — 결함 이력 기반 리스크 우선순위화 테스트 생성 방식 설명
- [Measuring AI ROI Through Business Outcomes (SD Times)](https://sdtimes.com/ai/measuring-ai-roi-through-business-outcomes/) — 활동 지표 대신 비즈니스 성과 지표로 AI ROI를 측정해야 한다는 근거 통계
