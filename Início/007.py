#Desenvolva um programa que leia as 2 notas de um aluno, calcule e mostre sua média

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) /2

print(f"A média do aluno é: {media:.2f}")
