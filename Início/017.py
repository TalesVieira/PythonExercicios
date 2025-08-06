#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa
from math import hypot

catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

#Agora putra forma de fazer utilizando módulo

hi = hypot(catetoOposto, catetoAdjacente)

print(hi)
