class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:.2f}"
    
    def desconto(self):
        percentualDesconto = float(input("Digite o desconto do produto: "))
        
        if percentualDesconto < 0 or percentualDesconto > 100:
            print("Porcentagem inválida. Insira um valor entre 0 e 100.")
            return
        
        self.preco -= (percentualDesconto / 100) * self.preco
        print(f"Desconto aplicado! O novo preço é R${self.preco:.2f}")
        
produto = Produto("Notebook Acer Nitro", 5450)
        
while True:
    print("\nMenu:")
    print("1. Verificar preço do produto")
    print("2. Dar desconto no produto")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Informações do produto: {produto}")
    elif opcao == "2":
        produto.desconto()
    elif opcao == "3":
        print("Encerrando o programa. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")