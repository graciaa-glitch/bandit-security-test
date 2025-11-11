# vuln_eval.py
# Bandit détecte l'usage de eval() comme vulnérabilité HIGH (B307)
# => Risque d'exécution de code arbitraire si l'entrée vient d'un utilisateur

user_input = "2 + 2"
# Simulation : entrée non sécurisée
result = eval(user_input)
print("Résultat :", result)
