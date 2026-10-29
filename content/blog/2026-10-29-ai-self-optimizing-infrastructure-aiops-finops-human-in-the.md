---
title: "2026-10-29 AI는 은빛 탄환이 아니다: Self-Optimizing Infrastructure 시대의 AIOps·FinOps·Human-in-the-Loop"
date: 2026-10-29T09:20:20.994591+09:00
tags: ["aiops", "finops-for-ai", "human-in-the-loop"]
---
## 왜 지금 "자가 최적화 인프라"인가

이번 meetup에서 발표자들은 IoT 디바이스 수백만 대에서 매달 쏟아지는 데이터를 다루는 통신·에너지 업종의 경험을 바탕으로, AI를 인프라 운영에 도입할 때 생기는 현실적인 딜레마를 공유했다. 핵심은 "AI가 알아서 다 해줄 것"이라는 기대와 실제 운영 사이의 간극이다. 업계 전반에서도 비슷한 흐름이 보인다. [Motadata의 IT 운영 트렌드 분석](https://motadata.com/blog/it-operations-trends)과 관련 업계 자료들은 AIOps가 경보(alert)에 사후 대응하던 방식에서, 장애를 예측하고 선제적으로 조치하는 "자가 치유(self-healing) 인프라"로 이동하고 있다고 설명한다. 용량 고갈을 예측해 미리 스케일링하거나, 비정상 서비스를 자동으로 재시작·롤백하는 수준까지 성숙도가 올라가는 식이다.

## AI는 블랙박스가 아니라 "평가 대상"이어야 한다

발표자는 "AI를 silver bullet(은빛 탄환)이나 black box로 취급하는 순간 문제가 시작된다"고 강조했다. 이는 최근 거버넌스 논의와 정확히 맞닿아 있다. [Tungsten Automation의 거버넌스 가이드](https://www.tungstenautomation.com/blog/human-in-the-loop-ai-enterprise-governance-best-practices)는 EU AI Act와 NIST AI RMF가 고위험 영역에서 인간의 감독·추적성·설명 가능성을 요구하는 흐름을 짚으며, Deloitte 조사에서 기업의 46%가 거버넌스를 핵심 리스크로 꼽았지만 성숙한 거버넌스 체계를 갖춘 곳은 21%에 불과하다는 점을 인용한다. [Airia의 분석](https://airia.com/blog/human-in-the-loop-enterprise-ai-controls/) 역시 금융·헬스케어 등 고위험 의사결정에는 에스컬레이션 경로, 오버라이드 기록, 리스크 등급별 자동화 임계값 같은 "설계된" human-in-the-loop이 필요하다고 강조한다. 단순히 사람을 끼워 넣는 것만으로는 책임을 떠넘기는 "러버스탬프"에 그칠 위험이 있다는 지적도 함께 나온다.

모델 품질 평가도 마찬가지다. 발표자가 말한 "어떤 모델이 다른 모델보다 더 잘 hallucinate하는지 봐야 한다"는 말은 실제로 [Hallucinations Leaderboard](https://alphaxiv.org/benchmarks/university-college-london/hallucinations-leaderboard)처럼 사실성(factuality)과 충실성(faithfulness)을 구분해 측정하는 공개 벤치마크가 존재하는 이유이기도 하다. 다만 이런 공개 점수는 자사 워크로드를 완벽히 대변하지 못하므로, 실제 업무 데이터 100~200건으로 자체 평가셋을 구성해야 한다는 실무 가이드도 함께 참고할 만하다.

## 멀티모델 전략과 AI 전용 FinOps

이번 발표의 가장 구체적인 조언은 "항상 최고 모델, 최고 정확도를 쫓지 말라"는 것이었다. 업무 유형별로 적합한 모델을 쓰는 멀티모델 라우팅이 실제 업계 표준으로 자리잡는 중이다. [Sphere Partners의 cost-aware routing 분석](https://www.sphereinc.com/blogs/cost-aware-model-routing)은 목표가 무조건 저렴한 모델이 아니라 "가치를 더하지 못하는 곳에 프리미엄 모델을 쓰지 않는 것"이라고 정리하며, 분류·추출·템플릿 생성 같은 업무는 소형 모델로도 충분하다고 본다. 반면 비즈니스 핵심 트랜잭션처럼 분당 매출 손실이 발생하는 영역은 더 높은 품질의 모델과 즉각적인 이상탐지가 필요하다는 것이 발표자의 설명과도 일치한다.

이 흐름은 FinOps 영역으로도 확장되고 있다. [PointFive의 FinOps for AI 자료](https://www.pointfive.co/finops-for-ai)는 Capgemini 조사를 인용해 2025년 기업의 68%가 GenAI 예산을 10% 이상 초과 집행했다고 전한다. 실제로 [Capgemini의 관련 보고서](https://smestreet.in/technology/capgemini-highlights-finops-gaps-in-cloud-saas-gen-ai-adoption-10229465)도 비용 가시성 부족과 자원 저활용을 주요 원인으로 지목한다. [Revefi의 분석](https://www.revefi.com/blog/finops-for-ai)은 LLM 호출이 전통적인 클라우드 태깅 체계처럼 조직·팀·기능 메타데이터를 갖지 못해 비용 추적 자체가 어렵다는 구조적 문제를 짚는다. 발표자가 말한 "AI 비용 절감분이 비즈니스 운영 비용 절감분보다 커야 한다"는 기준은 결국 토큰 단위가 아니라 해결된 티켓당 비용, SLA 충족률 같은 비즈니스 지표로 ROI를 측정하라는 FinOps의 최신 권고와 같은 방향이다.

## 실전 도입을 위한 제언

정리하면 세 가지다. 첫째, AIOps는 반응형 모니터링에서 예측형·자율 운영으로 가는 큰 흐름이지만 아직 성숙도가 낮은 조직이 많으므로 작은 자동화 범위부터 검증해야 한다. 둘째, human-in-the-loop은 형식적 체크박스가 아니라 리스크 등급에 따라 설계된 통제 장치로 구축해야 블랙박스 리스크를 실제로 줄일 수 있다. 셋째, 모든 작업에 최고 모델을 쓰는 대신 작업별로 모델을 다르게 배치하고, 비용을 토큰이 아닌 비즈니스 성과 단위로 추적하는 AI 전용 FinOps 체계를 갖추는 것이 지금 업계가 요구하는 다음 단계다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Motadata – IT Operations Trends](https://motadata.com/blog/it-operations-trends) — AIOps가 사후 대응형 모니터링에서 예측형·자가치유 인프라로 이동한다는 트렌드를 뒷받침
- [Tungsten Automation – Human-in-the-Loop AI: Enterprise Governance Best Practices](https://www.tungstenautomation.com/blog/human-in-the-loop-ai-enterprise-governance-best-practices) — EU AI Act/NIST AI RMF 기반 인간 감독 요구와 기업 거버넌스 성숙도 격차(46% vs 21%) 인용
- [Airia – Human-in-the-Loop Enterprise AI Controls](https://airia.com/blog/human-in-the-loop-enterprise-ai-controls/) — 리스크 등급별 자동화 임계값, 에스컬레이션, 오버라이드 기록 등 설계된 HITL 통제 사례
- [Hallucinations Leaderboard](https://alphaxiv.org/benchmarks/university-college-london/hallucinations-leaderboard) — 모델별 hallucination(사실성/충실성) 차이를 측정하는 공개 벤치마크 근거
- [Sphere Partners – Cost-aware model routing](https://www.sphereinc.com/blogs/cost-aware-model-routing) — 작업 유형별로 적합한 모델을 선택하는 멀티모델 전략의 원칙 설명
- [PointFive – FinOps for AI](https://www.pointfive.co/finops-for-ai) — Capgemini 조사 기반 2025년 GenAI 예산 초과(68%) 통계와 토큰 경제성 측정법 제시
- [Capgemini 관련 보도 – FinOps gaps in Cloud, SaaS, Gen AI Adoption](https://smestreet.in/technology/capgemini-highlights-finops-gaps-in-cloud-saas-gen-ai-adoption-10229465) — GenAI 비용 초과의 원인으로 비용 가시성 부족과 자원 저활용을 지목
- [Revefi – FinOps for AI](https://www.revefi.com/blog/finops-for-ai) — LLM 호출이 전통 클라우드 태깅 체계와 달리 메타데이터 부재로 비용 추적이 어렵다는 구조적 문제 설명
