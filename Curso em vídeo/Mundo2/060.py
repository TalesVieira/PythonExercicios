#Faça um programa que leia um número qualquer e mostre seu fatorial

from math import factorial

n = int(input("Digite um valor para ver seu fatorial: "))

f = factorial(n)

print(f"O fatorial de {n} é {f} ")