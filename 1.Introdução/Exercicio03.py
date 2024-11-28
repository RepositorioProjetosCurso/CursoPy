nome = "Fifa 23"

char = nome[0].lower()
novoNome = nome.replace(char, "$")
novoNome = char + novoNome[1:]
print(novoNome)