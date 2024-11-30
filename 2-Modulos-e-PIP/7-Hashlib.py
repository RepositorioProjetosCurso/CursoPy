import hashlib

# 1 - Verifica os algoritimos disponiveis
print(hashlib.algorithms_available)
print()

# 2 - Algoritimos disponiveis de acordo com o SO
print(hashlib.algorithms_guaranteed)
print()

# 3 - Utilizando sha256
algo = hashlib.sha256()
print(algo.digest())
print()
mensagem = "A melhor forma de prever o futuro é cria-lo".encode()
algo.update(mensagem)
print(algo.hexdigest())
print()

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())