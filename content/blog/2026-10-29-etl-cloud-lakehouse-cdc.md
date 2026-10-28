---
title: "2026-10-29 ETL의 재해석: Cloud Lakehouse와 실시간 CDC가 이끄는 데이터 아키텍처 전환"
date: 2026-10-29T08:53:44.570139+09:00
tags: ["data-lakehouse", "streaming-etl", "cdc"]
---
## 왜 지금 'ETL 현대화'가 화두인가

최근 밋업에서는 전통적인 ETL(Extract-Transform-Load) 방식이 한계에 부딫혀 클라우드 기반 아키텍처로 옮겨가야 한다는 메시지가 반복적으로 등장했다. 실제로 업계 동향을 보면 2025년 들어 대부분의 조직이 ETL 대신 ELT(Extract-Load-Transform)를 선호하는 쪽으로 이동하고 있다. 원본 데이터를 먼저 적재한 뒤 필요할 때 재모델링할 수 있다는 유연성 때문인데, [Domo의 Modern Data Stack 가이드](https://domo-webflow.domo.com/glossary/modern-data-stack)는 이를 2025년 데이터 스택의 핵심 특징으로 꼽는다. 데이터의 양과 다양성이 폭증한 지금, 고정된 스키마를 미리 설계하는 ETL 방식은 변화에 대응하기 어렵기 때문이다.

## Lakehouse: 웨어하우스와 레이크의 경계가 사라지다

트랜스포메이션을 어디서, 어떻게 수행할지에 대한 답으로 업계는 Lakehouse 아키텍처로 수렴하고 있다. Databricks의 [공식 문서](https://docs.databricks.com/aws/en/lakehouse-architecture)는 Lakehouse를 데이터 레이크와 데이터 웨어하우스의 하이브리드로 정의하며, Delta Lake가 저장 계층에서 ACID 트랜잭션과 스키마 강제(enforcement)를 제공하고 Unity Catalog가 거버넌스를 담당하는 구조를 제시한다. 원시 데이터가 들어오는 raw layer부터 정제된 분석용 테이블까지 단계적으로 품질을 높여가는 'medallion architecture' 패턴이 사실상 표준으로 자리잡았다. Apache Iceberg, Hudi 같은 오픈 테이블 포맷의 등장으로 웨어하우스와 레이크 간의 구분이 더욱 희미해지고 있다는 점도 [DSStream의 데이터 엔지니어링 전망](https://www.dsstream.com/post/the-future-of-data-engineering---trends-to-watch-in-2025)에서 확인할 수 있다.

## 실시간 수집: CDC와 스트리밍이 기본값으로

배치 중심의 야간 ETL 잡으로는 비즈니스가 요구하는 속도를 맞출 수 없다는 공감대도 뚜렷하다. Change Data Capture(CDC)는 데이터베이스의 트랜잭션 로그를 직접 읽어 변경분만 저지연으로 전파하는 방식으로, 폴링이나 트리거 기반 방식보다 운영 부담과 지연시간이 훨씬 낮다. [Fivetran](https://www.fivetran.com/blog/change-data-capture-what-it-is-and-how-to-use-it)이나 Debezium 같은 도구가 이 패턴의 표준 구현체로 꼽힌다. 여기에 Apache Kafka 기반 스트리밍 ETL이 결합되면서, Confluent는 Kafka Connect로 데이터를 수집하고 Kafka Streams나 ksqlDB로 즉시 변환한 뒤 싱크 커넥터로 적재하는 파이프라인을 [실시간 스트리밍 ETL 튜토리얼](https://www.confluent.io/blog/building-real-time-streaming-etl-pipeline-20-minutes/)에서 상세히 안내한다. Redpanda 역시 [동일한 패턴](https://redpanda.com/guides/kafka-tutorial/etl-pipeline)을 통해 여러 다운스트림 시스템이 하나의 스트림을 동시에 소비하는 fan-out 구조의 장점을 강조한다.

## 실무 도입을 위한 조언

이러한 흐름을 따라가려는 팀이라면, 먼저 레거시 ETL(SSIS, Informatica, Talend 등)을 전부 교체하기보다 신규 데이터 소스부터 CDC·스트리밍 기반으로 전환하는 점진적 접근이 현실적이다. Monte Carlo의 [2025 데이터 엔지니어링 전망](https://info.montecarlodata.com/get-resources/2025-data-engineering-trends)은 혁신보다 신뢰성, 데이터 품질, 비용 최적화를 함께 고려하라고 조언하는데, 이는 밋업에서 발표자가 반복해서 언급한 '데이터를 머신러닝·분석에 바로 활용 가능한 상태로 유지하는 것'의 중요성과도 일치한다. 결국 ETL 현대화는 단순한 도구 교체가 아니라, 데이터를 생성 즉시 신뢰할 수 있는 형태로 흘려보내는 파이프라인 문화로의 전환이라고 볼 수 있다.

## 🔗 참고 자료 (작성 중 열람한 자료)

- [Domo - The Modern Data Stack in 2025](https://domo-webflow.domo.com/glossary/modern-data-stack) — ETL에서 ELT로 전환되는 2025년 데이터 스택 트렌드를 뒷받침
- [Databricks - Introduction to the well-architected data lakehouse](https://docs.databricks.com/aws/en/lakehouse-architecture) — Lakehouse 아키텍처(Delta Lake, Unity Catalog, medallion 패턴) 정의의 공식 근거
- [DSStream - The Future of Data Engineering: Trends to Watch in 2025](https://www.dsstream.com/post/the-future-of-data-engineering---trends-to-watch-in-2025) — 웨어하우스-레이크 경계 소멸 및 Iceberg/Hudi 등 오픈 테이블 포맷 확산 근거
- [Fivetran - Change Data Capture: What It Is and How to Use It](https://www.fivetran.com/blog/change-data-capture-what-it-is-and-how-to-use-it) — CDC가 로그 기반으로 저지연 실시간 수집을 구현하는 방식 설명
- [Confluent - Building a Real-Time Streaming ETL Pipeline in 20 Minutes](https://www.confluent.io/blog/building-real-time-streaming-etl-pipeline-20-minutes/) — Kafka Connect/Streams 기반 실시간 스트리밍 ETL 파이프라인 구조의 근거
- [Redpanda - Understanding Apache Kafka ETL Pipeline](https://redpanda.com/guides/kafka-tutorial/etl-pipeline) — 스트리밍 파이프라인의 fan-out 소비 구조 및 저지연 이점 근거
- [Monte Carlo - How will data engineering evolve in 2025?](https://info.montecarlodata.com/get-resources/2025-data-engineering-trends) — 신뢰성·품질·비용 최적화를 혁신과 병행해야 한다는 실무 도입 조언의 근거
