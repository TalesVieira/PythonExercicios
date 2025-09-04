#Melhore o jogo do desafio 28 onde o computador vai "Pensar" em um número entre 0 e 10, mas agora o jogador deve tentar adivinhar
#até acertar, mostrando no final a quantidade de palpites nescessários para o acerto

from random import randint
print("Sou seu computador e pensei em um número entre 0 e 10, qual você acha que foi?")
numeroEscolhido = randint(0,10)


palpiteUsuario = int(input("Seu palpite: "))
tentativas = 1

while palpiteUsuario != numeroEscolhido:
    print(f"Errou, não pensei no número {palpiteUsuario}, tente novamente")
    palpiteUsuario = int(input("Palpite: "))
    tentativas +=1

    if palpiteUsuario == numeroEscolhido:
        break


print(f"VOCÊ ACETOU COM {tentativas}")
