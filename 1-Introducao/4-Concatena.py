name = input("Digite o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento: "))
gamePrice = float(input("Digite o valor do jogo: "))
plainIncluded = input("O jogo está incluso no plano? ")

print()
print("#### Dados do Jogo ####")
print("=======================")

# Alternativa 01
print("Nome do jogo: ", name)
print("Lançamento do jogo: ", yearLaunch)
print("Preço do jogo: ", gamePrice)
print("Plano incluso no jogo: ", plainIncluded)
print()

# Alternativa 02
print("Nome do jogo: ", name, "\n Ano de Lançamento: ", yearLaunch, "\nPreço do jogo: ", gamePrice, "\nPlano incluso no jogo: ", plainIncluded)
print()

# Alternativa 03
print(f"Nome do jogo: {name}\n Ano de Lançamento: {yearLaunch}\n Preço do jogo: {gamePrice}\n Plano incluso no jogo:  {plainIncluded}")