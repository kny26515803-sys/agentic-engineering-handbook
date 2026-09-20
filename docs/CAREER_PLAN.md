# Agentic Engineer 직무 역량 및 성장 계획서 (Career Plan)

## 1. 직무 정의 (Role Definition)
**Agentic Engineer (에이전트 엔지니어)**는 단순한 단발성 LLM 프롬프트 작성을 넘어, 자율적 문제 해결이 가능한 **자율 AI 에이전트 시스템, MCP(Model Context Protocol) 툴링, 컨텍스트 파이프라인, 에이전트 평가(Evals) 및 프로덕션 하네스(Harness)**를 설계·구축·운영하는 최고 수준의 AI 엔지니어입니다.

---

## 2. 로드맵 단계별 역량 모델 (Competency Framework)

| 단계 | 주요 영역 | 핵심 보유 역량 (Key Skills) | 실행 과제 (Build Exercises) |
|:---|:---|:---|:---|
| **Phase 0** | Agent Loop Base | LLM 기본 루프, Bash 실행기, 도구 호출, 파일 입출력 | `v0`~`v4` 에이전트 루프 바닥부터 구현하기 |
| **Phase 1** | Agent Foundations | 프롬프트 엔지니어링, 시스템 프롬프트 작성, 에이전트 판단 프레임워크 | Anthropic / OpenAI 에이전트 베스트 프랙티스 습득 |
| **Phase 2** | MCP & Tool Ecosystem | Model Context Protocol 서버/클라이언트 개발, 커스텀 툴 샌드박싱 | MCP Server 구축 및 Claude/Antigravity 연동 |
| **Phase 3** | Context, Memory & Skills | 장기/단기 메모리 윈도우 관리, 요약 기법, 스킬 모듈화 | Antigravity/Claude 스킬 세트 구현 및 주입 테스트 |
| **Phase 4** | Agent Harness & Multi-Agent | 에이전트 오케스트레이션, 서브에이전트 분기, 상태 분리 | 멀티에이전트 협업 루프 개발 |
| **Phase 5** | Evals & Benchmarks | SWE-bench, 에이전트 성능 측정, 벤치마크 설계, 회귀 테스트 | Custom Eval Harness 구축 및 에이전트 정량 평가 |
| **Phase 6** | Security & Production | 샌드박싱, 가드레일, 안전성 검증, 불확실성 제어 | 프로덕션 레벨 에이전트 배포 및 가드레일 적용 |

---

## 3. 핵심 마일스톤 및 실행 계획

1. **기반 기술 내재화 (Phase 0~2)**
   - `tutorials/agent-loop/` 코드의 백그라운드 원리 파악 및 커스텀 에이전트 제작
   - MCP Server 생태계 이해 및 사내/개인 도구의 MCP 모듈화
2. **에이전트 오케스트레이션 및 스킬화 (Phase 3~4)**
   - 에이전트가 사용할 도구, 지식(Knowledge Items), 스킬(Skills) 표준 정의 및 모듈화
3. **프로덕션 검증 및 평가 체계 구축 (Phase 5~6)**
   - 자동화된 Evals 구축으로 에이전트의 코드 생성 및 문제 해결 성공률 측정
   - Render / Cloud 인프라 기반 정적/동적 에이전트 서비스 배포 자동화
