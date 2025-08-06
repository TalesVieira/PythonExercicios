#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))

#usamos o radians pois o python espera que esteja em radianos, não em graus
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo de {angulo:.2f}, tem o seno de {seno:.2f}, cosseno de {cosseno:.2f}, e a tangente de {tangente:.2f}!")