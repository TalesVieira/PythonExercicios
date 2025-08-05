#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

precoDoProduto = float(input('Qual é o valor do produto?: '))

novoPreco = precoDoProduto - (precoDoProduto * 5/100)

print(f'O novo valor do produto vai ser de R${novoPreco}')