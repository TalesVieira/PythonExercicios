#Desenvolva um programa que leia o comprimenro de 3 retas e diga ao usuário se elas podem ou não forma um triângulo

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos PODEM FORMAR UMA RETA")
else:
    print("Os seguimentos inseridos não podem formar uma reta")