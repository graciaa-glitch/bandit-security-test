# vuln_hardcoded_secret.py
# Bandit détecte les secrets/mots de passe en dur (B105)
# => Risque de divulgation d’informations sensibles

PASSWORD = "SuperSecret123!"
print("Connexion avec mot de passe :", PASSWORD)
