import subprocess

# Vulnérabilité : utilisation dangereuse de shell=True
subprocess.call('ls -l', shell=True)

# Vulnérabilité : mot de passe en dur
password = "123456"
print("Mot de passe :", password)
