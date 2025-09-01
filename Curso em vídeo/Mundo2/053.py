#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços

frase = str(input("Digite uma frase para verificar se ela é um palíndromo: ")).strip().upper()
palavras = frase.split() #sapara as palavras da frase
junto = ''.join(palavras)
inverso = junto[::-1]

print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo")