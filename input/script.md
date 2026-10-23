<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
제공해주신 NetCom Learning의 강의 자료("Microsoft Security for Agentic AI: Threat Detection & Response with Defender and Sentinel", 강사: Ankul Bhardwaj) 기반의 **핵심 요약**은 다음과 같습니다.

---

## 1. 세션 개요 및 학습 목표

* **주요 내용:** AI 에이전트 및 클라우드 환경에서의 위협 지형 이해, 현대적 SecOps 아키텍처 구축, Defender XDR과 Microsoft Sentinel을 활용한 위협 조사, KQL(Kusto Query Language)을 이용한 헌팅 및 탐지 개발, 그리고 AI 보안 사고 대응.
* **핵심 목표:** 각 Microsoft 보안 서비스의 역할 이해, 교차 도메인 증거 조사, 에이전트 식별자·데이터·도구 보호 및 책임감 있는 사고 대응/복구 체계 확립.

## 2. 위협 지형 (Threat Landscape) 및 에이전트 위험

* **클라우드 위협:** 여전히 ID 중심의 공격(비밀번호 스프레이, 피싱, 토큰/세션 도용, 권한 남용 등)이 클라우드 보안 사고의 주원인입니다.
* **에이전트 보안 위협:** AI 에이전트는 컨텍스트(직·간접 프롬프트 인젝션, 민감 정보 유출), 실행/종속성(과도한 권한, 악성 도구 호출, 취약한 플러그인 및 공급망) 영역에서 새로운 공격 경로에 노출됩니다.

## 3. 현대적 SecOps 및 Microsoft 보안 아키텍처

* **통합 보안 체계:** Microsoft Entra(ID), Defender for Cloud/Cloud Apps(워크로드/SaaS), Purview(데이터 보호)가 결합하여 통합 텔레메트리 및 정책 경계를 제공합니다.
* **Defender XDR & Sentinel 연동:**
* **Defender XDR:** 엔드포인트, ID, 이메일, SaaS 간의 알림과 엔티티를 연결하여 공격 시나리오(Incident)를 추적합니다.
* **Microsoft Sentinel:** 다양한 소스의 로그를 수집·정규화(ASIM)하고, 분석 규칙과 플레이북을 통해 자동화된 대응 및 위협 헌팅을 수행합니다. (※ Azure 포털 지원은 2027년 3월 31일 이후 종료되며 Defender 포털로 통합 전환 진행 중)



## 4. 고급 위협 헌팅 (Advanced Hunting & KQL)

* **KQL 활용:** 가설 기반의 위협 헌팅을 위해 로그인 실패/성공 패턴 분석, 새로운 서비스 프롬프트/IP 페어 탐지, 엔드포인트 영속성(`schtasks.exe` 등) 조사, Defender와 Sentinel 간의 ID 상관관계 분석 등 KQL 쿼리 패턴을 제공합니다.

## 5. AI 워크로드 및 에이전트 보안 (Agent 365)

* **보안 설계 패턴:** 명확한 신원 소유자, 범위가 지정된 권한, 승인된 데이터 검색, 모델/오케스트레이션 경계, 툴 및 런타임 격리, 모니터링 및 복구 체계가 필요합니다.
* **수명주기 관리:** 설계 단계의 위협 모델링부터 배포 후 가드레일, 레드팀 테스트, 에이전트 관측 가능성(Observability) 확보를 통해 의도한 효과와 실제 실행 결과를 추적해야 합니다.

---

추가로 특정 섹션에 대한 상세한 설명이나 KQL 쿼리 분석 등이 필요하신가요?
```
