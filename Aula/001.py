"""
SISTEMA DE ACESSO: o usuário deve informar nome e senha, o acesso só deve ser permitido se o nome
for "admin" e a senha for "1234" ou "abcd", caso contrário mostre na tela, acesso negado

"""

nome = str(input("Digite o nome: ")).upper()
senha = str(input("Digite a senha: "))

if nome == "ADMIN" and senha == "1234" or "abcd":
    print("Seja bem vindo ao nosso sistema!")
else:
    print("Acesso negado!")
