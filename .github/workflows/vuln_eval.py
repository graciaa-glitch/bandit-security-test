# vuln_eval.py
# Bandit détecte l'usage d'eval() comme dangereux
user_input = "2 + 2"
# simulate untrusted input -> usage dangereux
result = eval(user_input)
print("Result:", result)
