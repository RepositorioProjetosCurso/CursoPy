times = {}

def adicionaTime():
    cadastroTime = input("Digite o nome do time: ")
    if cadastroTime not in times:
        times[cadastroTime] = []  # Cria uma lista vazia para jogadores desse time
        print(f"O time {cadastroTime} foi adicionado!")
    else:
        print(f"O time {cadastroTime} já está cadastrado.")


def excluiTime():
    indiceTime = int(input("Digite o indice do time que deseja excluir: "))
    if indiceTime in times:
        times.pop(indiceTime)
        print(f"O time de indice {indiceTime} foi removido!")
    else:
        print(f"O time de indice {indiceTime} não tem cadastro para exclusão")


def adicionaJogador():
    cadastroTime = input("Digite o nome do time para adicionar um jogador: ")
    if cadastroTime in times:
        jogador = input("Digite o nome do jogador: ")
        times[cadastroTime].append(jogador)  # Adiciona o jogador na lista do time
        print(f"O jogador {jogador} foi adicionado ao time {cadastroTime}.")
    else:
        print(f"O time {cadastroTime} não está cadastrado. Adicione o time primeiro.")


def removeJogador():
    cadastroTime = input("Digite o nome do time que o jogador foi cadastrado: ")
    if cadastroTime in times:
        jogador = input("Digite o nome do jogador: ")
        if jogador in times[cadastroTime]:
            times[cadastroTime].remove(jogador)  # Remover jogador da lista
            print(f"O jogador {jogador} foi removido do time {cadastroTime}.")
        else:
            print(f"O jogador {jogador} não está no time {cadastroTime}.")
    else:
        print(f"O time {cadastroTime} não está cadastrado.")


def listaTimes():
    for indice, time in enumerate(times):
        print(f"{indice}: {time}")
        for jogador in times[time]:
            print(f" - {jogador}")


# Função principal (main)
def main():
    while True:
        print("\n--- Gerenciamento de Times e Jogadores ---")
        print("1 - Adicionar Time")
        print("2 - Excluir Time")
        print("3 - Adicionar Jogador")
        print("4 - Remover Jogador")
        print("5 - Listar Times")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionaTime()
        elif escolha == "2":
            excluiTime()
        elif escolha == "3":
            adicionaJogador()
        elif escolha == "4":
            removeJogador()
        elif escolha == "5":
            listaTimes()
        elif escolha == "6":
            print("Saindo... Até logo!")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal para rodar o sistema
if __name__ == "__main__":
    main()