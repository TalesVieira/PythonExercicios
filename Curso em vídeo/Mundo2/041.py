# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria:
# Até 9 anos = Mirim
# Até 14 anos = Infantil
# Até 19 anos = Júnior
# Até 25 anos = Sênior
# Acima = Master

from datetime import date

anoAtual = date.today().year
anoDeNascimento = int(input("Qual o ano de nascimento do atleta?: "))

idade = anoAtual - anoDeNascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos e se encaixa na categoria MIRIM")
elif idade <= 14:
    print(f"O atleta tem {idade} anos e se encaixa na categoria INFANTIL")
elif idade <= 19:
    print(f"O atleta tem {idade} anos e se encaixa na categoria JÚNIOR")
elif idade <= 25:
    print(f"O atleta tem {idade} anos e se encaixa na categoria SÊNIOR")
else:
    print(f"O atleta tem {idade} anos e se encaixa na categoria MASTER")
