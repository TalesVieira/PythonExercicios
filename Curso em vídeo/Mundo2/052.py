#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
#Números primos são os que são somente divisíveis por 1 e ele mesmo

numero = int(input("Digite um número: "))
total = 0

for c in range(1, numero + 1):
    if numero % c == 0 :
        print('\033[31m', end='')
        total +=1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')

print(f"O número {numero} foi divisível {total}x")

if total ==2:
    print("E por isso ELE É PRIMO!")
else:
    print("e por isso ele NÃO É PRIMO")