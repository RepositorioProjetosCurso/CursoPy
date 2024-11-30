gameName = "Fifa 23"
gameDescription = """
Fifa 2025 é um jogo de futebol,
desenvolvido pela EA Sports em que,
é possivel jogar localmente e on-line.
"""

print(gameName.upper()) # Retorna string em MAIÚSCULO
print(gameName.lower()) # Retona string em minúsculo
print(gameName.capitalize()) # Retorna a primeira letra em maiusculo
print(gameName.title()) # Retorna a primeira letra em maiusculo
print(gameName.center(11, '-')) # Põem a string no meio e preenche as laterais com o caracter desejado no tamanho desejado
print(gameName.find('a')) # Retorna a posição de um determinado caracter
print()
print(gameDescription.count('f')) # Conta caracteres
print(gameDescription.count('a')) # Conta caracteres
print(gameDescription.count('e')) # Conta caracteres
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento especifico por outro
print(gameDescription.split(','))