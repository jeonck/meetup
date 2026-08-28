---
title: "2026-08-28 AI 에이전트의 State와 Memory: MongoDB로 구현하기"
date: 2026-08-28T09:27:59.482638+09:00
tags: ["mongodb", "ai-agent", "vector-search"]
---
## 📋 밋업 한눈에 보기

이번 밋업은 CNCF 및 스폰서 소개, 참석자 자기소개 등 네트워킹 시간으로 시작한 뒤, MongoDB 발표자가 AI 에이전트를 만들 때 필요한 state와 memory 개념을 설명하는 발표로 이어졌다. 발표자는 LLM 자체는 상태가 없다는 점을 지적하며, 안정적인 에이전트를 만들려면 작업 상태(state)와 사용자 관련 정보(memory)를 구분해서 저장해야 한다고 강조했다. 이어서 동시성 문제 해결을 위한 findOneAndUpdate, hybrid search를 위한 rank fusion, 그리고 mongod/mongot 프로세스 아키텍처 등 MongoDB의 구체적인 기능들을 예시와 함께 소개했다.

## 🔑 핵심 요점

- LLM/AI 에이전트는 기본적으로 상태가 없는(stateless) 구조이므로, 매 요청마다 필요한 맥락을 다시 제공해야 한다.
- State는 작업이 중단됐을 때 어디서부터 재시작할지 알려주는 정보이고, Memory는 사용자와의 상호작용에서 얻은 정보라는 점에서 서로 다른 개념이다.
- Memory는 세션 내에서만 유지되는 short-term memory, 세션을 넘어 유지되는 long-term memory, 특정 작업 수행 중에만 필요한 working memory로 나뉜다.
- 여러 세션이 동시에 같은 상태를 수정하면 race condition이 발생할 수 있고, findOneAndUpdate 같은 원자적 연산으로 이를 방지할 수 있다.
- MongoDB Atlas Search는 full-text search와 semantic(vector) search를 rank fusion 연산으로 결합한 hybrid search를 지원한다.
- 데이터가 변경되면 검색 인덱스(임베딩 포함)가 자동으로 재생성되어 개발자가 직접 동기화를 신경 쓸 필요가 없다.
- MongoDB의 검색 아키텍처는 문서를 저장하는 mongod 프로세스와 검색 인덱싱을 담당하는 mongot 프로세스로 나뉘어 있어 독립적으로 스케일링할 수 있다.

## 🛠 핵심 기술 쉽게 이해하기

### MongoDB

문서(document) 지향 NoSQL 데이터베이스로, 데이터를 JSON과 유사한 BSON(Binary JSON) 형식으로 저장한다. 특정 필드를 인덱싱해서 빠르게 조회하거나 검색할 수 있다.

**왜 필요한가** — AI 에이전트의 state, 대화 기록, memory 등 다양한 형태의 정보를 하나의 데이터베이스에 통합해서 저장하고, 여러 저장소 간 동기화 문제를 줄이기 위해 사용한다.

**발표에서는** — 발표자는 MongoDB를 이용해 에이전트의 state와 short/long-term memory를 저장하고, findOneAndUpdate라는 원자적 연산으로 여러 세션이 동시에 같은 상태를 수정할 때 발생하는 race condition을 방지하는 방법을 설명했다.

### MongoDB Atlas Search (hybrid search / rank fusion)

텍스트 키워드 검색(full-text search)과 의미 기반 벡터 검색(semantic/vector search)을 함께 지원하는 검색 기능이다. rank fusion 연산자를 사용하면 여러 검색 방식의 결과를 자동으로 합쳐준다.

**왜 필요한가** — 에이전트가 사용자 정보나 대화 기록에서 정확한 정보를 찾으려면 단순 키워드 매칭만으로는 부족하고, 의미가 비슷한 내용까지 찾아낼 수 있어야 하기 때문이다.

**발표에서는** — 발표자는 employee 데이터를 예로 들어 이름 필드에 대한 텍스트 검색과 설명 필드에 대한 semantic search를 rank fusion으로 결합하는 방식을 시연했고, 원본 데이터가 바뀌면 인덱스가 자동으로 재생성된다고 언급했다.

### Voyage AI (임베딩 서비스)

텍스트를 벡터(임베딩)로 변환해주는 임베딩 전문 AI 서비스로, 발표에 따르면 MongoDB가 몇 년 전 인수한 회사다.

**왜 필요한가** — 벡터 기반 semantic search를 하려면 텍스트를 임베딩으로 바꿔야 하는데, 이를 MongoDB와 통합된 형태로 손쉽게 제공하기 위해 도입되었다.

**발표에서는** — 발표자는 MongoDB가 이 임베딩 서비스를 인수해 자체 임베딩 모델과 외부 모델을 함께 지원하며, 정확한 정보 검색(memory retrieval)을 위한 핵심 요소라고 설명했다.

### mongod / mongot 프로세스 아키텍처

MongoDB Atlas Search 내부에서 실제 문서를 저장하는 mongod 프로세스와, 검색 인덱스 생성을 전담하는 mongot(Lucene 기반) 프로세스로 역할이 분리되어 있는 구조다.

**왜 필요한가** — 검색 워크로드와 데이터 워크로드를 분리해서 서로 영향을 주지 않고 각각 독립적으로 확장(scale)할 수 있게 하기 위함이다.

**발표에서는** — Q&A에서 청중이 검색 노드와 데이터 노드가 어떻게 함께 동작하는지 묻자, 발표자는 문서는 mongod에, 검색에 필요한 인덱스는 mongot에 저장되며 두 프로세스를 독립적으로 배포·스케일링할 수 있다고 답했다.

## 🧭 추구 방향과 흐름

- **Stateless 에이전트에서 Stateful 에이전트로** — 발표자는 LLM 자체는 상태가 없는 노드터미니스틱(non-deterministic) 응답 생성기일 뿐이며, 실제 프로덕션 환경에서 안정적으로 동작하는 에이전트를 만들려면 작업 재시작을 위한 state 관리와 사용자를 기억하기 위한 memory 관리가 필수적이라는 점을 강조했다.
- **데이터베이스 하나로 검색·상태·메모리 통합** — 발표자는 별도의 벡터 DB, 캐시, 관계형 DB를 따로 쓰면 정보 동기화가 복잡해진다고 지적하며, MongoDB 같은 단일 시스템에서 hybrid search와 state/memory 저장을 함께 처리하는 방향을 제시했다.

## 💬 Q&A 하이라이트

<details><summary>Q. 검색 노드와 다른 컴포넌트(state 저장)를 서로 다르게 스케일링할 수 있는지, mongod와 mongot 프로세스가 어떻게 함께 동작하는지</summary><p>문서 자체는 mongod 프로세스에 저장되고 검색에 필요한 인덱스는 mongot 프로세스에 별도로 저장되며, 이 두 프로세스는 독립적으로 배포하고 스케일링할 수 있다고 답했다.</p></details>

<details><summary>Q. 에이전트의 state와 관련 정보에 대한 접근을 어떻게 관리하고 보안을 적용하는지</summary><p>일반 애플리케이션 사용자와 마찬가지로 저장된 정보에 대해 통상적인 접근 제어(access control)를 적용할 수 있으며, 필요한 보안 정책을 걸 수 있다고 답했으나 시간 관계상 세부 내용은 다루지 못했다.</p></details>

## 🚀 바로 활용하기

1. MongoDB Atlas Search 문서에서 hybrid search(rank fusion) 예제를 직접 따라 해보기
2. findOneAndUpdate를 사용해 동시성 문제를 방지하는 원자적 업데이트 패턴을 연습해보기
3. 에이전트를 설계할 때 state와 short-term/long-term/working memory를 구분해서 데이터 모델을 정리해보기
4. Voyage AI 임베딩과 MongoDB 통합 예제를 찾아보고 semantic search를 실습해보기

## 🔗 참고 자료

- [MongoDB 공식 홈페이지](https://www.mongodb.com) — 발표에서 다룬 state/memory 저장, hybrid search 기능의 근간이 되는 MongoDB 공식 사이트
- [MongoDB Manual](https://www.mongodb.com/docs/manual/) — findOneAndUpdate 등 발표에서 언급된 원자적 연산과 BSON 문서 구조에 대한 공식 문서
- [Voyage AI](https://www.voyageai.com) — 발표에서 언급된 임베딩 서비스 제공사 공식 사이트
- [CNCF](https://www.cncf.io) — 밋업 초반에 언급된 클라우드 네이티브 관련 스폰서/커뮤니티 단체
