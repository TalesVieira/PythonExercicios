#Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uam mensagem no final
#média abaixo de 5 =  reprovado, entre 5.0 e 6.9 = recuperação, 7 ou superior = aprovado

nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f" Com a média {media} O aluno está REPROVADO!")
elif media == 5 or media < 7:
    print(f"Com a média {media} O aluno está em RECUPERAÇÃO!")
else:
    print(f" Com a média {media} O aluno está APROVADO!")