# Meetup Insights (meetup)

밋업에서 수집한 녹취 스크립트(STT 결과물)를 붙여넣으면, Claude가 분석해
밋업 요약 · 핵심 요점 · 기술 해설 · 추구 방향 · Q&A · 실천 항목 · 참고 링크로
구성된 한국어 포스트를 자동 게시하는 사이트.

사이트: https://meetup.metacog.co.kr/

## 어떻게 동작하나

```
input/script.md (밋업 스크립트 전체를 코드블록에 붙여넣기, GitHub 웹 UI에서 수정)
        │
        ▼  저장(커밋)하는 순간 push 후킹으로 즉시 실행 + 매일 07:00 KST 크론
pipeline/generate.py
  - 코드블록 전체를 스크립트 1개로 읽음 (`---` 구분선으로 여러 개 가능)
  - 이미 게시된 스크립트(해시 기준)는 건너뜀 — pipeline/state.json 으로 추적
  - 입력이 비어 있으면 기술 토픽 풀에서 그날의 항목으로 미니 기술 브리프 생성
  - Claude가 스크립트를 분석해 섹션 구성:
      📋 밋업 한눈에 보기 / 🔑 핵심 요점 / 🛠 핵심 기술 쉽게 이해하기 /
      🧭 추구 방향과 흐름 / 💬 Q&A 하이라이트 (토글) /
      🚀 바로 활용하기 / 🔗 참고 자료 (객관성 근거용 공식 문서 링크)
  - content/posts/YYYY-MM-DD-....md 로 저장
        │
        ▼  변경사항 커밋 & push
Hugo build → GitHub Pages 배포 (meetup.metacog.co.kr)
```

## 사용하는 방법

1. GitHub 저장소에서 [`input/script.md`](input/script.md) 파일을 연다.
   (블로그 상단 "Add Transcript ✏️" 버튼으로 바로 이동 가능)
2. 연필(✏️) 아이콘을 눌러 편집 모드로 들어간다.
3. 코드블록(```) 안에 밋업 스크립트 전체를 붙여넣는다. 여러 밋업을 한꺼번에
   처리하려면 `---` 만 있는 줄로 구분한다 — 블록마다 포스트가 하나씩 생성된다.
4. 우측 상단 "Commit changes"로 저장한다. **저장하는 순간 GitHub Actions가
   후킹되어 즉시 분석·게시가 시작된다** (로컬 git 작업 불필요).
5. 몇 분 뒤 사이트에 새 포스트가 올라온다.

이미 게시에 사용된 스크립트는 파일에 그대로 남아있어도 다시 게시되지 않는다
(텍스트 해시 기준 dedup). Actions 탭 → "Daily meetup post" → "Run workflow"로 수동
실행도 가능하다.

### 입력이 없는 날 — 미니 기술 브리프

코드블록을 비워두면 매일 07:00 KST 크론이 `pipeline/generate.py`의
`FALLBACK_QUOTES`(클라우드 네이티브 기술 토픽 풀)에서 그날의 토픽을 골라 미니
기술 브리프 포스트를 생성한다. 풀을 비우면(`FALLBACK_QUOTES = []`) 이 기능이 꺼진다.

### 참고 자료 링크의 객관성

포스트의 🔗 참고 자료 섹션은 본문 주장을 뒷받침하는 공식 프로젝트 홈페이지/문서
루트만 넣도록 프롬프트에서 강제하며, `parse_result()`가 http URL이 없는 항목을
걸러낸다. 깊은 경로의 링크(블로그 글 등)는 환각 위험 때문에 생성하지 않는다.

## 최초 설정 (1회만, 사람이 직접 해야 하는 단계)

자동 생성 단계는 Claude Code CLI를 사용한다. GitHub Actions에서 이 CLI를 인증하려면
Claude 구독 계정으로 발급한 OAuth 토큰을 저장소 Secret으로 등록해야 한다. 이 과정은
브라우저 로그인이 필요해 에이전트가 대신할 수 없다.

```bash
claude setup-token
```

터미널에 표시되는 인증 코드를 브라우저에 붙여넣고 로그인하면, **그 다음에** 터미널에
`sk-ant-oat01-...` 로 시작하는 토큰이 출력된다. (브라우저에 표시된 인증 코드 자체가
아니라, 붙여넣은 뒤 터미널에 최종 출력되는 토큰이어야 한다.)

```bash
gh secret set CLAUDE_CODE_OAUTH_TOKEN --repo jeonck/meetup
# 위 토큰을 붙여넣기
```

등록 후 Actions 탭에서 워크플로를 한 번 수동 실행(`workflow_dispatch`)해 정상 동작을
확인한다.

## 커스텀 도메인 (meetup.metacog.co.kr)

hosting.co.kr DNS 관리 화면에서 CNAME 레코드 1개를 추가해야 한다:

| 호스트 | 타입 | 값 |
|---|---|---|
| meetup | CNAME | jeonck.github.io. |

(talktime.metacog.co.kr과 동일한 방식.) 레코드가 전파되면 GitHub Pages가 자동으로
HTTPS 인증서를 발급한다. `static/CNAME`과 Pages 설정에는 이미 도메인이 등록돼 있다.

## 저장소 구조

| 경로 | 역할 |
|---|---|
| `input/script.md` | 밋업 스크립트 붙여넣는 곳 (사람이 수정 — 저장 즉시 후킹 실행) |
| `pipeline/generate.py` | 스크립트 분석 → Hugo 포스트 작성. 도메인 설정은 파일 상단 "도메인 설정" 블록 |
| `pipeline/state.json` | 게시에 사용된 스크립트 해시 목록 (중복 게시 방지) |
| `content/posts/` | 생성된 포스트 |
| `.github/workflows/daily.yml` | push 후킹 + 매일 07:00 KST 생성/배포 워크플로 |
| `themes/PaperMod` | Hugo 테마 (git submodule) |
| `assets/css/extended/cards.css` | 카드 그리드 레이아웃 + PaperMod 여백 버그 수정 |
| `assets/css/extended/quiz.css` | Q&A `<details>` 토글 스타일 |
| `static/CNAME` | 커스텀 도메인 (meetup.metacog.co.kr) |

## 로컬에서 테스트

```bash
hugo server -D                           # http://localhost:1313/
python3 pipeline/generate.py --dry-run   # 파일 생성 없이 결과만 확인
```

로컬에는 `claude` CLI 로그인 세션이 있으면 그대로 사용되고(`JUDGE_BACKEND=claude-code`),
없으면 `ANTHROPIC_API_KEY` 를 설정해 `JUDGE_BACKEND=api` 로 실행할 수 있다.
