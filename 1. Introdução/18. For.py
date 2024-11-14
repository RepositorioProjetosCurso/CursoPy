gameList = ["God Of War", "Resident Evil 4 - Remake", "Red Dead Redemption 2", "Star Wars", "Cook in Joy"]

# 1 - Iterando valores de uma lista
for game in gameList:
    print(game)
print()
    
# 2 - Quando a condição for atendida, o loop se encerrará
for game in gameList:
    if game == "Red Dead Redemption 2":
        break
    print(game)
    
# 3 - Quando a condição for atendida o loop vai para a proxima iteração
for game in gameList:
    if game == "Red Dead Redemption 2":
        continue
    print(game)
    
# 4 - Avaliação do jogo
gameName = input('Digite o nome do jogo: ')
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota: "))
    sum += note
print(f"A média de avaliação do jogo {gameName} é {sum/gameRating:.2f}")