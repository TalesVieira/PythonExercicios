# Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos PODEM FORMAR UM TRIÂNGULO", end=" ")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos inseridos NÃO PODEM FORMAR UM TRIÂNGULO.")
