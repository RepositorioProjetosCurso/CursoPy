def wellcome():
    print('Hello, World!')  
wellcome()

def sum():
    return 5 + 4
    # print(4 + 5)
print(sum())

def cadastro():
    name = input("Digite o nome do jogo: ")
    yearLaunch = int(input("Digite o ano de lançamento: "))
    gamePrice = float(input("Digite o valor do jogo: "))
    noteRating = float(input("Digite a nota de avaliação do jogo: "))
    
    print(f"{name} - R${gamePrice}")
cadastro()