#Mostre a tabuada de um número que o usuário escolher, utilizando o laço for

numero = int(input("Digite um número inteiro para ver sua tabuada: "))

for c in range(1,11):
    print(f"{numero} X {c:2} = {numero*c} ")