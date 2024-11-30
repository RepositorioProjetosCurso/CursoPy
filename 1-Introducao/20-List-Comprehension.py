# 1 - Liste valores de 0 a 10 menor que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 2 - Apenas valores determinados
gameList = ["God Of War", "Resident Evil 4 - Remake", "Red Dead Redemption 2", "Star Wars", "Cook in Joy"]
newGameList = [x for x in gameList if 'a' in x]

print(newGameList)

# 3 - Valores indesejados sendo excluidos
gamesFinished = [x for x in gameList if x != 'Resident Evil 4 - Remake']
print(gamesFinished)