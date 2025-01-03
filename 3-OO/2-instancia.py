class Movie:
    nome = ""
    anoLancamento = 0
    inclusoNoPlano = False
    nota = 0
    minutosDuracao = 0

# Primeiro Filme #
movieAladdin = Movie()
movieAladdin.nome = "Aladdin"
movieAladdin.anoLancamento = 1994
movieAladdin.inclusoNoPlano = True
movieAladdin.nota = 8.5
movieAladdin.minutosDuracao = 128

print("### Dados do Filme ###")
print(f"Nome do Filme: {movieAladdin.nome}\nAno de Lançamento: {movieAladdin.anoLancamento}")