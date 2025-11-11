# vuln_two_high.py
# Contient 2 vulnérabilités que Bandit signale normalement comme HIGH :
#  - subprocess.call(...) avec shell=True
#  - eval(...) sur une entrée utilisateur

import subprocess

def dangerous_subprocess(user_cmd):
    # VULN 1 : utilisation de shell=True (injection possible)
    # Simule une commande construite à partir d'une entrée non fiable
    subprocess.call(user_cmd, shell=True)


def dangerous_eval():
    # VULN 2 : eval() sur une entrée utilisateur (exécution arbitraire)
    # NOTE : on ne l'exécute pas automatiquement pour éviter d'exécuter du code dangereux
    user_expr = input("Entrez une expression Python: ")
    result = eval(user_expr)
    print("Resultat :", result)


if __name__ == "__main__":
    # Appels destinés à faire apparaître les motifs dans l'analyse statique
    # Le premier appel contient le shell=True directement ; le deuxième est présent dans le code
    dangerous_subprocess("ls -la")   # Bandit détecte shell=True ici
    # dangerous_eval()               # laissé désactivé pour ne pas exécuter d'input dangereux
