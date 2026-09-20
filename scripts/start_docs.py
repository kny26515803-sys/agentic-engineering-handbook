import os
import sys
import socket
import subprocess

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    build_script = os.path.join(base_dir, 'scripts', 'build_docs.py')
    
    print("1. Syncing documentation files to docs/...")
    subprocess.run([sys.executable, build_script], check=True)
    
    mkdocs_bin = os.path.join(base_dir, '.venv', 'Scripts', 'mkdocs.exe')
    if not os.path.exists(mkdocs_bin):
        mkdocs_bin = 'mkdocs'
        
    local_ip = get_local_ip()
    print("\n2. Starting local documentation server...")
    print(f"   💻 컴퓨터에서 접속: http://127.0.0.1:8000")
    print(f"   📱 스마트폰에서 접속: http://{local_ip}:8000  (같은 Wi-Fi 연결 필요)\n")
    
    subprocess.run([mkdocs_bin, 'serve', '-a', '0.0.0.0:8000'], cwd=base_dir)

if __name__ == '__main__':
    main()
