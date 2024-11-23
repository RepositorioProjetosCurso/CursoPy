import math

# 1 - Acessar número PI
print(math.pi)
print(f'{math.pi:.5f}')

# 2 - Acessar o número de Euler
print(math.e)
print(f'{math.e:.3f}')

# 3 - Arredonda numero
num1 = 3.895
print(math.ceil(num1)) # Arredondando para cima
print(math.floor(num1)) # Arredondando para baixo

# 4 - Calculando fatorial de numero
num2 = 7
print(math.factorial(num2))

# 5 - Potência de números
num3 = 10
print(math.pow(num3, 2))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC
mdc = math.gcd(25, 100) # 25 / 100
print(mdc)

# 8 - Logaritimo
print(math.log(10))