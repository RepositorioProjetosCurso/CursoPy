name = input("Digite o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento: "))
classification = float(input("Digite a nota de classificação do jogo: "))

if classification >= 8.0 or yearLaunch > 2015:
    print(f"O jogo {name} é bom. Recomendo jogá-lo")
else:
    print(f"O jogo {name} ainda não atingiu uma boa nota. Por isso não recomendo")