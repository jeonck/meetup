---
title: "2026-10-24 Microsoft Sentinel × Defender XDR × Agentic AI: 통합 SOC와 KQL이 만드는 보안 운영의 다음 단계"
date: 2026-10-24T01:18:50.674103+09:00
tags: ["microsoft-sentinel", "kql", "agentic-ai"]
---
## 왜 '통합 보안 운영 플랫폼'인가

Microsoft는 클라우드 네이티브 SIEM인 Sentinel과 XDR 솔루션인 Defender XDR을 하나의 Defender 포털 안에 통합했다. [Microsoft Learn의 Defender XDR 업데이트 페이지](https://learn.microsoft.com/en-NZ/defender-xdr/whats-new)에 따르면 이 통합 플랫폼은 2024년 중반 정식 출시(GA)되었고, 초기에는 테넌트당 하나의 Sentinel 워크스페이스만 지원하다가 2025년 중반에 멀티 워크스페이스 지원이 추가되는 등 지속적으로 기능이 확장되어 왔다. 핵심은 '툴 전환 피로'를 줄이는 것이다. 엔드포인트, 아이디, 이메일, SaaS 앱, 클라우드 워크로드를 넘나드는 탐지·조사·대응을 단일 데이터 모델과 단일 인시던트 큐에서 처리하도록 만든 것으로, [Petri의 분석](https://petri.com/microsofts-unified-security-operations-platform/)은 이를 '산업 최고 수준의 SIEM과 포괄적 XDR, 보안 전용 생성형 AI의 결합'으로 설명한다.

## KQL: 통합의 바닥을 지탱하는 공통 언어

이 통합이 실제로 동작하려면 서로 다른 로그 소스를 하나의 질의 언어로 다룰 수 있어야 한다. 그 역할을 하는 것이 KQL(Kusto Query Language)이다. [Microsoft의 공식 Kusto 문서](https://learn.microsoft.com/en-us/kusto/query)는 KQL을 '텔레메트리, 메트릭, 로그를 질의하는 데 최적화된 언어'로 정의하며, 파이프(`|`)로 연결되는 읽기 전용 질의 파이프라인 구조, 시계열 연산자, 텍스트 파싱, 벡터 유사도 검색까지 지원한다고 설명한다. 이 언어는 Sentinel뿐 아니라 Azure Monitor, Microsoft Fabric, Azure Data Explorer에서도 동일하게 쓰이기 때문에, 한 번 익힌 분석 로직(advanced hunting 쿼리)을 플랫폼 전체에서 재사용할 수 있다는 것이 실무적으로 큰 장점이다.

## Agentic AI가 SOC에 들어오는 방식

통합 데이터 위에 얹히는 것이 Security Copilot의 에이전트형 AI다. [Dark Reading 보도](https://www.darkreading.com/cybersecurity-operations/microsoft-gives-security-copilot-autonomy)에 따르면 Microsoft는 2025년 피싱 트리아지, 조건부 액세스 최적화, 취약점 대응 등을 담당하는 자체 에이전트와 파트너 에이전트를 공개 프리뷰로 전환했고, [Petri의 후속 보도](https://petri.com/microsoft-security-copilot-ai-agentic-capabilities/)는 이를 알럿 트리아지 업무를 보강하는 '분석가를 대체하지 않고 돕는' 봇으로 규정한다. 이 방향은 업계 전체의 흐름과도 맞물린다. [Gartner의 2026년 자료](https://www.gartner.com/en/documents/8513777)는 'SOC of 2030'으로 가는 여정에서 AI 기반을 먼저 다지고, 증강된 운영을 시범 적용한 뒤 지능형 운영으로 넘어가라고 권고하며, 2025년 'Predict' 리포트에서는 이미 '완전 자율 SOC는 결코 없을 것'이라는 입장을 밝힌 바 있다. 즉 업계 컨센서스는 완전 자동화가 아니라 사람과 AI가 함께 일하는 증강(augmentation) 모델이다.

## 도입을 고려한다면

이 흐름이 중요한 이유는 숫자에 있다. [Trend Micro의 설문](https://trendmicro.com/en_hk/about/newsroom/press-releases/2021/2021-06-02.html)은 응답자의 70%가 알럿 양에 '감정적으로 압도당한다'고 답했다고 보고했는데, 알럿 피로는 수년째 SOC의 만성 문제였다. KQL 기반 탐지 룰과 Agentic AI 트리아지는 이 반복 업무의 1차 필터 역할을 맡아 분석가가 실제 판단이 필요한 사안에 집중하도록 돕는 구조다. 다만 모든 자료가 공통적으로 강조하듯, 에이전트의 판단에는 여전히 사람의 검토와 피드백 루프가 필요하다. 조직 입장에서는 먼저 KQL로 자체 데이터 소스에 맞는 탐지 로직을 확보하고, 그 위에 에이전트를 단계적으로 붙여 신뢰 구간을 넓혀가는 순서가 현실적인 도입 경로다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Kusto Query Language (KQL) overview - Microsoft Learn](https://learn.microsoft.com/en-us/kusto/query) — KQL의 정의, 파이프 기반 쿼리 구조, 지원 범위(Sentinel·Fabric·Azure Monitor)를 뒷받침
- [What's new in Microsoft Defender XDR](https://learn.microsoft.com/en-NZ/defender-xdr/whats-new) — Sentinel-Defender XDR 통합 플랫폼의 GA 시점과 멀티 워크스페이스 지원 확장 시점을 뒷받침
- [Microsoft's Unified Security Operations Platform Delivers Comprehensive End-to-End Protection - Petri](https://petri.com/microsofts-unified-security-operations-platform/) — 통합 플랫폼의 구성요소(SIEM+XDR+생성형 AI)와 단일 데이터 모델 설명을 뒷받침
- [Microsoft gives Security Copilot autonomy - Dark Reading](https://www.darkreading.com/cybersecurity-operations/microsoft-gives-security-copilot-autonomy) — Security Copilot 에이전트 출시 배경과 분석가 업무 보강 역할을 뒷받침
- [Microsoft Expands Security Copilot with New AI Agentic Capabilities - Petri](https://petri.com/microsoft-security-copilot-ai-agentic-capabilities/) — 피싱 트리아지, 조건부 액세스 최적화 등 구체 에이전트 목록을 뒷받침
- [Gartner Insights Abstract (SOC of 2030 / A-SOC)](https://www.gartner.com/en/documents/8513777) — 에이전틱 SOC로 가는 단계적 로드맵(AI 기반 구축→증강 운영→지능형 운영) 권고를 뒷받침
- [70% Of SOC Teams Emotionally Overwhelmed By Security Alert Volume - Trend Micro](https://trendmicro.com/en_hk/about/newsroom/press-releases/2021/2021-06-02.html) — 알럿 피로 문제의 심각성(70% 응답)을 수치로 뒷받침
