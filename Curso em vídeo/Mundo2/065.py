# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre eles,
# e qual foi o maior e o menor valores digitados.
# O programa deve perguntar se o usuário quer ou não continuar.

resposta = "S"
somaTotal = 0
quantidadeValores = 0
maior = menor = 0  # serão definidos no primeiro número digitado

while resposta == "S":
    n = int(input("Digite um valor: "))
    somaTotal += n
    quantidadeValores += 1

    if quantidadeValores == 1:
        maior = menor = n  # primeiro número define maior e menor
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resposta = input("Quer continuar? [S/N] ").strip().upper()[0]

media = somaTotal / quantidadeValores
print(f"Você digitou {quantidadeValores} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
