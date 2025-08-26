#Faça um programa que leia 3 números e mostre qual é o maior e qual é menor

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3: 
    menor = n2
else:
    menor = 3

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")