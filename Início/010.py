#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#cotação do dia 05/08/2025 U$1 = R$5.50

dinheiroNaCarteira = float(input('Quantos reais você tem na carteira? R$: '))

quantoPodeComprar =  dinheiroNaCarteira / 5.50

print(f'Com R${dinheiroNaCarteira} na carteira, você pode comprar U${quantoPodeComprar:.2f}')