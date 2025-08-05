#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento de 15%

salario = float(input("Qual é o salário do funcionário?: R$"))

novoSalario = salario + (salario * 15/100)

print(f'O funcionário que recebia R${salario}, com o reajuste de 15% vai receber R${novoSalario}')