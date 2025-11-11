# vuln_subprocess_shell.py
# Bandit signale subprocess.run(..., shell=True) comme HIGH
import subprocess

cmd = "ls -la"
# usage de shell=True -> risque d'injection
subprocess.run(cmd, shell=True)
