import os

# 1 - Desligar o computador
# os.system('shutdown /s') # Desliga o computador em 60 segundos
os.system('shutdown /s /t 0') # Desliga o computador imediatamente

# # 2 - Cancela o desligamento
# os.system('shutdown /a')

def desligaEmUmaHora():
    os.system('shutdown /s /t 3600')
    
def desligaEmMeiaHora():
    os.system("shutdown /s /t 1800")
    
def cancelaDesligamento():
    os.system('shutdown /a')
    
# desligaEmUmaHora()
# cancelaDesligamento()

# desligaEmMeiaHora()
# cancelaDesligamento()