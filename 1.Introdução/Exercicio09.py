# 1 - Conta as letras maiúsculas e minúsculas de uma string
def contagem(string):
    letrasMaiusculas = []
    letrasMinusculas = []
    for letra in string:
        if letra.isupper():
            letrasMaiusculas.append(letra)
        elif letra.islower():
            letrasMinusculas.append(letra)
    print(f'Letras Maiúsculas: {letrasMaiusculas}')
    print(f'Letras Minúsculas: {letrasMinusculas}')

contagem("StrinG de TesTes")

# Código Refatorado
def contagem(string):
    letras_maiusculas = [letra for letra in string if letra.isupper()]
    letras_minusculas = [letra for letra in string if letra.islower()]
    
    print(f'Letras Maiúsculas: {", ".join(letras_maiusculas)}')
    print(f'Letras Minúsculas: {", ".join(letras_minusculas)}')

contagem("StrinG de TesTes")
