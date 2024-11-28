gameName = "Fifa 23"
gameDescription = """
Fifa 2025 é um jogo de futebol
desenvolvido pela EA Sports em que
é possive jogar localmente e on-line.
"""

# string[inicio : fim] - Indice começa na posição 0 | Indice final é indice -1

# 1 - Busque toda string apartir da posição
print(gameName[0:])

# 2 - Busque toda string até a ultima posição
print(gameName[:7])

# 3 - Busque toda string da terceira até a ultima posição
print(gameName[2:])

'''
string[inicio : fim] - Indice começa na posição 0 | Indice final é indice -1
Passo - Determina o incremento. Por padrão esse número é o 1.
'''
# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda string nos indices ímpares
print(gameName[1::2])

# 6 - Invertendo uma string
print(gameName[::-1])