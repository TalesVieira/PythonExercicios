# Crie um programa que leia vários números inteiros pelo teclado.
# O programa deve parar quando o usuário digitar 999 (condição de parada).
# No final, mostre quantos números foram digitados e a soma entre eles.

quantidadeDeNumerosDigitados = 0
soma = 0

numero = int(input("Digite um número para a soma (999 para parar): "))

while numero != 999:
    soma += numero
    quantidadeDeNumerosDigitados += 1
    numero = int(input("Outro valor (999 para parar): "))

print(f"Você digitou {quantidadeDeNumerosDigitados} números")
print(f"A soma de todos os valores digitados foi {soma}")
