#Escreva um programa que leia um número inteiro qualquer e pela para o usuário escolher a base de conversão
# 1 - binário
# 2 - octal
# 3 - hexadecimal

numero = int(input("Digite um número inteiro: "))

print("-=-" *20)
print("""
      ESCOLHA UMA DAS BASES PARA CONVERSÃO:
      [1] BINÁRIO
      [2] OCTAL
      [3] HEXADECIMAL
      """)
print("-=-" *20)

opcao = int(input("Qual você escolhe? "))

if opcao == 1:
    print(f"{numero} convertido para binário é {bin(numero)}")
elif opcao == 2:
    print(f"{numero} convertido para octal é {oct(numero)}")
elif opcao == 3:
    print(f"{numero} convertido para hexadecimal é {hex(numero)}")
else:
    print("A opção selecionada infelizmente é inválida")
