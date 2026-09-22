---
title: "2026-09-23 Copilot Studio로 주문 취소 에이전트 만들기 실습"
date: 2026-09-23T05:30:02.504292+09:00
tags: ["copilot-studio", "power-automate", "mcp"]
---
## 📋 밋업 한눈에 보기

이번 밋업은 Microsoft Copilot Studio 실습 워크숍으로, Power Automate 플로우와 Dataverse를 연동해 주문을 취소하는 에이전트를 직접 만들어보는 세션이었습니다. 참가자들은 flow 안에서 order ID를 받아 레코드를 조회하고 상태를 Cancelled로 업데이트하는 과정을 따라 했고, 이를 에이전트의 tool로 등록해 채팅으로 테스트했습니다. 후반부에는 MCP(Model Context Protocol)를 이용해 Outlook 이메일을 트리거로 삼아 사용자 개입 없이 자동으로 응답하는 autonomous agent 구성도 다뤘습니다. 실습 중간에 잘못된 테이블 이름, 트리거 미작동, 중복 flow 생성 등 여러 트러블슈팅 상황이 실시간으로 다뤄졌습니다.

## 🔑 핵심 요점

- Copilot Studio 에이전트에 Power Automate flow를 tool로 연결해 Dataverse 레코드를 조회·업데이트하는 실습을 진행했다.
- flow에서 List rows로 가져온 결과의 row ID를 함수식으로 참조해 Update a row 액션에 전달하는 방식을 배웠다.
- 존재하지 않는 order ID를 입력하면 flow가 매칭에 실패해 에러를 반환하며, 실제 운영 환경에서는 별도의 에러 핸들링이 필요하다는 점이 강조되었다.
- flow를 에이전트에 연결할 때는 instructions에 forward slash(/)로 tool 이름을 참조해야 하며, 이름과 description이 에이전트의 동작 트리거에 중요하다.
- MCP를 추가하면 사용자가 직접 대화를 시작하지 않아도 에이전트가 이메일 등 외부 이벤트에 자동으로 반응하는 autonomous 기능을 구현할 수 있다.
- Outlook MCP 서버를 tool로 추가하고 '이메일 도착' 트리거에 폴더·제목 필터를 설정해 특정 이메일에만 반응하도록 구성했다.
- 실습 중 테이블 이름 오타, 중복 flow, 트리거 미발동 등 다양한 오류가 발생했고 현장에서 하나씩 디버깅하는 과정이 시연되었다.

## 🛠 핵심 기술 쉽게 이해하기

### Microsoft Copilot Studio

대화형 AI 에이전트를 코드 없이 만들 수 있는 Microsoft의 저코드 플랫폼입니다. 지식 소스, tool(도구), 트리거 등을 조합해 특정 업무를 수행하는 챗봇형 에이전트를 구성할 수 있습니다.

**왜 필요한가** — 사용자 요청을 이해하고 백엔드 시스템(Power Automate, Dataverse 등)과 연동해 실제 업무를 자동으로 처리하기 위해 사용합니다.

**발표에서는** — 발표자는 주문 취소를 처리하는 에이전트를 처음부터 만들면서 이름/설명 설정, tool 추가, instructions 작성, 채팅 테스트까지 전 과정을 실습으로 보여줬습니다.

### Power Automate

여러 앱과 서비스를 연결해 자동화된 워크플로우(flow)를 만드는 도구입니다. 트리거가 발생하면 정해진 순서대로 액션들이 실행됩니다.

**왜 필요한가** — 에이전트가 실제로 데이터베이스 레코드를 조회하고 값을 변경하는 등의 구체적인 작업을 수행하려면 flow가 필요합니다.

**발표에서는** — List rows로 Dataverse에서 주문 레코드를 찾고, 함수식으로 row ID를 넘겨 Update a row 액션으로 주문 상태를 Cancelled로 바꾸는 flow를 만들고 테스트하는 과정이 자세히 다뤄졌습니다.

### Dataverse

Microsoft Power Platform에서 사용하는 클라우드 기반 데이터베이스로, 테이블 형태로 비즈니스 데이터를 저장하고 관리합니다.

**왜 필요한가** — 에이전트와 flow가 실제 주문 데이터(machine order 테이블 등)를 읽고 쓸 저장소가 필요하기 때문에 사용됩니다.

**발표에서는** — 참가자들은 make.powerapps.com에서 machine order 테이블을 열어 특정 order ID의 상태 값을 직접 확인하고, flow 실행 후 상태가 Cancelled로 바뀌었는지 검증했습니다.

### Model Context Protocol (MCP)

AI 에이전트가 외부 서비스(이메일, 캘린더 등)의 기능을 표준화된 방식으로 호출할 수 있게 해주는 프로토콜입니다.

**왜 필요한가** — 사용자가 직접 채팅을 시작하지 않아도 에이전트가 외부 이벤트(예: 이메일 수신)에 반응해 자율적으로 동작하도록 하기 위해 사용합니다.

**발표에서는** — Outlook용 Email management MCP server를 tool로 추가하고, '주문 상태' 제목의 이메일이 inbox에 도착하면 자동으로 답장을 보내도록 트리거와 instructions를 설정하는 과정이 시연되었습니다.

### Power Apps (maker portal)

make.powerapps.com에서 제공하는 관리 화면으로, Dataverse 테이블 데이터를 직접 조회하고 편집할 수 있습니다.

**왜 필요한가** — flow나 에이전트가 만든 결과가 실제 데이터에 반영되었는지 확인하거나, 테스트용 데이터(order ID 등)를 미리 찾기 위해 사용합니다.

**발표에서는** — 참가자들이 테스트할 order ID를 찾기 위해 이 포털에서 machine order 테이블을 열어 값을 확인했고, environment를 잘못 선택해 테이블이 안 보이는 문제도 현장에서 해결했습니다.

## 🧭 추구 방향과 흐름

- **저코드 기반 AI 에이전트 구축** — 발표는 코드를 작성하지 않고 UI 조작만으로 데이터 조회, 업데이트, 이메일 응답까지 처리하는 에이전트를 만드는 방향을 지향합니다. Copilot Studio와 Power Automate를 조합해 비개발자도 업무 자동화 에이전트를 만들 수 있음을 보여주는 것이 핵심이었습니다.
- **에이전트의 자율성(Autonomous agent) 확장** — 세션 후반부는 사용자가 대화를 시작해야만 동작하는 방식에서 벗어나, 외부 이벤트(이메일 수신)에 자동으로 반응하는 방향으로 나아갑니다. MCP를 통해 트리거 기반의 자율 동작을 구현한 것이 그 근거입니다.
- **실습 중심의 트러블슈팅 교육** — 발표자는 이론 설명보다 참가자 화면을 직접 공유받아 오류(잘못된 테이블 이름, 중복 flow, 트리거 미작동)를 함께 찾고 고치는 방식으로 진행했습니다. 이는 실제 현업에서 마주칠 디버깅 경험을 미리 체득시키려는 목적으로 보입니다.

## 💬 Q&A 하이라이트

<details><summary>Q. 존재하지 않는 order ID(예: 100)를 입력하면 flow가 어떻게 동작하나요?</summary><p>List rows 필터가 해당 번호를 데이터베이스에서 찾지 못하므로 flow가 실행되지 않고 입력이 올바르지 않다는 에러를 반환합니다. 실제 운영에서는 이런 잘못된 입력에 대비해 별도의 에러 핸들링과 대체 흐름을 구성해야 합니다.</p></details>

<details><summary>Q. 이메일 MCP를 통한 응답이 실제로 발송되지 않고 '초안(draft)'으로만 남는 이유는 무엇인가요?</summary><p>발표자는 이메일을 실제로 발송하는 데 필요한 권한(permission)이 아직 제대로 구성되지 않아서일 가능성이 크다고 답했습니다.</p></details>

<details><summary>Q. 한 참가자가 flow가 두 개 생성되어 어떤 flow가 에이전트에 실제로 연결되어 있는지 구분하기 어렵다고 질문했습니다.</summary><p>발표자는 에이전트의 instructions에서 어떤 tool 이름이 forward slash로 참조되어 있는지 확인해 그것이 실제 연결된 flow이며, 사용하지 않는 나머지 flow는 3-dot 메뉴에서 삭제하면 된다고 안내했습니다.</p></details>

## 🚀 바로 활용하기

1. Copilot Studio에서 간단한 에이전트를 만들고, Power Automate flow를 tool로 연결해 Dataverse 레코드를 조회·업데이트하는 실습을 따라해 본다.
2. List rows와 Update a row 액션을 조합할 때 함수식(FX)으로 이전 액션의 출력값(row ID)을 참조하는 방법을 직접 연습해본다.
3. 에이전트 instructions에 tool을 forward slash(/)로 참조하는 문법과 description 작성법을 익혀 트리거 정확도를 높여본다.
4. Outlook 등 외부 서비스를 MCP로 연동해 이메일 도착 같은 이벤트 기반으로 에이전트가 자동 응답하는 autonomous 시나리오를 구성해본다.

## 🔗 참고 자료

- [Microsoft Copilot Studio 공식 문서](https://learn.microsoft.com/en-us/microsoft-copilot-studio/) — 에이전트 생성, tool 추가, instructions 작성 등 발표에서 다룬 전체 워크플로우의 근거 문서입니다.
- [Power Automate 공식 문서](https://learn.microsoft.com/en-us/power-automate/) — List rows, Update a row 등 flow 액션 구성 방식을 확인할 수 있습니다.
- [Microsoft Dataverse 개요](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro) — 발표에서 다룬 machine order 테이블 등 데이터 저장 구조의 배경 지식입니다.
- [Power Apps](https://learn.microsoft.com/en-us/power-apps/) — make.powerapps.com 메이커 포털에서 테이블 데이터를 확인하는 방법과 관련됩니다.
- [Model Context Protocol](https://modelcontextprotocol.io) — 발표 후반부에 다룬 MCP 기반 autonomous 에이전트 구성의 기술적 배경입니다.
