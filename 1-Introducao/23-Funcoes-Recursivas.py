# Fatorial de um número

def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))

factorialNumber = int(input("Digite um número para saber o fatorial: "))
print(f"O fatorial de {factorialNumber} é: {fatorial(factorialNumber)}")

# Soma total de um número
def somaTotal(num):
    if num == 1:
        return 1
    else:
        return (num + somaTotal(num - 1))

sumNumber = int(input("Digite um número para ver a soma total: "))
print(f"A soma total de {sumNumber} é: {somaTotal(sumNumber)}")