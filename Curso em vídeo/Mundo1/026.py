#Faça um programa que leia uma frase completa e mostre
# Quantas vezes aparece a letra A
#Em que posição ela aparece pela primeira e última vez

frase = str(input("Digite uma frase: ")).upper().strip()

print(f"A letra A, aparece {frase.count('A')}x na frase")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}") #Retorna a primeira posição
print(f"A última letra A apareceu na posição {frase.rfind('A')+1}")#Retorna a última posição

#