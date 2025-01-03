class Movie:
    
    avaliacoes = []
    
    def __init__(self, nome):
        self.nome = nome
    
    def avaliacao(self):
        nota = float(input("Digite a nota do filme(1 a 10): "))
        
        if 1 <= nota <= 10:
            Movie.avaliacoes.append(nota)
            print(f"A nota {nota} foi adicionada")
        else:
            print("Nota inválida. Insira um valor entre 0 e 10")
    
    def calculaMedia(self):
        if Movie.avaliacoes:
            return sum(Movie.avaliacoes) / len(Movie.avaliacoes)
        return 0.0

filme = Movie("Avatar - O caminho das águas")

while True:
    print("\nMenu:")
    print("1. Adicionar avaliação")
    print("2. Ver média das avaliações")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        filme.avaliacao()
    elif opcao == "2":
        media = filme.calculaMedia()
        print(f"Média das avaliações: {media:.2f}")
    elif opcao == "3":
        print("Encerrando o programa. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")