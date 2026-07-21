#!/usr/bin/env python3
"""Meetup insights pipeline — 밋업 녹취 스크립트 → 정리 + 기술 리서치 포스트.

input/script.md 코드블록에 붙여넣은 밋업 스크립트 전체를 하나의 항목으로 읽어,
Claude로 분석해 다음 섹션으로 구성된 한국어 포스트를 생성한다:
  - 밋업 한눈에 보기 (요약)
  - 핵심 요점 (Key Takeaways)
  - 핵심 기술 쉽게 이해하기 (기술별: 무엇인가/왜 필요한가/발표에서는)
  - 추구 방향과 흐름 (트렌드·지향점)
  - Q&A 하이라이트 (토글 아코디언)
  - 바로 활용하기 (실천 항목)
  - 참고 자료 (객관성 근거용 공식 문서 링크)

추가로, 같은 스크립트의 핵심 기술과 추구 방향을 소재로 웹 검색으로 자료를 조사해
참조 링크(작성 중 열람한 자료)를 포함한 리서치 글을 content/blog/ 에 별도 게시한다.

코드블록 안에서 `---` 만 있는 줄로 구분하면 스크립트 여러 개를 각각 별도 포스트로
처리한다. 이미 게시에 사용된 스크립트(텍스트 해시 기준)는 다시 나타나도 건너뛴다.
밋업 포스트와 블로그 글은 독립 dedup(`h` / `blog::h`)이라 한쪽 실패 시 그쪽만
재시도된다. 입력이 비어 있으면 FALLBACK_QUOTES(기술 토픽 풀)에서 그날의 항목을
대신 사용한다(폴백 항목에는 블로그 글을 만들지 않는다).

Usage:
    python pipeline/generate.py [--dry-run]

Env:
    JUDGE_BACKEND            "claude-code" | "api" (기본: 자동 — claude CLI가 있으면
                             claude-code, 없으면 api)
    CLAUDE_CODE_OAUTH_TOKEN  claude-code 백엔드 CI 인증 (claude setup-token으로 발급,
                             로컬은 claude 로그인 세션 사용)
    ANTHROPIC_API_KEY        api 백엔드 필수
    CLAUDE_MODEL             생성 모델 (기본 claude-sonnet-5)
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SENTENCE_FILE = ROOT / "input" / "script.md"
STATE_FILE = ROOT / "pipeline" / "state.json"
CONTENT_DIR = ROOT / "content" / "posts"
BLOG_DIR = ROOT / "content" / "blog"

KST = timezone(timedelta(hours=9))

# ============================== 도메인 설정 =================================
# 이 블록만 새 프로젝트 주제에 맞게 교체한다. 아래 엔진 코드는 건드릴 필요 없다.

# input/script.md 가 비어 있을 때 대신 쓰는 항목 풀 — 클라우드 네이티브 기술 토픽.
# 스크립트가 없는 날에도 토픽 하나를 앵커로 미니 기술 브리프 포스트가 생성된다.
FALLBACK_QUOTES = [
    {"text": "Platform Engineering", "author": ""},
    {"text": "GitOps", "author": ""},
    {"text": "Internal Developer Platform (IDP)", "author": ""},
    {"text": "Kubernetes Operators & CRDs", "author": ""},
    {"text": "Service Mesh", "author": ""},
    {"text": "eBPF Networking", "author": ""},
    {"text": "Policy as Code", "author": ""},
    {"text": "Infrastructure as Code with Crossplane", "author": ""},
    {"text": "Zero Trust Networking", "author": ""},
    {"text": "AI Agents for Operations (AIOps)", "author": ""},
]

# Claude에게 부여할 역할/톤
SYSTEM_PROMPT = """You are a senior tech-community editor for a Korean developer \
blog. You analyze raw meetup transcripts (imperfect speech-to-text output with \
fillers, mishearings, garbled tech terms, and mixed speakers is expected — infer the \
intended technology names from context, e.g. "crossbane" means Crossplane, \
"citium" means Cilium) and turn them into clear, practical Korean write-ups that a \
junior developer can understand. Write all body text in natural Korean, but keep \
technology names, product names, and code identifiers in English. Ground every claim \
in the transcript; never invent statements the speakers did not make. For the \
references section, provide only URLs you are highly confident exist: official \
project homepages and documentation roots (e.g. https://kubernetes.io, \
https://argo-cd.readthedocs.io, https://www.crossplane.io, https://cilium.io, \
https://istio.io, https://kyverno.io, https://dora.dev, https://www.cncf.io). \
Never fabricate deep links or blog URLs you are unsure about."""

# {sentence} / {note} 두 자리를 반드시 유지. JSON 스키마의 이중 중괄호는 str.format()
# 이스케이프이므로 스키마를 고칠 때도 그대로 유지한다.
GENERATE_PROMPT = """Below is a raw transcript from a tech meetup \
(speech-to-text output; it contains fillers, transcription errors, garbled \
technology names, and multiple speakers).{note} Analyze it and produce a Korean \
write-up. Respond ONLY with JSON in exactly this format, no other text:

{{"title": "짧은 한국어 제목 (기술 용어는 영어 유지)",
 "summary": "밋업에서 무슨 이야기가 오갔는지 3-4문장 한국어 요약",
 "takeaways": ["밋업의 핵심 요점 한 줄 (한국어)"],
 "technologies": [
   {{"name": "기술/도구 이름 (영어)",
     "what": "이 기술이 무엇인지 초심자도 이해할 수 있는 2-3문장 한국어 설명",
     "why": "어떤 문제를 풀기 위해 쓰는지 1-2문장",
     "in_talk": "발표에서 이 기술이 어떻게 다뤄졌는지 1-2문장"}}
 ],
 "directions": [
   {{"theme": "발표가 추구하는 방향/트렌드 이름",
     "detail": "그 방향이 무엇이고 발표의 어떤 내용이 근거인지 2-3문장 한국어 설명"}}
 ],
 "qa": [
   {{"question": "청중 질문의 요지 (한국어)",
     "answer": "발표자 답변의 요지 (한국어, 1-3문장)"}}
 ],
 "actions": ["독자가 당장 시도해볼 수 있는 구체적 실천 항목 (한국어)"],
 "references": [
   {{"title": "자료 이름", "url": "https://...",
     "note": "이 링크가 본문의 어떤 내용을 뒷받침하는지 한 줄"}}
 ],
 "tags": ["kebab-case-tag", "max 3"]}}

Requirements:
- takeaways: 4-7 items, each a self-contained sentence a reader can skim.
- technologies: 3-6 items, ordered by importance in the talk. Explanations must be
  easy — assume the reader has heard the name but never used the tool. Fix garbled
  STT names to the real technology (Crossplane, Cilium, Istio, Argo CD, Kyverno,
  kagent, Prometheus, Loki, cert-manager, ...) only when the context makes the
  intended tool clear.
- directions: 2-4 items capturing what the speaker/community is aiming for
  (e.g. platform as a product, self-service, zero trust, shift-left).
- qa: include ONLY question-answer exchanges actually present in the transcript;
  empty array if there was no Q&A.
- actions: 2-4 concrete first steps (install X and try Y, read Z docs, ...).
- references: 4-8 items. Official project homepages / documentation roots only —
  these give readers objective backing for the write-up. No fabricated URLs.
- All body text in Korean; technology names stay in English.

Transcript:
{sentence}"""

QUOTE_NOTE = (
    " Actually, there is no meetup transcript today. Instead, write a compact"
    " Korean tech brief anchored on this topic: treat it as the first item in"
    " \"technologies\", add 2-3 closely related technologies, describe the"
    " direction the ecosystem is heading in \"directions\", leave \"qa\" as an"
    " empty array, and base \"actions\" and \"references\" on how a reader would"
    " start learning it."
)

# ── 블로그(리서치) 생성 ──
# 밋업 스크립트의 핵심 기술과 추구 방향을 소재로, 웹 검색으로 자료를 실제 조사해
# 참조 링크를 포함한 별도의 리서치 글을 content/blog/ 에 게시한다.
# claude-code 백엔드는 WebSearch 툴, api 백엔드는 서버측 web_search 툴을 사용한다.

BLOG_SYSTEM_PROMPT = """You are a tech researcher-writer for a Korean developer \
blog. You receive a raw meetup transcript, identify its core technologies and the \
direction the speaker/community is pursuing, and then RESEARCH those topics on the \
web before writing. You MUST use the web search tool to look up current, factual \
material (official docs, project pages, research reports) and you may only cite \
URLs that actually appeared in your search results — never invent or guess a URL. \
Write all body text in natural Korean; keep technology names in English. The \
article must stand on researched evidence: every major claim should be traceable \
to one of the cited sources."""

BLOG_PROMPT = """Below is a raw meetup transcript (imperfect speech-to-text). \
Your task is NOT to summarize the meetup. Instead:

1. Identify the 2-4 core technologies and the overall direction/trend the talk
   pursues (e.g. platform engineering, GitOps, zero trust, AI-assisted ops).
2. Use the web search tool to research each of them: official documentation,
   project pages, foundation/report pages (CNCF, DORA, etc.). Do enough searches
   to ground every major claim (typically 4-8 searches).
3. Write ONE in-depth Korean blog article (1200-2000 Korean characters of body)
   about those technologies and that direction — what they are, why the industry
   is moving that way, current state, and practical adoption advice.

Citation rules (critical, for objectivity):
- While writing, cite the sources you actually consulted as inline markdown
  links, e.g. "CNCF의 [연례 서베이](https://www.cncf.io/reports/)에 따르면 ...".
- Only cite URLs that appeared in your web search results. Never fabricate URLs.
- Every section should contain at least one cited source.

Respond ONLY with JSON in exactly this format, no other text:

{{"title": "블로그 글 제목 (한국어, 기술 용어는 영어 유지)",
 "body": "마크다운 본문. '## 소제목' 섹션 구조, 인라인 참조 링크 포함. 한국어.",
 "references": [
   {{"title": "열람한 자료 이름", "url": "https://...",
     "note": "이 자료가 본문의 어떤 주장을 뒷받침하는지 한 줄"}}
 ],
 "tags": ["kebab-case-tag", "max 3"]}}

The "references" array lists every source you consulted (searched and used),
including the ones cited inline. 4-8 items.

Transcript:
{sentence}"""

HEADING_BLOG_REFS = "🔗 참고 자료 (작성 중 열람한 자료)"

# 게시가 끝나면 input/script.md 를 이 최소 템플릿으로 되돌린다 (안내 한 줄 + 빈 코드블록).
# 실패한 스크립트가 하나라도 있으면 재시도를 위해 되돌리지 않는다.
RESET_TEMPLATE = """<!-- 밋업 스크립트(STT 전체)를 아래 코드블록 안에 붙여넣고 커밋하면 즉시 분석·게시됩니다. 여러 개는 `---` 줄로 구분 -->
```
```
"""

# 포스트 본문 섹션 제목
HEADING_INPUT = "📋 밋업 한눈에 보기"
HEADING_INPUT_QUOTE = "오늘의 기술 토픽"
HEADING_TAKEAWAYS = "🔑 핵심 요점"
HEADING_TECH = "🛠 핵심 기술 쉽게 이해하기"
HEADING_DIRECTIONS = "🧭 추구 방향과 흐름"
HEADING_QA = "💬 Q&A 하이라이트"
HEADING_ACTIONS = "🚀 바로 활용하기"
HEADING_REFS = "🔗 참고 자료"

# ============================ 도메인 설정 끝 =================================


def log(msg: str) -> None:
    print(msg, flush=True)


def sentence_hash(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
    return (slug or "meetup")[:60].rstrip("-")


def read_sentences() -> list[str]:
    """input/script.md 코드블록 안의 스크립트를 읽는다.

    코드블록 전체가 항목 하나. `---` 만 있는 줄로 구분하면 여러 스크립트를
    각각 별도 항목(= 별도 포스트)으로 처리한다.
    """
    if not SENTENCE_FILE.exists():
        log(f"오류: {SENTENCE_FILE} 파일이 없습니다")
        sys.exit(1)
    text = SENTENCE_FILE.read_text(encoding="utf-8")
    fenced = re.search(r"```[a-zA-Z]*\n(.*?)```", text, re.DOTALL)
    body = fenced.group(1) if fenced else text
    scripts = []
    for chunk in re.split(r"^\s*---+\s*$", body, flags=re.MULTILINE):
        chunk = chunk.strip()
        if chunk and not chunk.startswith("<!--"):
            scripts.append(chunk)
    return scripts


def fallback_quote_item(today) -> dict | None:
    """input이 비어 있을 때 사용할 항목 — 날짜 기준으로 풀을 순환 선택."""
    if not FALLBACK_QUOTES:
        return None
    idx = today.timetuple().tm_yday % len(FALLBACK_QUOTES)
    quote = FALLBACK_QUOTES[idx]
    return {
        "text": quote["text"],
        "source": quote.get("author") or "idiom",
        # 날짜를 해시에 포함 — 같은 항목이 몇 주 뒤 다시 나와도 새로 게시되도록
        "dedup_key": sentence_hash(f"{today.isoformat()}::{quote['text']}"),
    }


def build_queue(sentences: list[str], today) -> list[dict]:
    if sentences:
        return [
            {"text": s, "source": None, "dedup_key": sentence_hash(s)}
            for s in sentences
        ]
    fallback = fallback_quote_item(today)
    return [fallback] if fallback else []


class FatalAPIError(Exception):
    """재시도가 무의미한 오류(크레딧 부족, 인증 실패) — 실행 전체 중단."""


def is_fatal_api_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return any(marker in msg for marker in (
        "credit balance", "authenticat", "invalid x-api-key",
        "invalid api key", "invalid bearer token", "oauth token", "/login",
        "401",
    ))


def parse_result(text: str) -> dict | None:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    required = ("title", "summary")
    if not all(isinstance(data.get(k), str) and data.get(k) for k in required):
        return None
    for key in ("takeaways", "technologies", "directions", "qa", "actions", "references"):
        value = data.get(key) or []
        data[key] = value if isinstance(value, list) else []
    # references는 실제 http URL이 있는 항목만 유지 (환각 방지 최소 검증)
    data["references"] = [
        r for r in data["references"]
        if isinstance(r, dict) and str(r.get("url", "")).startswith("http")
    ]
    if not data["technologies"]:
        return None
    tags = data.get("tags") or []
    data["tags"] = [slugify(str(t)) for t in tags[:3] if str(t).strip()] or ["meetup-notes"]
    return data


def build_prompt(sentence: str, source: str | None) -> str:
    note = QUOTE_NOTE if source else ""
    return GENERATE_PROMPT.format(sentence=sentence, note=note)


def generate_api(client, model: str, sentence: str, source: str | None = None) -> dict | None:
    prompt = build_prompt(sentence, source)
    for attempt in (1, 2):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=8000,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:  # noqa: BLE001
            if is_fatal_api_error(exc):
                raise FatalAPIError(str(exc)) from exc
            log(f"  API 오류 (시도 {attempt}): {exc}")
            if attempt == 2:
                return None
            continue
        text = next((b.text for b in response.content if b.type == "text"), "")
        result = parse_result(text)
        if result:
            return result
        log(f"  JSON 파싱 실패 (시도 {attempt}): {text[:120]!r}")
    return None


def generate_cli(model: str, sentence: str, source: str | None = None) -> dict | None:
    prompt = build_prompt(sentence, source)
    env = os.environ.copy()
    env.pop("ANTHROPIC_API_KEY", None)
    cmd = ["claude", "-p", "--model", model, "--tools", "",
           "--output-format", "text", "--append-system-prompt", SYSTEM_PROMPT]
    for attempt in (1, 2):
        try:
            result = subprocess.run(cmd, input=prompt, env=env, timeout=360,
                                     capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            log(f"  CLI 타임아웃 (시도 {attempt})")
            continue
        if result.returncode != 0:
            err = (result.stderr or result.stdout).strip()
            if is_fatal_api_error(RuntimeError(err)):
                raise FatalAPIError(err[:300])
            log(f"  CLI 오류 (시도 {attempt}): {err[:200]}")
            if attempt == 2:
                return None
            continue
        parsed = parse_result(result.stdout)
        if parsed:
            return parsed
        log(f"  JSON 파싱 실패 (시도 {attempt}): {result.stdout[:120]!r}")
    return None


def parse_blog_result(text: str) -> dict | None:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    required = ("title", "body")
    if not all(isinstance(data.get(k), str) and data.get(k) for k in required):
        return None
    refs = data.get("references") or []
    data["references"] = [
        r for r in (refs if isinstance(refs, list) else [])
        if isinstance(r, dict) and str(r.get("url", "")).startswith("http")
    ]
    if not data["references"]:  # 열람 자료 없는 리서치 글은 게시하지 않음
        return None
    tags = data.get("tags") or []
    data["tags"] = [slugify(str(t)) for t in tags[:3] if str(t).strip()] or ["tech-research"]
    return data


def generate_blog_api(client, model: str, sentence: str) -> dict | None:
    prompt = BLOG_PROMPT.format(sentence=sentence)
    for attempt in (1, 2):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=8000,
                system=BLOG_SYSTEM_PROMPT,
                tools=[{"type": "web_search_20250305", "name": "web_search",
                        "max_uses": 8}],
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:  # noqa: BLE001
            if is_fatal_api_error(exc):
                raise FatalAPIError(str(exc)) from exc
            log(f"  블로그 API 오류 (시도 {attempt}): {exc}")
            if attempt == 2:
                return None
            continue
        text = "".join(b.text for b in response.content if b.type == "text")
        result = parse_blog_result(text)
        if result:
            return result
        log(f"  블로그 JSON 파싱 실패 (시도 {attempt}): {text[:120]!r}")
    return None


def generate_blog_cli(model: str, sentence: str) -> dict | None:
    prompt = BLOG_PROMPT.format(sentence=sentence)
    env = os.environ.copy()
    env.pop("ANTHROPIC_API_KEY", None)
    # --tools 는 노출 범위, --allowedTools 는 권한 승인 — CI(비대화형)에서는 둘 다
    # 있어야 WebSearch가 실제로 실행된다 (없으면 권한 요청 문구만 출력되고 실패).
    cmd = ["claude", "-p", "--model", model, "--tools", "WebSearch",
           "--allowedTools", "WebSearch",
           "--output-format", "text", "--append-system-prompt", BLOG_SYSTEM_PROMPT]
    for attempt in (1, 2):
        try:
            result = subprocess.run(cmd, input=prompt, env=env, timeout=600,
                                     capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            log(f"  블로그 CLI 타임아웃 (시도 {attempt})")
            continue
        if result.returncode != 0:
            err = (result.stderr or result.stdout).strip()
            if is_fatal_api_error(RuntimeError(err)):
                raise FatalAPIError(err[:300])
            log(f"  블로그 CLI 오류 (시도 {attempt}): {err[:200]}")
            if attempt == 2:
                return None
            continue
        parsed = parse_blog_result(result.stdout)
        if parsed:
            return parsed
        log(f"  블로그 JSON 파싱 실패 (시도 {attempt}): {result.stdout[:120]!r}")
    return None


def yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def html_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_post(sentence: str, result: dict, date: datetime, source: str | None = None) -> Path:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    base = f"{date.date().isoformat()}-{slugify(result['title'])}"
    path = CONTENT_DIR / f"{base}.md"
    n = 2
    while path.exists():
        path = CONTENT_DIR / f"{base}-{n}.md"
        n += 1

    tags = list(result["tags"])
    if source:
        tags = (tags + ["tech-brief"])[:4]
    tags_str = ", ".join(yaml_quote(t) for t in tags)

    sections = []

    if source:
        sections.append(f"## {HEADING_INPUT_QUOTE}\n\n> **{sentence}**\n\n{result['summary']}\n")
    else:
        sections.append(f"## {HEADING_INPUT}\n\n{result['summary']}\n")

    if result["takeaways"]:
        lines = [f"## {HEADING_TAKEAWAYS}\n"]
        lines.append("\n".join(f"- {t}" for t in result["takeaways"]))
        sections.append("\n".join(lines) + "\n")

    if result["technologies"]:
        lines = [f"## {HEADING_TECH}\n"]
        for item in result["technologies"]:
            lines.append(f"### {item.get('name', '')}\n")
            what = item.get("what", "")
            why = item.get("why", "")
            in_talk = item.get("in_talk", "")
            if what:
                lines.append(f"{what}\n")
            if why:
                lines.append(f"**왜 필요한가** — {why}\n")
            if in_talk:
                lines.append(f"**발표에서는** — {in_talk}\n")
        sections.append("\n".join(lines))

    if result["directions"]:
        lines = [f"## {HEADING_DIRECTIONS}\n"]
        for item in result["directions"]:
            theme = item.get("theme", "")
            detail = item.get("detail", "")
            lines.append(f"- **{theme}** — {detail}")
        sections.append("\n".join(lines) + "\n")

    if result["qa"]:
        lines = [f"## {HEADING_QA}\n"]
        for item in result["qa"]:
            question = html_escape(str(item.get("question", "")))
            answer = html_escape(str(item.get("answer", "")))
            lines.append(
                f"<details><summary>Q. {question}</summary>"
                f"<p>{answer}</p></details>\n"
            )
        sections.append("\n".join(lines))

    if result["actions"]:
        lines = [f"## {HEADING_ACTIONS}\n"]
        lines.append("\n".join(f"{i}. {a}" for i, a in enumerate(result["actions"], 1)))
        sections.append("\n".join(lines) + "\n")

    if result["references"]:
        lines = [f"## {HEADING_REFS}\n"]
        for item in result["references"]:
            title = item.get("title", "") or item.get("url", "")
            url = item.get("url", "")
            note = item.get("note", "")
            entry = f"- [{title}]({url})"
            if note:
                entry += f" — {note}"
            lines.append(entry)
        sections.append("\n".join(lines) + "\n")

    post = f"""---
title: {yaml_quote(f"{date.date().isoformat()} {result['title']}")}
date: {date.isoformat()}
tags: [{tags_str}]
---
""" + "\n".join(sections)
    path.write_text(post, encoding="utf-8")
    return path


def write_blog_post(result: dict, date: datetime) -> Path:
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    base = f"{date.date().isoformat()}-{slugify(result['title'])}"
    path = BLOG_DIR / f"{base}.md"
    n = 2
    while path.exists():
        path = BLOG_DIR / f"{base}-{n}.md"
        n += 1

    tags_str = ", ".join(yaml_quote(t) for t in result["tags"])

    ref_lines = [f"## {HEADING_BLOG_REFS}\n"]
    for item in result["references"]:
        title = item.get("title", "") or item.get("url", "")
        url = item.get("url", "")
        note = item.get("note", "")
        entry = f"- [{title}]({url})"
        if note:
            entry += f" — {note}"
        ref_lines.append(entry)

    post = f"""---
title: {yaml_quote(f"{date.date().isoformat()} {result['title']}")}
date: {date.isoformat()}
tags: [{tags_str}]
---
{result['body'].strip()}

""" + "\n".join(ref_lines) + "\n"
    path.write_text(post, encoding="utf-8")
    return path


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcript study pipeline")
    parser.add_argument("--dry-run", action="store_true",
                         help="파일 생성/state.json 갱신 없이 결과만 출력")
    args = parser.parse_args()

    backend = os.environ.get("JUDGE_BACKEND", "").strip() or (
        "claude-code" if shutil.which("claude") else "api"
    )
    client = None
    if backend == "api":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            log("오류: api 백엔드에는 ANTHROPIC_API_KEY 환경변수가 필요합니다")
            return 1
        import anthropic  # 지연 임포트

        client = anthropic.Anthropic()
    elif backend == "claude-code":
        if not shutil.which("claude"):
            log("오류: claude-code 백엔드에는 claude CLI가 PATH에 있어야 합니다")
            return 1
    else:
        log(f"오류: 알 수 없는 JUDGE_BACKEND={backend!r} (claude-code | api)")
        return 1

    model = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")
    today = datetime.now(KST).date()
    sentences = read_sentences()
    queue = build_queue(sentences, today)
    if sentences:
        log(f"입력된 스크립트 {len(sentences)}개")
    elif queue:
        log(f"input/script.md 에 스크립트가 없어 기술 토픽으로 대체합니다: {queue[0]['text']}")
    else:
        log("input/script.md 에 스크립트가 없고 FALLBACK_QUOTES도 비어 있어 오늘은 건너뜁니다")
        return 0

    state = load_state()
    processed: dict = state.get("processed", {})

    log(f"=== 생성 시작 (backend={backend}, model={model}, dry_run={args.dry_run}) ===")

    new_count = 0
    skipped_dup = 0
    failed = 0
    fatal_error = None
    for item in queue:
        sentence, source, h = item["text"], item["source"], item["dedup_key"]
        blog_key = f"blog::{h}"
        # 밋업 정리 포스트와 리서치 블로그는 독립 dedup — 한쪽만 실패해도
        # 다음 실행에서 실패한 쪽만 재시도된다. 블로그는 실제 스크립트에만 생성
        # (폴백 기술 브리프에는 리서치 글을 만들지 않음).
        need_post = h not in processed
        need_blog = source is None and blog_key not in processed
        if not need_post and not need_blog:
            skipped_dup += 1
            continue

        preview = sentence if len(sentence) <= 80 else sentence[:80] + "…"
        log(f"\n오늘의 항목 ({len(sentence)}자): {preview}")

        if need_post:
            try:
                if backend == "claude-code":
                    result = generate_cli(model, sentence, source)
                else:
                    result = generate_api(client, model, sentence, source)
            except FatalAPIError as exc:
                fatal_error = exc
                break

            if result is None:
                log("  생성 실패 — 건너뜁니다 (다음 실행에서 재시도)")
                failed += 1
            else:
                now = datetime.now(KST)
                log(f"  → {result['title']}")
                if args.dry_run:
                    log(json.dumps(result, ensure_ascii=False, indent=2))
                else:
                    path = write_post(sentence, result, now, source)
                    log(f"  생성 파일: {path.relative_to(ROOT)}")
                    processed[h] = now.date().isoformat()
                    new_count += 1

        if need_blog:
            log("  리서치 블로그 생성 중 (웹 검색 포함)…")
            try:
                if backend == "claude-code":
                    blog = generate_blog_cli(model, sentence)
                else:
                    blog = generate_blog_api(client, model, sentence)
            except FatalAPIError as exc:
                fatal_error = exc
                break

            if blog is None:
                log("  블로그 생성 실패 — 건너뜁니다 (다음 실행에서 재시도)")
                failed += 1
            else:
                now = datetime.now(KST)
                log(f"  → [blog] {blog['title']}")
                if args.dry_run:
                    log(json.dumps(blog, ensure_ascii=False, indent=2))
                else:
                    path = write_blog_post(blog, now)
                    log(f"  생성 파일: {path.relative_to(ROOT)}")
                    processed[blog_key] = now.date().isoformat()
                    new_count += 1

    log(f"\n=== 결과: 신규 {new_count} / 중복 스킵 {skipped_dup} / 생성 실패 {failed} ===")

    if args.dry_run:
        log("(dry-run — 파일 생성/기록 갱신 없음)")
        return 1 if fatal_error else 0

    if new_count:
        state["processed"] = processed
        STATE_FILE.write_text(json.dumps(state, indent=1, sort_keys=True), encoding="utf-8")

    # 게시 완료된 스크립트는 입력 템플릿에서 비운다 — 실패분이 있으면 유지(재시도용)
    if sentences and not failed and not fatal_error:
        SENTENCE_FILE.write_text(RESET_TEMPLATE, encoding="utf-8")
        log("input/script.md 를 초기 템플릿(한 줄 안내 + 빈 코드블록)으로 비웠습니다")

    if fatal_error:
        log(f"\n중단: 복구 불가능한 API 오류 — {fatal_error}")
        log("→ Anthropic 크레딧/API 키(또는 CLAUDE_CODE_OAUTH_TOKEN)를 확인하세요.")
        log("→ 성공한 항목은 이미 게시/기록되었습니다.")
        return 1
    return 1 if failed and not new_count else 0


if __name__ == "__main__":
    sys.exit(main())
