#Crie um programa que leia dois valores e mostre na tela um MENU, seu programa deverá realizar a operação solicitada em cada caso
#1 - somar
#2 - multiplicar
#3 - maior
#4 - Digitar novos números
#5 - sair do programa

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

opcao = 0

while opcao != 5:
    print("""
ESCOLHA A OPÇÃO DESEJADA
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR VALOR
[4] INSERIR NOVOS VALORES
[5] SAIR DO PROGRAMA
""")
    
    opcao = int(input("Opção: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} + {n2} é {soma}")
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f"A multiplicação entre {n1} X {n2} é {multiplicacao}")
    elif opcao ==3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior valor digitado foi {maior}")
    elif opcao == 4:
        print("Insira os novos valores: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao ==5:
        print("Encerrando programa...")
    else:
        print("Desculpe, não reconheci a opção desejada")

    