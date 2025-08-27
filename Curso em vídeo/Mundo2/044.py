# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando seu preço normal e a condição de pagamento:
# 1 - À vista no dinheiro/cheque: 10% de desconto
# 2 - À vista no cartão: 5% de desconto
# 3 - Em até 2x no cartão: preço normal
# 4 - 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: R$ "))

print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    total = preco - (preco * 0.10)
    print(f"Pagamento à vista no dinheiro/cheque. Total: R$ {total:.2f}")
elif opcao == 2:
    total = preco - (preco * 0.05)
    print(f"Pagamento à vista no cartão. Total: R$ {total:.2f}")
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Pagamento em 2x no cartão. 2 parcelas de R$ {parcela:.2f}. Total: R$ {total:.2f}")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    total = preco + (preco * 0.20)
    parcela = total / parcelas
    print(f"Pagamento em {parcelas}x no cartão. Cada parcela: R$ {parcela:.2f}. Total: R$ {total:.2f}")
else:
    print("Opção inválida, tente novamente!")
