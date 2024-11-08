gameTuple = ("Fifa 25", "Cook in Joy", "Ben 10", "Warzone", "GTA V")
print(type(gameTuple))

'''
    Uma tupla não possibilita remover valores
    não possibilita adicionar valores
    não possibilita ordenar valores
'''

# Buscar os dois primeiros itens da lista
print(gameTuple[0:2])

# Buscar o ultimo item da lista
print(gameTuple[-1])

# Buscar jogos até uma determinada posição
print(gameTuple[:3])

# Buscar jogos de uma posição em diante
print(gameTuple[2:])

# Recuparar item da lista pelo indice
print(gameTuple.index("Fifa 25"))