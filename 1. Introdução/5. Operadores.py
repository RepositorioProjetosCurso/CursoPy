num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print()

# Aritimeticos
soma = num1 + num2
subtra = num1 - num2
multipli = num1 * num2
divisao = num1 / num2
modulo = num1 % num2
exponen = num1 ** num2

print(f"O total da soma: {soma}")
print(f"O total da subtração: {subtra}")
print(f"O total da multiplicação: {multipli}")
print(f"O total da divisão: {divisao}")
print(f"O total do resto: {modulo}")
print(f"O total da exponenciação: {exponen}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}? {biggerEqual}")

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1