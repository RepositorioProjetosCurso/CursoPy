# Exercicio contagem regressiva
import winsound

contagemRegressiva = [contagem for contagem in range(10, 0, -1)]
for numero in contagemRegressiva:
   print(f'O foguete será lançado em {numero}')
winsound.Beep(1000, 750)