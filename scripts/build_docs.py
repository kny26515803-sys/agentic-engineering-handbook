import os
import shutil

def sync_docs():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(base_dir, 'docs')
    
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir, exist_ok=True)
    
    # 1. Copy README.md as docs/index.md
    readme_src = os.path.join(base_dir, 'README.md')
    index_dst = os.path.join(docs_dir, 'index.md')
    if os.path.exists(readme_src):
        with open(readme_src, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('(LICENSE)', '(https://github.com/keyuchen21/agentic-engineering-handbook/blob/main/LICENSE)')
        with open(index_dst, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Copied README.md -> docs/index.md")

    # 2. Copy root documentation files
    for root_doc in ['ARCHITECTURE.md', 'CAREER_PLAN.md', 'KNOWLEDGE_SYSTEM.md']:
        src = os.path.join(base_dir, root_doc)
        dst = os.path.join(docs_dir, root_doc)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {root_doc} -> docs/{root_doc}")
        
    # 3. Copy tutorials directory
    tutorials_src = os.path.join(base_dir, 'tutorials')
    tutorials_dst = os.path.join(docs_dir, 'tutorials')
    if os.path.exists(tutorials_src):
        shutil.copytree(tutorials_src, tutorials_dst)
        print("Copied tutorials/ -> docs/tutorials/")
        
        agent_loop_dir = os.path.join(tutorials_dst, 'agent-loop')
        if os.path.exists(agent_loop_dir):
            for filename in os.listdir(agent_loop_dir):
                if filename.endswith('.md'):
                    file_path = os.path.join(agent_loop_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        md_text = f.read()
                    md_text = md_text.replace('](../README.md)', '](../../index.md)')
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(md_text)

    agent_loop_dir = os.path.join(tutorials_dst, 'agent-loop')
    agent_loop_index = os.path.join(agent_loop_dir, 'index.md')
    if os.path.exists(agent_loop_dir) and not os.path.exists(agent_loop_index):
        with open(agent_loop_index, 'w', encoding='utf-8') as f:
            f.write("# Phase 0 — Agent Loop Tutorials\n\nThis section covers building an agent loop from scratch across v0 to v4.\n")
        print("Created docs/tutorials/agent-loop/index.md")

if __name__ == '__main__':
    sync_docs()
