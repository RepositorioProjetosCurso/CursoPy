# Função que recebe dois argumentos (Nome | Sobrenome)
def fullName(name, lName):
    print(f'Nome completo: {name} {lName}')
fullName('Pedro', 'Lucas')

# Função que soma parametros
def sum(a, b):
    return a + b
print(sum(10, 9))

# Argumentos default numa função
def adress(country = "Brasil"):
    print(f"Eu moro no {country}")
adress()
adress('Canadá')

# Avaliação do jogo
def ratingGame(qntdRating):
    gameName = input("Digite o nome do jogo: ")
    sum = 0
    for i in range(qntdRating):
        note = float(input("Digite uma nota para o jogo: "))
        sum += note
    print(f"Média de avalição do jogo {gameName} foi {sum / qntdRating :.2f}")

qntdRating = int(input("Digite quantas avalições deseja fazer no jogo: "))
ratingGame(qntdRating)