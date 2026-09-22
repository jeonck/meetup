---
title: "2026-09-23 Microsoft Copilot Studio 핸즈온: 환경, ALM, 그리고 에이전트 만들기"
date: 2026-09-23T02:00:32.070916+09:00
tags: ["copilot-studio", "power-platform", "ai-agent"]
---
## 📋 밋업 한눈에 보기

이 밋업은 Microsoft Copilot Studio를 활용해 AI 에이전트를 처음부터 만들어보는 실습(핸즈온) 워크숍이다. 참가자들은 Power Platform 환경(environment)을 만들고, 솔루션(solution)을 임포트한 다음, Power Apps 캔버스 앱으로 더미 데이터를 생성하고, 마지막으로 대화형 프롬프트로 Copilot Studio 에이전트를 만드는 전체 흐름을 따라갔다. 진행자는 환경, 솔루션, ALM(Application Lifecycle Management) 같은 개념을 비유를 들어가며 설명했고, Copilot Studio 에이전트와 Microsoft 365 Copilot 내 에이전트의 차이(LLM 선택권, 지식 소스, 도구, 트리거 등)를 강조했다. 세션 상당 부분은 계정 로그인, 트라이얼 연장, 파일 임포트 등 실습 중 발생한 기술적 트러블슈팅에 할애되었다.

## 🔑 핵심 요점

- Power Platform의 environment는 테넌트 내에서 보안, 데이터 상주(residency), 소비량, 데이터 격리 등의 목적으로 나누는 독립된 작업 공간이며, 그 안에 앱·에이전트·자동화·데이터가 저장된다.
- ALM(Application Lifecycle Management)은 앱이나 에이전트를 실제 운영 데이터에 바로 투입하지 않고 개발-테스트-운영 단계를 거쳐 안전하게 배포하는 프로세스이며, 운전 연습(시뮬레이션→한산한 도로→시내)에 비유해 설명되었다.
- solution은 에이전트, 앱, 데이터 소스를 하나로 묶어 여러 environment 사이로 이동시킬 수 있는 컨테이너 역할을 한다.
- Copilot Studio 에이전트는 Microsoft 365 Copilot 내에서 만드는 에이전트보다 훨씬 유연하다: LLM을 여러 옵션 중에서 선택할 수 있고, Azure AI Search·Salesforce·Confluence·Databricks 같은 다양한 지식 소스를 연결할 수 있으며, 데이터 소스에 쓰기 작업을 하는 tool, 자율 실행을 위한 trigger, 다른 에이전트를 호출하는 기능까지 제공한다.
- 이런 확장된 지식 소스 연결 기능은 데모 계정의 제한 때문이 아니라, Copilot Studio와 Microsoft 365 Copilot(프리미엄 라이선스 포함)의 근본적인 플랫폼 차이에서 비롯된다.
- 최신 인터페이스에서 에이전트를 생성하면 Copilot credit(크레딧)이 소비되지만, 구버전 인터페이스에서는 이 변경 사항이 적용되었는지 Microsoft 측의 명확한 안내가 아직 없다.
- 관리자 권한이 있으면 Copilot Studio의 모니터링(monitor) 메뉴에서 에이전트의 성공률과 크레딧 소비 현황을 확인할 수 있다.

## 🛠 핵심 기술 쉽게 이해하기

### Microsoft Copilot Studio

대화형 프롬프트만으로 AI 에이전트를 만들 수 있는 로우코드 플랫폼이다. 에이전트에 지식 소스, 도구, 트리거를 붙여 특정 업무를 자동으로 수행하게 만들 수 있다.

**왜 필요한가** — 코딩 없이도 기업 데이터와 여러 LLM을 결합한 맞춤형 AI 에이전트를 빠르게 구축하기 위해 사용한다.

**발표에서는** — 참가자들은 프롬프트 한 줄로 에이전트를 생성했고, 진행자는 LLM 선택 옵션, 지식 소스 추가, 도구, 트리거, 다른 에이전트 호출 기능을 차례로 소개했다.

### Power Platform Environment

테넌트 내에서 앱, 에이전트, 데이터, 자동화를 저장하는 독립된 작업 공간이다. 보안, 데이터 상주, 소비량 관리, 데이터 격리 등의 이유로 용도별로 나눠 사용한다.

**왜 필요한가** — 여러 팀이나 목적(개발/테스트/운영 등)에 따라 데이터를 분리 관리하기 위해 필요하다.

**발표에서는** — 실습 첫 단계로 environment를 생성하고 Copilot Studio에서 올바른 environment를 선택하는 과정을 진행했다.

### Solution (Dataverse Solution)

에이전트, 앱, 데이터 소스를 하나의 패키지로 묶은 컨테이너다. 이 패키지를 여러 environment로 가져오거나(import) 옮길 수 있다.

**왜 필요한가** — 개발 environment에서 만든 결과물을 테스트·운영 environment로 안전하게 이동시키는 ALM 절차의 핵심 구성요소다.

**발표에서는** — 참가자들은 'Agent in a Day' 실습 zip 파일을 solution으로 import했고, import에는 최대 10분 정도 소요되었다.

### Power Apps (Canvas App)

미리 만들어진 UI를 통해 데이터베이스(Dataverse) 테이블에 레코드를 입력할 수 있는 로우코드 앱 유형이다.

**왜 필요한가** — 코드를 작성하지 않고도 업무용 폼이나 화면을 빠르게 만들어 데이터를 입력·조회하기 위해 사용한다.

**발표에서는** — 참가자들은 이미 만들어진 canvas app에서 machine order 레코드를 여러 건 생성해, 이후 Copilot Studio 에이전트가 조회할 더미 데이터를 준비했다.

### 지식 소스 커넥터 (Azure AI Search, Salesforce, Confluence, Databricks 등)

Copilot Studio 에이전트가 답변을 생성할 때 참고할 외부 데이터 소스를 연결하는 기능이다.

**왜 필요한가** — 에이전트가 사내 문서, CRM 데이터, 데이터 레이크 등 다양한 시스템의 최신 정보를 근거로 답하게 하기 위해 필요하다.

**발표에서는** — 진행자는 Copilot Studio의 'Add knowledge' 메뉴를 보여주며, 이 커넥터들이 Microsoft 365 Copilot(프리미엄 포함)에서는 제공되지 않는 Copilot Studio만의 차별점이라고 설명했다.

## 🧭 추구 방향과 흐름

- **로우코드/노코드 방식의 AI 에이전트 구축** — 발표 전체가 코드를 작성하지 않고 프롬프트와 클릭만으로 environment 생성부터 에이전트 배포까지 이어지는 흐름을 보여주었다. 이는 비개발자도 기업용 AI 에이전트를 직접 만들 수 있게 하려는 Copilot Studio의 방향성을 드러낸다.
- **ALM 기반의 단계적 배포** — 진행자는 앱이나 에이전트를 곧바로 운영 데이터에 투입하지 않고 개발-테스트-운영 단계를 거치는 ALM 원칙을 강조했다. Environment와 Solution 개념이 이 단계적 배포를 뒷받침하는 구조로 설명되었다.
- **플랫폼 확장성과 데이터 소스 다양화** — Copilot Studio가 Microsoft 365 Copilot 대비 더 많은 LLM 선택지와 지식 소스(Confluence, Databricks, Salesforce 등)를 지원한다는 점이 반복적으로 강조되었다. 이는 엔터프라이즈 환경에서 이기종 데이터 소스를 통합하려는 방향성을 보여준다.

## 💬 Q&A 하이라이트

<details><summary>Q. environment를 만드는 게 정확히 무엇을 하는 것인가?</summary><p>environment는 클라우드 테넌트 안에서 보안, 데이터 상주, 소비량, 데이터 격리 등의 이유로 분리한 작업 공간이며, 여기에 앱·에이전트·데이터·자동화가 저장된다.</p></details>

<details><summary>Q. 실습에서 'compare' 기능으로 레코드를 만드는 이유가 무엇인가?</summary><p>이 캔버스 앱은 이미 만들어진 데모 앱으로, 실제 업무 로직을 깊이 이해할 필요 없이 이후 에이전트가 조회할 더미 레코드를 데이터베이스에 채워 넣기 위한 인터페이스일 뿐이다.</p></details>

<details><summary>Q. 에이전트를 만드는 과정에서 토큰이나 크레딧이 소비되는가?</summary><p>최신 인터페이스에서는 에이전트 생성 시 Copilot credit이 소비된다고 표시되지만, 예전 인터페이스에 이 변경이 동일하게 적용되었는지는 Microsoft 측의 공식 확인이 아직 없다.</p></details>

<details><summary>Q. 왜 새 인터페이스가 아니라 예전(classic) 인터페이스로 진행하는가?</summary><p>실습 자료(instruction)가 예전 인터페이스 기준으로 작성되어 있고, 새 인터페이스에는 아직 해당 가이드가 제공되지 않기 때문이다.</p></details>

<details><summary>Q. 에이전트의 크레딧 소비 현황을 확인할 방법이 있는가?</summary><p>관리자(administrator) 권한이 있으면 monitor 메뉴에서 성공률과 함께 billing(청구/소비) 정보를 확인할 수 있다.</p></details>

<details><summary>Q. Copilot Studio가 여러 지식 소스를 연결할 수 있는 건 데모 계정이라 가능한 것인가?</summary><p>아니다. Microsoft 365 Copilot은 프리미엄 라이선스를 사용해도 Azure AI Search, Salesforce, Confluence, Databricks 같은 지식 소스를 지원하지 않으며, 이는 Copilot Studio라는 플랫폼 자체의 차별화된 기능이다.</p></details>

## 🚀 바로 활용하기

1. Microsoft Power Platform에서 트라이얼/데모 environment를 만들어 Copilot Studio에 직접 로그인해본다.
2. 간단한 프롬프트만으로 에이전트를 생성해보고, LLM 선택 옵션과 'Add knowledge' 메뉴에서 제공되는 커넥터 목록을 비교해본다.
3. Power Platform ALM 문서를 읽고 solution을 통한 환경 간 이동(개발→테스트→운영) 절차를 익힌다.
4. 관리자 권한이 있다면 Copilot Studio의 monitor/billing 메뉴에서 에이전트별 크레딧 소비량을 확인해본다.

## 🔗 참고 자료

- [Microsoft Copilot Studio 공식 문서](https://learn.microsoft.com/microsoft-copilot-studio/) — 에이전트 생성, LLM 선택, 지식 소스, 도구, 트리거 등 본문에서 다룬 핵심 기능의 공식 문서
- [Power Platform ALM 개요](https://learn.microsoft.com/power-platform/alm/overview) — 발표에서 설명한 개발-테스트-운영 단계별 배포(ALM) 개념의 공식 설명
- [Power Apps 공식 홈페이지](https://powerapps.microsoft.com/) — 실습에서 사용한 canvas app을 만드는 Power Apps 제품 소개
- [Power Platform Environments 개요](https://learn.microsoft.com/power-platform/admin/environments-overview) — 본문에서 설명한 environment 개념(보안·데이터 상주·소비량 분리)의 공식 문서
