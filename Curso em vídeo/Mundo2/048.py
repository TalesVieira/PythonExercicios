#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de 3 e que estão no intervalo de 1 até 500

soma = 0

for numeros in range(1, 501):
    if numeros % 2 != 0 and numeros % 3 == 0:
        soma += numeros

print(soma)


#soma = 0

# Começa em 3 (primeiro número ímpar e múltiplo de 3) e vai de 6 em 6
#for numeros in range(3, 501, 6):
 #   soma += numeros

#print(soma)
###