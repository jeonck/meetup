---
title: "2026-08-28 AI 에이전트에게 기억을 심는 법: State, Memory, 그리고 MongoDB 하이브리드 검색"
date: 2026-08-28T09:33:22.605812+09:00
tags: ["mongodb", "ai-agent-memory", "hybrid-search"]
---
## AI 에이전트, "말은 잘하는데 왜 기억을 못할까"

최근 밋업에서 다뤄진 핵심 주제는 AI 에이전트가 프로덕션 단계로 넘어가면서 부딪히는 실질적 병목, 즉 state와 memory 설계 문제였다. LangChain의 [State of Agent Engineering 리포트](https://www.langchain.com/state-of-agent-engineering)에 따르면 이미 조직의 상당수가 에이전트를 실제 운영 환경에 투입했지만, 응답 품질(정확성·일관성·환각)이 가장 큰 배포 장벽으로 꼽힌다. 발표자가 강조했듯 LLM 자체는 무상태(stateless)다. 매 요청마다 새로 답하기 때문에, "기억"은 애플리케이션이 별도로 설계해야 하는 인프라 문제가 된다.

## State와 Memory는 다른 문제다

발표의 첫 번째 원칙은 state와 memory를 혼동하지 말라는 것이다. LangGraph [공식 문서](https://docs.langchain.com/oss/python/langgraph/persistence)는 이를 명확히 구분한다. State는 그래프 실행의 매 super-step마다 저장되는 체크포인트로, 에이전트가 중단된 지점에서 재개하거나 human-in-the-loop, time-travel 디버깅을 가능케 하는 "실행 이력"이다. 반면 memory는 세션을 넘어 남아야 하는 지식이다. MongoDB는 이를 [단기·장기 메모리 가이드](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory)에서 working memory(현재 처리 중인 맥락), episodic memory(과거 사건), semantic memory(일반 지식), procedural memory(반복 작업 절차)로 세분화한다. MongoDB는 실제로 [체크포인터로 단기 상태를, Store로 장기 기억을 분리 저장](https://www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph)하는 통합을 LangGraph용으로 제공한다.

## 동시성: findAndModify가 필요한 이유

여러 세션이 같은 사용자의 기억 문서에 동시에 접근하면 경쟁 조건이 발생한다. 단일 사용자 환경에서 문제없던 read-then-write 패턴이, 다중 에이전트·다중 요청 환경에서는 두 요청이 같은 값을 읽고 서로의 갱신을 덮어써 버리는 상황을 만든다. MongoDB 공식 매뉴얼은 [단일 문서에 대한 쓰기 연산이 원자적](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/)임을 보장한다고 설명하는데, findAndModify(findOneAndUpdate)처럼 읽기와 수정을 하나의 연산으로 묶으면 이 원자성을 그대로 활용해 경쟁 조건을 근본적으로 없앨 수 있다. 여기에 버전 필드를 이용한 낙관적 잠금을 더하면, 다중 에이전트가 같은 장기 기억 레코드를 동시에 건드리는 시나리오에서도 정합성을 지킬 수 있다.

## 기억을 "찾는" 기술: 하이브리드 검색

기억을 저장하는 것과 필요한 순간에 정확히 꺼내는 것은 별개 문제다. MongoDB Atlas Search는 [전문(full-text) 검색과 벡터 검색을 하나의 파이프라인에서 결합](https://www.mongodb.com/company/blog/product-release-announcements/boost-search-relevance-mongodb-atlas-native-hybrid-search)하는 네이티브 하이브리드 검색을 제공한다. MongoDB 8.0부터 도입된 [$rankFusion](https://www.mongodb.com/docs/manual/reference/operator/aggregation/rankFusion/) 연산자는 여러 검색 파이프라인의 순위를 Reciprocal Rank Fusion(RRF) 알고리즘으로 합산해, 키워드 매칭의 정밀함과 의미 기반 검색의 유연함을 동시에 살린다. 대화 이력을 JSON/BSON 문서로 그대로 저장하면서도 이름·설명 필드가 즉시 전문 검색 대상이 되는 구조는, 스키마가 계속 진화하는 에이전트 메모리에 특히 잘 맞는다.

## 임베딩까지 데이터베이스 안으로

MongoDB는 2025년 2월 임베딩·리랭킹 모델 기업 [Voyage AI를 인수](https://www.mongodb.com/press/mongodb-announces-acquisition-of-voyage-ai)했다. CEO Dev Ittycheria가 밝혔듯, AI 도입을 가로막는 근본 원인 중 하나가 환각이며 이를 줄이려면 고품질 검색(retrieval)이 필수라는 판단이었다. 이후 Atlas 안에서 임베딩·리랭킹을 API로 직접 호출할 수 있도록 통합해, 별도 임베딩 서비스나 외부 벡터 스토어 관리 부담을 없앴다. 검색 트래픽이 커지면 [Search Nodes](https://www.mongodb.com/docs/search/deployment/deployment-options/)로 검색 프로세스(mongot)를 데이터 프로세스(mongod)와 분리 배치할 수 있어, 인덱싱·검색 부하가 트랜잭션 성능을 갉아먹는 리소스 경합 문제도 독립적으로 확장해 해결한다.

## 실무 도입 조언

에이전트에 기억을 붙이려는 팀이라면 먼저 state(재시작을 위한 실행 이력)와 memory(지식)를 별도 컬렉션·클래스로 설계하고, 검증된 체크포인터·Store 통합을 활용하는 것이 좋다. 다중 사용자 갱신이 있다면 findAndModify와 낙관적 잠금을 기본값으로 삼고, 검색 품질이 중요한 시나리오에서는 처음부터 하이브리드 검색을 설계에 포함시키는 편이 나중에 아키텍처를 갈아엎는 것보다 훨씬 저렴하다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [LangChain, State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering) — 에이전트 프로덕션 도입률과 품질이 최대 배포 장벽이라는 통계 근거
- [LangGraph Persistence — Docs by LangChain](https://docs.langchain.com/oss/python/langgraph/persistence) — state(체크포인트)와 memory(지식)의 공식적 구분, 체크포인터 동작 방식
- [What Is Agent Memory? — MongoDB](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory) — short-term/working/episodic/semantic/procedural memory 분류 근거
- [Powering Long-Term Memory For Agents With LangGraph And MongoDB](https://www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph) — MongoDB 체크포인터(단기)와 Store(장기) 이원화 통합 발표
- [Atomicity and Transactions — MongoDB Manual](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/) — 단일 문서 쓰기 연산의 원자성 보장, findAndModify 동시성 해법의 근거
- [Boost Search Relevance With MongoDB Atlas' Native Hybrid Search](https://www.mongodb.com/company/blog/product-release-announcements/boost-search-relevance-mongodb-atlas-native-hybrid-search) — 전문 검색과 벡터 검색을 결합한 네이티브 하이브리드 검색 소개
- [$rankFusion (aggregation) — MongoDB Manual](https://www.mongodb.com/docs/manual/reference/operator/aggregation/rankFusion/) — RRF 기반 하이브리드 검색 연산자의 공식 스펙과 MongoDB 8.0 도입 시점
- [MongoDB Announces Acquisition of Voyage AI](https://www.mongodb.com/press/mongodb-announces-acquisition-of-voyage-ai) — Voyage AI 인수 배경과 목적(환각 감소, 고품질 검색)에 대한 공식 발표
- [MongoDB Search Deployment Options](https://www.mongodb.com/docs/search/deployment/deployment-options/) — mongot/mongod 분리 배치(Search Nodes)를 통한 워크로드 독립 확장 근거
