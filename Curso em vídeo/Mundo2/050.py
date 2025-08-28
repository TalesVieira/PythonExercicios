#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares

print("ATENÇÃO, Agora você vai precisar digitar 6 números inteiros!")

numerosDigitados = []
soma = 0
for n in range(1,7):
    numero = int(input(f"Digite o número da posição {n}: "))
    numerosDigitados.append(numero)
    if numero % 2 ==0:
        soma += numero


print(f"Os núemros digitados foram {numerosDigitados}")
print(f"E a soma de todos os pares é {soma}")