#Refaça o desafio 51 lendo o primeiro termo e a razão de uma Progressão aritmética e mostrando os 10 primeiros 
#termos utilizando a estrutura while

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 1
termo = primeiroTermo

while contador <= 10:
    print(f"{termo}", end=' ')
    termo += razao
    contador += 1

print("FIM")