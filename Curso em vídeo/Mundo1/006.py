#Crie um algoritmo que leia um número e mostre seu dobro, triplo e sua raiz quadrada

numero = int(input('Digite um número inteiro: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)

print(f"O número digitado foi {numero}, seu dobro é {dobro}, seu triplo é {triplo}, e sua raiz quadrada é {raizQuadrada:.2f}") 
#:.2f para formatar o valor com 2 casas decimais