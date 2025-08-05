#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias pelos quais
#ele foi alugado, calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por km rodado

dias = int(input("Por quantos dias você ficou com o veículo?: "))
kmPercorrido = int(input("Quantos km você percorreu com o veículo?: "))

valorTotal = (60 * dias) + (0.15 * kmPercorrido) 

print(f'O valor total a ser pago é R${valorTotal:.2f}')