nomeFuncionario = str(input("Informe o nome do funcionario: "))
salarioFuncionario = float(input("Informe o salário do funcionario: "))

if salarioFuncionario > 1250.00:
    aumentoSalarial =  salarioFuncionario + (salarioFuncionario * 0.10)
    print(f"Você recebeu um aumento de R${aumentoSalarial:.2f}")
elif salarioFuncionario <= 1250.00:
    aumentoSalarial =  salarioFuncionario + (salarioFuncionario * 0.15)
    print(f"Você recebeu um aumento de R${aumentoSalarial:.2f}")
else: print("Inválido, informe um valor correto")

print(f"Olá {nomeFuncionario}, seu salário agora é R${aumentoSalarial:.2f}")