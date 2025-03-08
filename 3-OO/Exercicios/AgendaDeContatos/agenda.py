from contato import Contato

class Agenda:
    def __init__(self):
        self.lista_de_contatos = []

    def adiciona_contato(self, contato):
        self.lista_de_contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def remove_contato(self, contato):
        if contato in self.lista_de_contatos:
            self.lista_de_contatos.remove(contato)
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado para remoção!")

    def busca_contato(self, name_search):
        for pessoa in self.lista_de_contatos:
            if pessoa.name == name_search:
                print(f"Contato encontrado: {pessoa}")
                return pessoa  # Retorna o contato encontrado
        print("Contato não encontrado!")

    def lista_contatos(self):
        if self.lista_de_contatos:
            for pessoa in self.lista_de_contatos:
                print(pessoa)
        else:
            print("Não há contatos na agenda.")
        print("Todos os contatos foram listados!")
