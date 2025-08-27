#Escreva um programa que leia dois números inteiros e compare-os mostrando uma mensagem
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os 2 são iguais

numero1 = int(input("Digite um valor inteiro: "))
numero2 = int(input("Digite mais um valor inteiro: "))

if numero1 > numero2:
    print("O primeiro valor digitado foi o maior!")
elif numero2 > numero1:
    print("O segundo valor digitado foi o maior!")
else:
    print("Os valores digitados são iguais!")