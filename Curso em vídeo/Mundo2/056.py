#Desemvolva um programa que leia nome idade e sexo de 4 pessoas, no final do programa mostre
#A média de idade do grupo
# qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaIDade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
totalMulheresMenosDe20Anos = 0
for p in range(0, 4):
    nome = str(input(f"Nome da pessoa de número {p+1}: ")).strip()
    idade = int(input(f"Idade da pessoa de número {p+1}: "))
    sexo = str(input(f"Sexo da pessoa de número {p+1} [M/F]: ")).strip().upper()

    if p == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo == "M" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo == "F" and idade < 20:
        totalMulheresMenosDe20Anos +=1
mediaIdade = somaIDade /4

print(f"A média de idade das pessoas é de {mediaIdade} anos")
print(f"O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeHomemMaisVelho}")
print(f"Ao todo são {totalMulheresMenosDe20Anos} mulheres com menos de 20 anos")
