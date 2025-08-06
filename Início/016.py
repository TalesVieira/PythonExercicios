#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção interia
#Ex = 6,127, o número 6.127 tem a parte inteira 6
import math #importanto biblioteca com operçaões matemáticas

numero = float(input('Digite um número para ver a sua parte inteira: '))

print(f'O número digitado foi {numero}, e sua parte inteira é {numero:.0f}') #forma de fazer sem usar biblioteca

print(f'O número digitado foi {numero}, e sua parte interia é {math.trunc(numero)}') #utilizando módulo