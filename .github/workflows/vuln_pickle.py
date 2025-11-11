# vuln_pickle.py
# Bandit détecte pickle.loads() sur des données non fiables comme vulnérabilité HIGH (B301)
# => Risque d'exécution de code arbitraire

import pickle

# Simulation : données venant d'une source non sûre
data = b"cos\nsystem\n(S'echo hello world'\ntR."
obj = pickle.loads(data)
