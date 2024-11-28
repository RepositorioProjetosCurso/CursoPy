num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operador = input("Digite o operador desejado(+ - * /): ")

if operador == '+':
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    print('Operação Inválida!')
    resultado = 0
print(f"O resultado é {resultado:.2f}")