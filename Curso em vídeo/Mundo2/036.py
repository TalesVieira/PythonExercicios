#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar, a prestação não pode exceder 30% do salário ou então o empréstimo será negado

valorDaCasa = float(input("Qual o valor da casa?: R$"))
salario = float(input("Qual o salário do comprador?: R$"))
anos = int(input("Em quantos anos o comprador quer quitar a casa?: "))

prestacao = valorDaCasa / (anos * 12)

minimo = salario * 30 / 100

print(f"Para pagar uma casa de {valorDaCasa} em {anos}, a prestação será de {prestacao:.2f}")

if prestacao <= minimo:
    print("Empréstimo concedido!")
else:
    print("Infelizmente o empréstimo foi negado")