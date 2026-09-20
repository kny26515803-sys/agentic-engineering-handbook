# v0: Bash 하나면 충분하다 (Bash is All You Need)

**궁극의 단순화: 단 50줄의 코드, 1개의 도구로 완성하는 완전한 에이전트.**

v1, v2, v3 에이전트를 만들기 전에 본 튜토리얼에서는 에이전트의 *본질*이 무엇인지 질문을 던집니다.

v0는 불필요한 레이어를 제거하고 오직 핵심만 남김으로써 이에 대한 답을 제시합니다.

## 핵심 통찰 (The Core Insight)

유닉스(Unix) 철학: 모든 것은 파일이며, 모든 것은 파이프(pipe)로 연결될 수 있다. Bash는 이 세계로 통하는 관문입니다:

| 요구사항 | Bash 명령 대응 |
|:---|:---|
| **파일 읽기** | `cat`, `head`, `grep` |
| **파일 쓰기** | `echo '...' > file` |
| **코드/파일 탐색** | `find`, `grep`, `rg` |
| **실행 및 테스트** | `python`, `npm`, `make` |
| **서브에이전트 위임** | `python v0_bash_agent.py "작업 설명"` |

마지막 줄이 가장 중요한 통찰입니다: **Bash를 통해 자기 자신을 다시 호출하면 서브에이전트(Subagent)가 구현됩니다.** 별도의 Task 도구나 에이전트 레지스트리 없이 재귀 호출만으로 완벽한 서브에이전트가 완성됩니다.

---

## 완전한 코드 (The Complete Code)

```python
#!/usr/bin/env python
from anthropic import Anthropic
import subprocess, sys, os

client = Anthropic(api_key="your-key", base_url="...")
TOOL = [{
    "name": "bash",
    "description": """Execute shell command. Patterns:
- Read: cat/grep/find/ls
- Write: echo '...' > file
- Subagent: python v0_bash_agent.py 'task description'""",
    "input_schema": {"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"]}
}]
SYSTEM = f"CLI agent at {os.getcwd()}. Use bash. Spawn subagent for complex tasks."

def chat(prompt, history=[]):
    history.append({"role": "user", "content": prompt})
    while True:
        r = client.messages.create(model="...", system=SYSTEM, messages=history, tools=TOOL, max_tokens=8000)
        history.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return "".join(b.text for b in r.content if hasattr(b, "text"))
        results = []
        for b in r.content:
            if b.type == "tool_use":
                out = subprocess.run(b.input["command"], shell=True, capture_output=True, text=True, timeout=300)
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": out.stdout + out.stderr})
        history.append({"role": "user", "content": results})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(chat(sys.argv[1]))  # 서브에이전트 모드
    else:
        h = []
        while (q := input(">> ")) not in ("q", ""):
            print(chat(q, h))
```

---

## 요약

1. **단 하나의 도구(Bash)**로 모든 입출력 및 외부 명령을 통합 처리합니다.
2. **자기 자신 재귀 호출**로 서브에이전트의 컨텍스트 분리를 달성합니다.
3. 에이전트 루프의 본질은 결국 **"모델 + 도구 + 무한 루프"**의 결합입니다.

[← 메인 로드맵으로 돌아가기](../../index.md)
