gameList = ["God Of War", "Resident Evil 4 - Remake", "Red Dead Redemption 2", "Star Wars", "Cook in Joy"]

# Tamanho da lista
print(len(gameList))

# Recuparar item da lista pelo indice
print(gameList.index("Star Wars"))

# Adicionar item ao final da lista
gameList.append("Raimbow Six")
print(gameList)

# Ordenar uma lista
gameList.sort()
print(gameList)

# Copiar de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("Resident Evil 4 - Remake")
print(gameReset)

# Remove todos os itens da lista
gameReset.clear()
print(gameReset)