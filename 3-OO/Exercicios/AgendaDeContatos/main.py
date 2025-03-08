from contato import Contato
from agenda import Agenda

def exibe_menu():
    print("\nEscolha uma opção:")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar contatos")
    print("4 - Buscar contato")
    print("5 - Sair")

def main():
    agenda = Agenda()

    while True:
        exibe_menu()
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            contato = Contato(nome, telefone, email)
            agenda.adiciona_contato(contato)

        elif opcao == "2":
            nome = input("Digite o nome do contato para remover: ")
            contato = agenda.busca_contato(nome)
            if contato:
                confirmacao = input("Tem certeza que deseja remover? (s/n): ")
                if confirmacao.lower() == 's':
                    agenda.remove_contato(contato)

        elif opcao == "3":
            agenda.lista_contatos()

        elif opcao == "4":
            nome = input("Digite o nome para buscar: ")
            agenda.busca_contato(nome)

        elif opcao == "5":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
