# 1 - Separa numeros impares e pares
def verificaNumeros(numeros):
    par = []
    impar = []
    for numero in numeros:
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)
    return par, impar

print(verificaNumeros([10, 20, 31, 5, 11, 28, 29, 64]))