#Faça um programa que leia o peso de 5 pessoas, no final mostre qual foi a maior e qual foi o menor peso lidos

maior = 0
menor = 0

for c in range(0,5):
    peso = float(input(f"Digite o peso da Pessoa {c+1}: "))

    if c ==1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


print(f"O maior peso foi {maior}")
print(f"O menor peso foi {menor}")