import random

# 1 - Seleciona o valor aleatório de uma lista
lista = [10, 6, 8, 7, 41, 52, 12, 14, 3]
print(random.choice(lista))

# 2 - Gera um número aleatório em um intervalo de valores
valorAleatorio = random.randint(3, 13)
print(valorAleatorio)

# 3 - Seleciona caractere aleatório de uma string
nome = "Um curso aleatório"
charAleatorio = random.choice(nome)
print(charAleatorio)

# 4 - Seleciona mais de um valor
print(random.sample(lista, 4))
print(random.sample(lista, 2))
# Utilizando em strings
print(random.sample(nome, 3))