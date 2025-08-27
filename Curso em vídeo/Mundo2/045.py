#Crie um programa que faça o computador jogar pedra papel ou tesoura

import random

jogador = input("Escolha: pedra, papel ou tesoura: ").lower()
computador = random.choice(["pedra", "papel", "tesoura"])

print("Computador escolheu:", computador)

if jogador == computador:
    print("Empate!")
elif jogador == "pedra":
    if computador == "tesoura":
        print("Você venceu!")
    else:
        print("Computador venceu!")
elif jogador == "papel":
    if computador == "pedra":
        print("Você venceu!")
    else:
        print("Computador venceu!")
elif jogador == "tesoura":
    if computador == "papel":
        print("Você venceu!")
    else:
        print("Computador venceu!")
else:
    print("Jogada inválida!")
