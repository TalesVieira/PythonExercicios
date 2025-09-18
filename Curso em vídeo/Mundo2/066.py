#Crie um programa que leia vários números inteiros pelo teclado , o programa só vai parar quando o usuário digitar 999
#que é nossa condição de parada, no final, mostre quantos números foram digitados e qual a soma entre eles

valorDeEntrada = 0
total = 0
soma = 0
while valorDeEntrada != 999:
    total += 1
    valorDeEntrada = int(input("Digite um valor para a soma (999 STOP): "))
    soma += valorDeEntrada


total -= 1
soma -= 999

print(f"Você digitou {total} números")
print(f"E a soma deles é {soma}")