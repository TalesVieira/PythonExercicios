#Crie um programa que leia o ano de nascimento de sete pessoas, no final mostre quantas pessoas 
#ainda não atingiram a maioridade e quantas já

from datetime import date

anoAtual = date.today().year

maiorDeIDade = 0
menorDeIdade = 0

for c in range(1, 8):
    anoNascimento = int(input(f"Digite o ano de nascimento da Pessoa n{c}: "))
    idade = anoAtual - anoNascimento

    if idade >= 18:
        maiorDeIDade +=1
    else:
        menorDeIdade +=1


print(f"Pessoas maiores de idade {maiorDeIDade}")
print(f"Pessoas menores de idade {menorDeIdade}")