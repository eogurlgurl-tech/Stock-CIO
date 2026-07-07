import subprocess
import sys
from pathlib import Path
root = Path(r'd:\3. 업무 (GitHub)\Stock-CIO')
cmd = [r'C:\Users\DHLIM\AppData\Local\Python\pythoncore-3.14-64\python.exe', '-m', 'pytest', '-q', 'tests/test_config_manager_packaged.py']
result = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
raise SystemExit(result.returncode)
