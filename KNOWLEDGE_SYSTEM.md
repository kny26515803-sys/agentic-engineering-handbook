# Agentic Engineering Handbook — Knowledge System Document

## 1. 개요 (Overview)
본 지식 문서는 **OpenAI, Anthropic, Google, MCP, Harness, Evals, 프로덕션 에이전트 시스템**에 관한 179개의 엄선된 리소스와 학습 자료를 체계적으로 분류한 지식 맵(Knowledge Map)입니다.

---

## 2. 지식 영역 분류 (Knowledge Domain Taxonomy)

### Domain A. Agent Loops & Reasoning Patterns
- **Model + Tools + Loop**: 기본 루프 구성 요소 및 컨텍스트 제어
- **Planning Mechanisms**: ReAct, Plan-and-Solve, Todo 관리, 구조화된 계획 수립
- **Subagent & Delegation**: 주 컨텍스트 보호 및 서브에이전트 태스크 위임 패턴

### Domain B. Protocols & Tool Interfaces
- **MCP (Model Context Protocol)**: 표준 툴 인터페이스, 서버/클라이언트 아키텍처
- **Function Calling**: LLM 별 (OpenAI, Gemini, Claude) 도구 스키마 정의 및 파싱 베스트 프랙티스

### Domain C. Context, Memory & Skills
- **Context Compaction**: 롱 컨텍스트 윈도우 관리 및 요약 기법
- **Memory Architectures**: Ephemeral vs Persistent 메모리, 에피소딕 메모리
- **Skills System**: 런타임 스킬 주입 및 YAML 기반 스킬 템플릿

### Domain D. Evals & Benchmarks
- **SWE-bench**: 에이전트 코딩 능력 평가 벤치마크
- **Agent Evaluation Frameworks**: 정량적 성공률, 정밀도, 재현율 측정 도구

---

## 3. 웹 및 전자책 출판 연동
본 지식 문서 및 전체 리소스는 [`mkdocs.yml`](file:///c:/Users/USER/MYFOLDER/agentic-engineering-handbook/mkdocs.yml) 설정과 Render 배포 파이프라인을 통해 웹 및 PDF 전자책 형태로 실시간으로 통합 및 동기화됩니다.
