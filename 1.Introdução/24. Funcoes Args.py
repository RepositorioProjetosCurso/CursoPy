'''
*args - Utilizamos quando não temos certeza de quantos parametros desejamos passar numa função
- Os argumentos são passados como uma tupla

**kwargs - Passamos valores e também chaves para cada argumento
- Os argumentos são passados como um dicionário
'''

# 1 - Soma de numeros
def sum(*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print(f'A soma é: {sumTotal}')

sum(8, 2)
sum(8, 2, 2)
sum(10, 11)
sum(9, 3, 5, 6, 7, 8, 1)

# 2 - Apresentação de cursos
def apresentacao(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print('### Curso ###')
apresentacao(Nome="Python", Categoria="Backend", Nivel="Iniciante")
apresentacao(Nome="React JS", Categoria="Front-End", Nivel="Médio")