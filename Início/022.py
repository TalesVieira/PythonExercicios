#Crie um programa que leia o nome completo de uma pessoa e mostre, o nome com todas as letras minúsculas e maiúsculas
#quantas letras tem ao todo sem considerar os espaços, e quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip()

nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()

print(f"Seu nome em maiúsculo é {nomeMaiusculo}")
print(f"Seu nome em minúsculo é {nomeMinusculo}")
#Contando quantidade de letras subtrando pelos espaços
print(f"Seu nome tem {len(nome)-nome.count(' ')} letras")

print(f"Seu primeiro nome tem {nome.find(' ')} letras")
