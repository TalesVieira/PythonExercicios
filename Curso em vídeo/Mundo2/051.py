#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética, no final, mostre os 10 primeiros termos 
#dessa progressão

primeiroTermo = int(input(("Primeiro termo: ")))
razao = int(input("Razão: "))

decimoTermo = primeiroTermo + (10-1) * razao

for c in range(primeiroTermo, decimoTermo + razao, razao):
    print(f"{c}")

print("FIM")