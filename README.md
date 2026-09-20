# Agentic Engineering Handbook (에이전트 엔지니어링 핸드북)

> OpenAI, Anthropic, Google, MCP, Harness, Evals 및 프로덕션 에이전트 시스템 구축을 위한 가이드 및 학습 로드맵

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--07--25-blue.svg)](#)

👉 **[🌐 한글 라이브 웹사이트 바로가기](https://kny26515803-sys.github.io/agentic-engineering-handbook/)** | **[📄 한글 전자책 PDF 다운로드](Agentic_Engineering_Handbook_KR.pdf)**

---


## 💡 핸드북 소개 (Why This Repository?)

AI 산업은 본격적인 **에이전트 시대(Agentic Era)**로 진입했습니다. 프로덕션 수준의 AI 시스템을 구축하려면 에이전트 루프, 도구 활용(Tool Use), MCP(Model Context Protocol), 메모리 관리, 장기 실행 워크플로우, 코딩 에이전트, 에이전트 하네스(Harness), 평가(Evals), 그리고 안전성(Safety)에 대한 깊은 이해가 필수적입니다.

그러나 이러한 핵심 기술 지식은 OpenAI 블로그, Anthropic 엔지니어링 아티클, SDK 공식 문서, 기술 서적 및 논문 등으로 파편화되어 존재합니다.

본 핸드북은 **179개의 엄선된 기술 자료와 아티클**을 하나의 체계적인 학습 로드맵으로 정리한 가이드입니다.

**최종 목표: 세계적인 수준의 에이전트 엔지니어(Agentic Engineer)로 성장하기**

---

## 📖 핸드북 활용 가이드 (How To Use This Handbook)

자신의 학습 목표와 출발점에 맞춰 아래 가이드를 활용하세요:

- **에이전트를 처음 접하는 경우:** [학습 로드맵](#learning-roadmap)의 Phase 0부터 Phase 6까지 순서대로 진행하세요. 각 단단계의 `필독 (Read First)`, `심화 (Then Read)`, 및 `실습 과제 (Build Exercise)`를 체크리스트처럼 활용하세요.
- **이미 LLM 애플리케이션을 개발해 본 경우:** [Phase 2 — MCP & 툴 생태계](#phase-2--mcp--tool-ecosystem) 또는 [Phase 3 — 컨텍스트, 메모리 & 스킬](#phase-3--context-memory--skills)부터 시작하여 에이전트 루프, 도구 호출, Evals 및 프로덕션 설계 공백을 메우세요.
- **실전 프로젝트를 구축하려는 경우:** 각 Phase별 `실습 과제 (Build Exercise)` 프롬프트를 활용한 후, 코딩 에이전트, 보안, 코드 리뷰, SRE 등을 다루는 [실전 응용 트랙](#applied-practice-tracks)으로 확장하세요.
- **참고 자료를 찾는 경우:** [전체 레퍼런스 리스트](#full-reading-table)로 바로 이동하세요. 핵심 개념은 `P0`, 실무 구현 상세는 `P1`, 심화 배경 지식은 `P2`로 구분되어 있습니다.

---

## 🎯 학습 로드맵 (Learning Roadmap)

### Phase 0 — 에이전트 루프 바닥부터 구현하기 (Agent Loop From Scratch)

Claude Code나 자율 AI 코딩 도구를 다루다 보면 파일 읽기, 명령 실행, 코드 수정, 서브에이전트 위임 등이 마치 마법처럼 동작하는 것처럼 느껴집니다.

하지만 엔지니어링 관점에서 에이전트의 핵심 구조는 매우 단순합니다:

$$\text{Model} + \text{Tools} + \text{One Loop}$$

이 핵심 루프를 직접 구현해 보면 에이전트 시스템 전체를 훨씬 명확하게 이해할 수 있습니다:

- 에이전트가 언제 먼저 계획(Plan)을 세우고, 언제 즉시 실행(Act)해야 하는가?
- 명시적인 To-Do 리스트가 장기 작업 실행 시 에이전트의 이탈(Drift)을 방지하는 이유
- 서브에이전트(Subagent)가 주 컨텍스트(Main Context)를 보호하면서 탐색 영역을 넓히는 원리
- 스킬(Skills), MCP, 훅(Hooks)이 동일한 기본 루프 위에서 어떻게 기능을 확장하는가?

본 단계는 [shareAI-lab/mini-claude-code](https://github.com/shareAI-lab/mini-claude-code)의 오픈소스 튜토리얼을 기반으로 한국어 스터디 노트를 추가하여 구성되었습니다.

| 단계 | 한국어 튜토리얼 문서 | 구현 코드 |
|:---|:---|:---|
| **v0** | [Bash 하나면 충분하다 (Bash is All You Need)](tutorials/agent-loop/v0-bash-is-all-you-need.md) | [v0_bash_agent.py](tutorials/agent-loop/v0_bash_agent.py) |
| **v1** | [에이전트로서의 모델 (Model as Agent)](tutorials/agent-loop/v1-model-as-agent.md) | [v1_basic_agent.py](tutorials/agent-loop/v1_basic_agent.py) |
| **v2** | [구조화된 계획 수립 (Structured Planning)](tutorials/agent-loop/v2-structured-planning.md) | [v2_todo_agent.py](tutorials/agent-loop/v2_todo_agent.py) |
| **v3** | [서브에이전트 메커니즘 (Subagent Mechanism)](tutorials/agent-loop/v3-subagent-mechanism.md) | [v3_subagent.py](tutorials/agent-loop/v3_subagent.py) |
| **v4** | [스킬 메커니즘 (Skills Mechanism)](tutorials/agent-loop/v4-skills-mechanism.md) | [v4_skills_agent.py](tutorials/agent-loop/v4_skills_agent.py) |

---

### Phase 1 — 에이전트 기초 (Agent Foundations)

> 워크플로우 vs 에이전트, 툴 루프, 핸드오프, 가드레일에 대한 공통 용어와 멘탈 모델을 정립합니다.

#### 핵심 멘탈 모델

**에이전트를 도입해야 할까?** (Barry Zhang, Anthropic의 4가지 질문 체크리스트)

| 질문 | No 인 경우 → 워크플로우(Workflow) | Yes 인 경우 → 에이전트(Agent) |
|:---|:---|:---|
| **작업이 충분히 복잡한가?** | 결정 트리(Decision Tree)로 완벽히 매핑 가능 | 불확실하고 모호한 문제 공간 |
| **작업의 가치가 충분한가?** | 실행당 < $0.10 비용 | 실행당 > $1 이상 가치 생성 |
| **핵심 능력을 모델이 잘 수행하는가?** | 약한 고리가 전체 체인을 단절시킴 | 모델이 모든 단계를 안정적으로 처리 |
| **오류 비용이 낮고 감지 가능한가?** | 높은 오류 비용 + 감지 어려움 ➔ 사람 개입 필요 | 테스트/CI를 통해 오류 자동 감지 가능 |

**에이전트의 관점에서 생각하라 (Think like the agent):**
대부분의 설계 실패는 사람의 시각에서 시스템을 설계하기 때문에 발생합니다. 에이전트의 컨텍스트 윈도우 내부(시스템 프롬프트 + 도구 설명 + 최근 관찰된 결과) 입장이 되어 보세요. 각 단계에서 에이전트가 올바르게 행동할 수 있는 충분한 정보가 주어져 있는지 점검해야 합니다.

→ 참고 영상: [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk)

#### 필독 아티클 (Read First)

| # | 제목 | 제공 |
|:---|:---|:---|
| 1 | [System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | Anthropic |
| 2 | [Prompt guidance](https://developers.openai.com/api/docs/guides/prompt-guidance) | OpenAI |
| 3 | [Function Calling](https://developers.openai.com/api/docs/guides/function-calling) | OpenAI |
| 4 | [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | Anthropic |
| 5 | [Function calling - Gemini API](https://ai.google.dev/gemini-api/docs/function-calling) | Google |
| 6 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Anthropic |
| 7 | [New tools for building agents](https://openai.com/index/new-tools-for-building-agents/) | OpenAI |
| 8 | [Agents SDK overview](https://developers.openai.com/api/docs/guides/agents) | OpenAI |

---

### Phase 2 — MCP & 툴 생태계 (MCP & Tool Ecosystem)

> MCP 서버/클라이언트 구조, 로컬 vs 원격 연결, 도구 동적 로딩, 승인 절차 및 커넥터 경계를 습득합니다.

#### 필독 아티클 (Read First)

| # | 제목 | 제공 |
|:---|:---|:---|
| 1 | [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) | Anthropic |
| 2 | [MCP and Connectors](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) | OpenAI |
| 3 | [Building MCP servers for ChatGPT Apps and API integrations](https://developers.openai.com/api/docs/mcp) | OpenAI |

---

### Phase 3 — 컨텍스트, 메모리 & 스킬 (Context, Memory & Skills)

> 컨텍스트 윈도우 제어, 단기/장기 메모리 관리, 스킬/플러그인 작성법 및 `AGENTS.md` 활용법을 익힙니다.

#### 필독 아티클 (Read First)

| # | 제목 | 제공 |
|:---|:---|:---|
| 1 | [Agent Skills Specification](https://agentskills.io/specification) | Agent Skills |
| 2 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic |
| 3 | [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) | Anthropic |
| 4 | [Building Reliable Agents with Memory and Compaction](https://developers.openai.com/cookbook/examples/agents_sdk/building_reliable_agents_memory_compaction) | OpenAI |

---

### Phase 4 — 에이전트 하네스 & 장기 실행 에이전트 (Harness & Long-Running Agents)

> 이벤트 스트림, 스레드 관리, 도구 실행 샌드박싱, 상태 복구, 인간 승인 루프를 구현하는 에이전트 하네스 기술을 마스터합니다.

#### 필독 아티클 (Read First)

| # | 제목 | 제공 |
|:---|:---|:---|
| 1 | [Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/) | OpenAI |
| 2 | [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/) | OpenAI |
| 3 | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Anthropic |

---

### Phase 5 — 코딩 & 워크스페이스 에이전트 (Coding & Workspace Agents)

> Codex와 Claude Code 제품/SDK 구조를 비교하고, 대규모 코드베이스에서의 멀티 에이전트 협업 및 IDE 연동 기법을 다룹니다.

#### 필독 아티클 (Read First)

| # | 제목 | 제공 |
|:---|:---|:---|
| 1 | [AGENTS.md](https://agents.md/) | Agentic AI Foundation |
| 2 | [Introducing Codex](https://openai.com/index/introducing-codex/) | OpenAI |
| 3 | [Best practices for Claude Code](https://www.anthropic.com/engineering/claude-code-best-practices) | Anthropic |
| 4 | [How Claude Code works in large codebases](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) | Anthropic |

---

### Phase 6 — 평가, 안전성 & 프로덕션 (Evals, Safety & Production)

> 사전/사후 평가 루프, 트레이싱(Tracing), 프롬프트 인젝션 방어, 권한 제어 및 회귀 테스트 모니터링 체계를 구축합니다.

#### 필독 아티클 (Read First)

| # | 제목 | 제공 |
|:---|:---|:---|
| 1 | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Anthropic |
| 2 | [The six generations of AI agents and how to eval them](https://www.braintrust.dev/blog/six-generations-ai-agents) | Braintrust |
| 3 | [Agent observability powers agent evaluation](https://www.langchain.com/blog/agent-observability-powers-agent-evaluation) | LangChain |

---

## 🛠️ 실전 응용 트랙 (Applied Practice Tracks)

| 트랙 명칭 | 추천 시작 문서 | 중요성 및 핵심 목표 |
|:---|:---|:---|
| **에이전트 코딩 워크플로우** | [Coding Agents 101](https://devin.ai/agents101), [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) | 에이전트 이론을 명확한 프롬프팅, 검증 체계, 병렬 작업 등 일상적인 코딩 습관으로 전환합니다. |
| **명세 기반 시스템 구축** | [The spec is dead, long live the spec!](https://blog.ravi-mehta.com/p/specs-are-the-new-source-code) | 명세서(Spec)와 프롬프트를 에이전트가 즉시 실행 가능한 소스 코드로 다룹니다. |
| **컨텍스트 실패 모드 분석** | [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html), [Context Rot](https://research.trychroma.com/context-rot) | 컨텍스트 오염, 환각, 검색 과부하 및 성능 저하 원인을 정확히 진단합니다. |
| **Evals & 관측 가능성** | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 오프라인/온라인 평가, 데이터셋 정제, 회귀 게이트 구축 피드백 루프를 만듭니다. |
| **딥리서치 에이전트** | [Deep research](https://developers.openai.com/api/docs/guides/deep-research), [Open Deep Research](https://github.com/langchain-ai/open_deep_research) | 장기 실행 탐색 에이전트: 계획, 검색, MCP, 출처 인용 및 보고서 합성 기법을 연습합니다. |
| **에이전트 보안 & 가드레일** | [OWASP Top Ten](https://owasp.org/www-project-top-ten/), [Prompt Injection Analysis](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) | 프롬프트 인젝션, 권한 오용, 샌드박싱 등 에이전트 보안 베스트 프랙티스를 적용합니다. |
