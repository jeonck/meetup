---
title: "2026-08-26 AWS Bedrock 멀티에이전트와 MCP로 살펴보는 엔터프라이즈 에이전틱 AI 아키텍처"
date: 2026-08-26T02:56:11.331813+09:00
tags: ["aws-bedrock", "agentic-ai", "mcp"]
---
## 왜 지금 '에이전틱 AI'인가

2025년까지만 해도 기업 애플리케이션에 task-specific AI agent가 탑재된 비율은 5% 미만이었지만, [Gartner는 2026년 말까지 이 수치가 40%까지 급증할 것](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)이라고 전망했다. 단순히 하나의 LLM이 질문에 답하는 챗봇 시대를 지나, 여러 개의 전문화된 에이전트가 도구를 호출하고 서로 협업하며 실제 업무를 처리하는 '에이전틱(agentic)' 시스템으로 무게중심이 옮겨가고 있다. 이번 글에서는 AWS 생태계를 중심으로 이 흐름을 구성하는 핵심 기술 — Amazon Bedrock의 멀티에이전트 오케스트레이션, Lambda 기반 서버리스 실행 계층, AgentCore Memory, 그리고 도구 연동 표준인 Model Context Protocol(MCP) — 을 짚어본다.

## Bedrock 멀티에이전트: Supervisor가 이끄는 협업 구조

AWS는 2025년 3월 [Amazon Bedrock 멀티에이전트 협업 기능을 정식 출시](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-multi-agent-collaboration/)했다. 핵심 개념은 supervisor agent가 사용자의 복잡한 요청을 분해해 전문화된 collaborator agent들에게 위임하고, 각 결과를 다시 하나의 응답으로 통합하는 구조다. [AWS 공식 가이드](https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html)에 따르면 supervisor는 최대 10개의 협업 에이전트를 연결할 수 있고, 상황에 따라 순수 오케스트레이션 모드 또는 단순 요청을 곧바로 라우팅하는 모드를 선택해 지연 시간을 줄일 수 있다. Inline Agent 기능은 CDK 템플릿을 활용해 런타임에 동적으로 에이전트 구조를 생성할 수 있게 해, 고정된 파이프라인이 아니라 필요에 따라 재구성되는 시스템을 지향한다.

## 실행 계층: Lambda, EventBridge, SQS, Step Functions

에이전트가 '생각'만 하는 것이 아니라 실제로 행동하려면 실행 엔진이 필요하다. Bedrock 에이전트의 action group은 [OpenAPI 스키마와 하나의 Lambda 함수로 구성](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html)되며, 에이전트가 특정 작업이 필요하다고 판단하면 파라미터와 세션 정보를 이벤트로 담아 해당 Lambda를 호출한다. Lambda는 상태를 갖지 않는 서버리스 컴퓨트이기 때문에 요청마다 독립적으로 확장되고, 사용한 만큼만 비용이 발생한다는 장점이 있다. 이 위에서 오케스트레이션을 담당하는 것이 EventBridge, SQS, Step Functions다. [EventBridge는 이벤트를 필터링·라우팅하는 이벤트 버스](https://cloudchipr.com/blog/aws-eventbridge)로 프로듀서와 컨슈머를 완전히 분리하고, SQS는 프론트엔드와 백엔드 처리 속도 차이를 흡수하는 버퍼 역할을 하며, Step Functions는 조건 분기와 재시도 로직을 가진 워크플로우를 시각적으로 구성한다. 이 세 서비스의 조합은 마이크로서비스 시대부터 검증된 decoupling 패턴을 에이전틱 시스템에 그대로 이식한 것이다.

## 기억하는 에이전트: AgentCore Memory

대화가 세션을 넘어 이어지려면 기억이 필요하다. [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)는 단기 메모리와 장기 메모리를 구분한다. 단기 메모리는 세션 내의 원본 대화를 턴 단위로 저장해 즉각적인 문맥 유지를 담당하고, 장기 메모리는 백그라운드에서 비동기로 동작하며 요약(summarization), 시맨틱 사실(semantic memory), 사용자 선호도(user preferences) 같은 구조화된 지식을 추출해 세션 간에도 유지한다. AWS는 실무 가이드로 우선 DynamoDB나 ElastiCache 기반의 단기 메모리를 견고하게 만든 뒤, 필요한 경우에만 장기 시맨틱 메모리를 확장하라고 권고한다.

## 상호운용성의 표준, MCP

에이전트가 도구를 호출하는 방식이 저마다 다르면 생태계가 파편화된다. 이 문제를 해결하기 위해 Anthropic이 2024년 11월 공개한 [Model Context Protocol(MCP)](https://www.anthropic.com/news/model-context-protocol)은 LLM과 외부 데이터·애플리케이션·서비스를 연결하는 개방형 표준이다. [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro)는 이를 'AI 애플리케이션을 위한 USB-C'에 비유하는데, 한 번 구현하면 수많은 MCP 서버 생태계에 바로 연결된다는 의미다. OpenAI, Microsoft, Google DeepMind 등 주요 플레이어들이 빠르게 MCP를 채택하면서 사실상 업계 표준으로 자리잡았다.

## 보안이 핵심: Guardrails와 최소 권한

자율적으로 행동하는 에이전트가 늘어날수록 보안 리스크도 커진다. [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)는 콘텐츠 필터, 민감정보 탐지, 프롬프트 공격 탐지 등 6가지 정책 유형으로 모델 입출력을 검사하는 파이프라인이며, 유해 콘텐츠를 최대 88%까지 차단한다고 밝히고 있다. 업계 차원에서도 [Forrester의 2026 보안 서베이](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/)는 보안 의사결정권자의 49%가 에이전틱 AI를 우려 사항으로 꼽았다고 전하며, 에이전트마다 고유 자격 증명과 좁은 범위의 도구 허용 목록, 시간 제한이 있는 권한을 부여하는 zero standing privilege 원칙을 강조한다. IAM 역할을 통해 각 Lambda 함수와 에이전트가 딱 필요한 만큼의 권한만 갖도록 설계하는 것이 실질적인 방어선이다.

## 실무 도입을 위한 조언

도입을 고려한다면 다음 순서를 권한다. 첫째, 파운데이션 모델은 무조건 크고 비싼 것을 쓰기보다 지연 시간과 비용, 작업 난이도에 맞춰 'right-size'하고 Bedrock의 단일 API 구조를 활용해 모델을 유연하게 교체할 수 있도록 설계한다. 둘째, 상태는 Lambda 안에 두지 말고 DynamoDB나 AgentCore Memory 같은 외부 저장소로 분리해 stateless 원칙을 지킨다. 셋째, 도구별 IAM 역할과 Guardrails를 처음부터 설계에 포함시켜 사고 발생 시 blast radius를 최소화한다. 마지막으로, MCP처럼 업계 표준화가 진행 중인 프로토콜을 채택해 벤더 종속을 줄이는 것이 장기적으로 유리하다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Amazon Bedrock now supports multi-agent collaboration (AWS What's New)](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-multi-agent-collaboration/) — Bedrock 멀티에이전트 협업 기능의 2025년 3월 GA 출시 사실 뒷받침
- [Create multi-agent collaboration - Amazon Bedrock (AWS 공식 문서)](https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html) — supervisor-collaborator 구조, 최대 10개 협업 에이전트, Inline Agent 등 세부 사양
- [Configure Lambda functions - Amazon Bedrock (AWS 공식 문서)](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html) — action group과 Lambda 함수의 연결 구조, 이벤트 전달 방식 설명
- [Getting Started with AWS EventBridge](https://cloudchipr.com/blog/aws-eventbridge) — EventBridge의 이벤트 라우팅과 프로듀서-컨슈머 디커플링 특성
- [Add memory to your Amazon Bedrock AgentCore agent (AWS 공식 문서)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) — AgentCore Memory의 단기/장기 메모리 구조와 추출 전략 설명
- [Introducing the Model Context Protocol (Anthropic)](https://www.anthropic.com/news/model-context-protocol) — MCP의 최초 발표와 목적 설명
- [What is the Model Context Protocol (MCP)? (modelcontextprotocol.io)](https://modelcontextprotocol.io/docs/getting-started/intro) — MCP를 'USB-C for AI'로 비유하는 공식 설명 및 업계 채택 현황
- [Guardrails for Amazon Bedrock - safety filters and privacy controls (AWS Blog)](https://aws.amazon.com/bedrock/guardrails/) — Guardrails의 정책 유형과 유해 콘텐츠 차단율 88% 수치 근거
- [The State Of Agentic AI In 2026 (Forrester)](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/) — 보안 의사결정권자의 에이전틱 AI 우려 비율 및 zero standing privilege 권고
- [Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) — 에이전틱 AI 도입 가속화를 보여주는 서론의 통계 근거
