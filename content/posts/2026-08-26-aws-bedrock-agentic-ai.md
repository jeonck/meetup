---
title: "2026-08-26 AWS Bedrock 기반 Agentic AI 아키텍처 설계"
date: 2026-08-26T02:54:28.825415+09:00
tags: ["aws-bedrock", "agentic-ai", "serverless-architecture"]
---
## 📋 밋업 한눈에 보기

이번 세션은 AWS Bedrock을 중심으로 엔터프라이즈급 agentic AI 시스템을 어떻게 설계하는지를 다뤘다. 발표자는 시스템을 experience layer, orchestration layer, agent runtime layer, tools/memory/data layer의 4개 계층과 IAM·CloudWatch 같은 crosscutting 서비스로 나누어 설명했다. Bedrock의 supervisor-collaborator 멀티에이전트 구조, Lambda를 통한 tool 실행, 단기·장기 메모리 관리, least privilege 기반 보안 모델이 핵심 주제였다. 전체적으로 stateless, 서버리스 우선, 최소 권한 원칙에 기반한 프로덕션급 agentic 아키텍처 구축 가이드를 제시했다.

## 🔑 핵심 요점

- Agentic AI 시스템은 experience, orchestration, agent runtime, tools/memory/data의 4개 계층 구조로 설계하는 것이 권장된다.
- Amazon Bedrock의 supervisor agent는 복잡한 작업을 여러 specialist collaborator agent로 분해하고 결과를 다시 하나의 응답으로 통합한다.
- Lambda 함수는 stateless하고 최대 15분만 실행되므로, 세션을 넘어 유지해야 할 데이터는 DynamoDB 같은 외부 저장소에 보관해야 한다.
- 메모리는 단기(세션 내 대화)와 장기(세션 간 semantic search로 검색되는 지식)로 나뉘며, 각각 관리 방식이 다르다.
- 보안은 least privilege 원칙을 기반으로 하며, 각 tool과 agent에게 필요한 최소 권한만 부여해야 blast radius를 줄일 수 있다.
- MCP(Model Context Protocol)는 agent와 tool 간 표준 통신 프로토콜로, 이를 통해 다양한 tool을 plug-and-play로 연결할 수 있다.
- 모든 tool 호출은 로깅되어 누가 어떤 행동을 대신 수행했는지 추적 가능해야 하며, 이는 침해 발생 시 포렌식 분석에 필수적이다.

## 🛠 핵심 기술 쉽게 이해하기

### Amazon Bedrock

Bedrock은 여러 파운데이션 모델(FM)을 한곳에 모아 선택해서 쓸 수 있게 해주는 AWS 서비스다. AWS 자체 모델뿐 아니라 서드파티 모델, 직접 만든 모델도 포함할 수 있다.

**왜 필요한가** — 여러 LLM을 개별적으로 다루지 않고 하나의 API와 보안 정책(guardrails)으로 통합 관리하기 위해 사용한다.

**발표에서는** — 발표에서는 Bedrock을 agentic 아키텍처의 reasoning 핵심으로 소개했으며, supervisor-agent 멀티에이전트 프레임워크와 guardrails 기능이 여기서 제공된다고 설명했다.

### AWS Lambda

Lambda는 서버 관리 없이 코드를 실행할 수 있는 서버리스 컴퓨팅 서비스다. 호출될 때만 실행되고, stateless하며 최대 15분간만 동작한다.

**왜 필요한가** — agent가 실제로 tool을 호출해 업무 로직(DB 조회, API 호출 등)을 수행하도록 해주는 실행 계층이 필요하기 때문이다.

**발표에서는** — 발표자는 Lambda가 action group과 연결되어 agent가 실제 작업을 수행하는 layer라고 설명하며, stateless·pay-per-use·수평 확장 등 특성을 강조했다.

### Bedrock Supervisor / Multi-agent collaboration

Supervisor는 여러 specialist sub-agent를 조율하는 최상위 agent로, 복잡한 요청을 분해해 적절한 collaborator agent에게 위임하고 결과를 하나로 합친다.

**왜 필요한가** — 하나의 agent가 모든 일을 처리하기보다, 전문화된 여러 agent가 각자 잘하는 일을 맡도록 해 정확도와 확장성을 높이기 위함이다.

**발표에서는** — plain supervisor 모드와 routing 모드 두 가지 협업 방식, 최대 10개 collaborator agent 연결, 최대 3단계 계층 구조 등이 구체적으로 설명됐다.

### Amazon SQS / EventBridge / Step Functions

SQS는 메시지 큐로 프론트엔드와 백엔드 처리를 분리(decoupling)하고, EventBridge는 이벤트 발생 시 다른 작업을 트리거하며, Step Functions는 워크플로우 형태로 여러 단계를 조율한다.

**왜 필요한가** — orchestration layer에서 요청을 동기/비동기로 어떻게 처리할지, 어떤 순서로 tool을 호출할지 결정하기 위해 필요하다.

**발표에서는** — 발표자는 커피숍 비유(주문 접수와 제조 분리)로 SQS의 decoupling 개념을 설명하고, EventBridge와 Step Functions는 각각 이벤트 트리거와 워크플로우 조율 역할을 한다고 소개했다.

### IAM (Identity Access Management) & Least Privilege

IAM은 사용자나 프로그램(principal)이 무엇을 할 수 있는지 권한을 관리하는 AWS 서비스다. Least privilege는 필요한 최소한의 권한만 부여하는 보안 원칙이다.

**왜 필요한가** — agent나 Lambda 함수가 침해당하더라도 피해 범위(blast radius)를 최소화하기 위해 필요하다.

**발표에서는** — 발표에서는 refund agent가 $50 한도까지만 환불 처리 가능하고 고객 정보 서랍은 아예 접근 불가한 예시로 least privilege를 설명했다.

### MCP (Model Context Protocol)

MCP는 agent가 tool과 통신하는 표준 프로토콜로, Anthropic이 초기 버전을 만들었다고 언급됐다.

**왜 필요한가** — 모든 개발자가 매번 자체 프로토콜을 만들지 않고도 tool과 agent를 상호 호환되게 plug-and-play로 연결하기 위함이다.

**발표에서는** — tool interface 설명 중 처음 언급되었으며, agent가 tool을 호출하는 표준 방식으로 소개됐다.

## 🧭 추구 방향과 흐름

- **Serverless-first, stateless 아키텍처** — 발표자는 agent와 Lambda 함수를 stateless하게 설계하고, 상태가 필요하면 DynamoDB나 ElastiCache 같은 외부 저장소에 두라고 강조했다. 이는 수평 확장, 장애 복구, 비용 효율성을 위한 클라우드 네이티브 설계 원칙이다.
- **Least privilege 기반 보안** — 모든 tool과 agent에 최소 권한만 부여하고, IAM 역할을 tool 단위로 분리하며, 모든 호출을 로깅해 추적 가능하게 만드는 것이 핵심 원칙으로 제시됐다. 이는 SQL injection 같은 과거 취약점 사례와 privilege escalation 공격을 언급하며 근거로 들었다.
- **전문화된 멀티에이전트 협업** — 하나의 범용 agent 대신, 각각 한 가지 일을 잘하는 specialist agent들을 supervisor가 조율하는 구조를 지향한다. 이는 복잡한 작업을 안정적으로 분해·위임·통합하기 위한 설계 방향으로 발표 전반에 걸쳐 강조됐다.
- **메모리의 계층화와 경계 설정** — 단기 메모리와 장기 메모리를 구분하고, TTL(time to live)로 메모리를 만료시키며, 메모리 범위를 제한(scoped)하는 방향을 제시했다. 이는 성능뿐 아니라 데이터 침해 시 blast radius를 줄이기 위한 보안적 고려이기도 하다.

## 🚀 바로 활용하기

1. AWS Bedrock 콘솔에서 사용 가능한 파운데이션 모델 목록을 확인하고, 워크로드 성격(비용, 지연시간, 성능)에 맞는 모델을 선택해본다.
2. 간단한 Lambda 함수와 action group을 만들어 Bedrock agent가 tool을 호출하는 흐름을 직접 구성해본다.
3. DynamoDB 또는 ElastiCache를 이용해 세션 상태를 외부에 저장하는 stateless Lambda 패턴을 연습해본다.
4. IAM 역할을 tool 단위로 세분화해 least privilege 원칙을 적용하는 방법을 검토해본다.

## 🔗 참고 자료

- [AWS](https://aws.amazon.com) — Bedrock, Lambda, IAM, CloudWatch 등 발표에서 다룬 모든 서비스의 공식 홈페이지
- [Amazon Bedrock](https://aws.amazon.com/bedrock) — 발표의 핵심인 파운데이션 모델 허브 및 supervisor 멀티에이전트 프레임워크 공식 페이지
- [AWS Lambda](https://aws.amazon.com/lambda) — agent가 tool을 실행하는 서버리스 컴퓨팅 계층에 대한 공식 문서
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb) — stateless Lambda 함수의 외부 상태 저장소로 언급된 NoSQL 데이터베이스
- [Amazon EventBridge](https://aws.amazon.com/eventbridge) — 이벤트 기반 orchestration 계층에서 소개된 서비스
- [AWS Step Functions](https://aws.amazon.com/step-functions) — 워크플로우 형태로 tool을 조율하는 orchestration 서비스
