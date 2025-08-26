#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$ 1250 aumente 10 %
#Para menores aumente 15%

salarioDoFuncionario = float(input("Qual é o salário do funcionário: R$"))

if salarioDoFuncionario > 1250:
    salarioComAumento = salarioDoFuncionario + (salarioDoFuncionario * 10/100 )
else:
    salarioComAumento = salarioDoFuncionario + (salarioDoFuncionario * 15/100)

print(f"O novo salário do funcionário será de R${salarioComAumento}")

