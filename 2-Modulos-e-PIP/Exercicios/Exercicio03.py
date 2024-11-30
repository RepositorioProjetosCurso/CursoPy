import re

def verificaString(string):
    padrao = re.compile(r'^[A-Za-z0-9]+$')
    corresponde = []
    nao_corresponde = []

    # Iterar por cada caractere no texto
    for f in string:
        if padrao.match(f):
            corresponde.append(f)
        else:
            nao_corresponde.append(f)

    # Exibir os resultados
    print("Corresponde:", corresponde)
    print("Não corresponde:", nao_corresponde)

texto = "aB#c$D%\\e^F&G*h(I)j-K+L=M~n_o`p{q|r}s]t[u;v:z"
verificaString(texto)

print()

texto2 = "xY@z!W#1$2%3^4&A*B(C)D-E+F=G~H_I`J{K|L}M]N[O;P:QR\\<S>T?UV\\V"
verificaString(texto2)