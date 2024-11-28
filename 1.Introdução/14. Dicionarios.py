gameFifa = {
    "name": "Fifa",
    "yearLaunch": 2024,
    "gamePrice": 190.80,
    "classification": 8.5,
    "genre": ["Sports", "Family"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))
print()

# Busca um elemento do dicionario
print(gameFifa["genre"])
print(gameFifa["classification"])

# Buscar apenas as chaves do dicionario
print(gameFifa.keys())

# Buscar apenas os valores do dicionario
print(gameFifa.values())

# Buscar com chave e valor
print(gameFifa.items())

# Adicionar itens no dict
gameFifa['players'] = 2
print(gameFifa)

# Atualizar itens de um dicionario
gameFifa.update({"players" : 1})
print(gameFifa)

# Remove itens de um dict
gameFifa.pop("players")
print(gameFifa)