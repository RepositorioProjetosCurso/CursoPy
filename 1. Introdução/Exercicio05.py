distanciaEmKm = float(input("Qual a distancia que deseja percorrer(Em KM)? "))

if distanciaEmKm <= 200:
    passagemCalculada = distanciaEmKm * 0.50
elif distanciaEmKm > 200:
    passagemCalculada = distanciaEmKm * 0.35
print(f"O valor da passagem é {passagemCalculada:.2f} e você irá percorrer {distanciaEmKm}KM")