# Exercicio tabuada
number = int(input("Tabuada de: "))
beggin = int(input("Começa em: "))
end = int(input("Termina em: "))

x = beggin

while x <= end:
    print(f'Tabuada de {number} x {x} = {number * x}')
    x += 1