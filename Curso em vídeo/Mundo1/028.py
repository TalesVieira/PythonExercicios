#Escreva um programa que faça o computador "pensar" um número inteiro entre 0 e 5, e peça para o usuário tentar descobrir
#O programa deverá escrever na tela se o usuário venceu ou pedeu

from random import randint
print("-=-" *20)
print("Sou seu computador e pensei em um número entre 0 e 5, qual você acha que foi?")
print("-=-" *20)
palpiteUsuario = int(input("Seu palpite: "))
print("-=-" *20)

numeroEscolhido = randint(0,5)

if palpiteUsuario == numeroEscolhido:
    print(f"PARABÉNS!, Você acertou o número que eu estava pensado, era realmente o {palpiteUsuario}")
else:
    print(f"Infelizmente você não acertou!, o número não era {palpiteUsuario} e sim {numeroEscolhido}!")

