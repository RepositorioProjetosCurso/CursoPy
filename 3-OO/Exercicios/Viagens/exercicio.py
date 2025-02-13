from locais import Trip

traveler = input("Qual o seu nome? ")

trip01 = Trip("Parajuru")
trip02 = Trip("São José Dos Campos")
trip03 = Trip("São Paulo")
trip04 = Trip("Rio de Janeiro")
trip05 = Trip("Espirito Santo")

trip_list = [trip01, trip02, trip03, trip04, trip05]

print("""

    Escolha para qual destino deseja ir:
      [0] - Parajuru
      [1] - São José Dos Campos
      [2] - São Paulo
      [3] - Rio de Janeiro
      [4] - Espirito Santo

""")

choice = int(input("Digite o número do destido desejado: "))

for option in trip_list:
    if choice >= 5:
        print("Opção inválida, digite outra opção!")
        break
    else:
        print(f"{traveler} sua viagem para {trip_list[choice].destiny} foi confirmada")
        print("Aproveite sua viagem!")
        break