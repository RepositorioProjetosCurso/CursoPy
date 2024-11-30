gameName = input("Digite o nome do jogo: ")
qntdRating = 0
totalRating = 0
rating = 0
average = 0

while (rating != -1):
    rating = float(input("Informe a nota do jogo: "))
    if (rating != -1):
        totalRating += rating
        qntdRating += 1
        average = totalRating / qntdRating
print(f"A média das avalições do jogo {gameName} é {average:.2f}")