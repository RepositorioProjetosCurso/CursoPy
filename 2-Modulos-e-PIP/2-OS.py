import os

# 1 - Consultar as funcionalidades do modulo
help('os')

# 2 - Retornar a pasta atual
print(os.getcwd())

# 3 - Listar arquivos e pastas
print(os.listdir())

# 4 - Apresentar versão do SO
os.system('ver')

# 5 - Configurações da maquina
os.system("systeminfo")

# 6 - Limpar a tela
os.system('cls')