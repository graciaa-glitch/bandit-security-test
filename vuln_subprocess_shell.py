# vuln_subprocess_shell.py
# Bandit détecte subprocess avec shell=True comme vulnérabilité HIGH (B602, B607)
# => Risque d'injection de commande

import subprocess

cmd = "ls -la"
subprocess.run(cmd, shell=True)
