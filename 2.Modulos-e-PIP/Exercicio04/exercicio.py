### Minha Versão ###
import random

limiteInferior = 1
limiteSuperior = 50 
numeroSorteado = random.randint(limiteInferior, limiteSuperior)

print(f"Tente adivinhar o número sorteado entre {limiteInferior} e {limiteSuperior}.")

while True:
    resposta = int(input("Digite o seu número escolhido: "))
    
    if resposta == numeroSorteado:
        print(f"Você acertou, o número sorteado foi {numeroSorteado}")
        break
    else:
        print(f"Seu número {resposta} está errado")



### Versão Curso ###
import random 

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Adivinhar um número")
    print("2. Sair")
    
    choice = input('>')
    
    if choice == "1":
        print("=== Advinhe um número de 1 a 20 ===")
        numero = int(input("Digite um número de 1 a 20: "))
        resultado = random.randint(1, 20)
        if numero == resultado:
            print("Parabéns, você acertou!")
        else:
            print(f"Tente novamente, o número sorteado foi {resultado}")
    elif choice == "2":
        print("Obrigado por jogar!")
        done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 2.")