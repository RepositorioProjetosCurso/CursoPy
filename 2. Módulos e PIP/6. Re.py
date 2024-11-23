import re

# 1 - Índice inicial e final de palavras
# o r significa que estamos trabalhando com uma string bruta ou (raw string)
text = "OneBitCode - Transformando pessoas em programadores sem limites"
match = re.search(r'pessoas em programadores', text)

print('Indice inicial', match.start())
print('Indice final', match.end())