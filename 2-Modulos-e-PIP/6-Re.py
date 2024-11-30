import re

# 1 - Índice inicial e final de palavras
# o r significa que estamos trabalhando com uma string bruta ou (raw string)
text = "OneBitCode - Transformando pessoas em programadores sem limites"
match = re.search(r'pessoas em programadores', text)

print('Indice inicial - ', match.start())
print('Indice final - ', match.end())
print()

# 2 - Buscando o indice que possui o ponto
site = 'https://onebitcode.com'
match = re.search(r'\.', site)
print(match)
print()

# 3 - Buscando uma lista de caracteres dentro de uma frase
padrao = "[a-m]"
resultado = re.findall(padrao, text)
print(text)
print(resultado)
print()

# 4 - Verificando o inicio de um string
regra = r'^A'
frases = ['A casa está suja', 'Vamos nos divertir hoje', 'Olá, como você está?']
for f in frases:
    if re.match(regra, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")
print()
        
# 5 - Verificando o fim de uma string
regra2 = r'!$'
frases2 = 'Hoje está um lindo dia!'
match = re.search(regra2, frases2)
if match:
    print("Corresponde")
else:
    print("Não corresponde")