class Movie:
    def __init__(self, nome, anoLancamento, inclusoNoPlano, nota, duracaoEmMinutos):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.inclusoNoPlano = inclusoNoPlano
        self.nota = nota
        self.duracaoEmMinutos = duracaoEmMinutos
    
    def __str__(self):
        return f"Filme: {self.nome}"

movie = Movie("Gato de Botas 02", 2023, False, 8.6, 146)
movie2 = Movie("Avatar", 2022, True, 9.9, 180)

print(movie.nome)
print(movie2.nome)

print(movie)