class Movie:
    def __init__(self, nome, anoLancamento, inclusoNoPlano, nota, duracaoEmMinutos):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.inclusoNoPlano = inclusoNoPlano
        self.nota = nota
        self.duracaoEmMinutos = duracaoEmMinutos
    
    def __str__(self):
        return f"Filme: {self.nome}"
    
    def ficha_tecnica(self):
        print("--- Dados do Filme ---")
        print(f"Nome do Filme: {self.nome}")
        print(f"Ano de Lançamento: {self.anoLancamento}")
        print(f"Está no plano? {self.inclusoNoPlano}")
        print(f"Nota do filme: {self.nota}")
        print(f"Duração do Filme: {self.duracaoEmMinutos}")
        print("----------------------")
        
        
mario = Movie("Super Mario Bros", 2023, False, 8.0, 125)
topGun = Movie("Top Gun Maverick", 2022, True, 7.4, 152)

mario.ficha_tecnica()
print()
topGun.ficha_tecnica()