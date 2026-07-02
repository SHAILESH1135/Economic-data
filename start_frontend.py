import subprocess
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
cwd = r"C:\SHAILESH\My work space\India economic data analysis\frontend"
npm_path = r"C:\Program Files\nodejs\npm.cmd"
print(f"Starting npm run dev in cwd: {cwd} using {npm_path}")

process = subprocess.Popen(
    [npm_path, "run", "dev"],
    cwd=cwd,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8",
    bufsize=1
)

try:
    for line in process.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
except KeyboardInterrupt:
    print("Stopping frontend server...")
    process.terminate()
