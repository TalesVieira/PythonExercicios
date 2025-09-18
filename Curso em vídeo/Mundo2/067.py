#Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário
#o programa deve encerrar se o número for negativo

while True:
    numero = int(input("Digite um valor para ver sua tabuada (ou valor negativo para encerrar!): "))
    
    if numero < 0:
        break
    else:
        for n in range(1, 11):  
            print(f"{numero} X {n} = {numero * n}")

print("Você digitou um número negativo. O programa foi encerrado.")
