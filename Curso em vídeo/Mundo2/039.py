#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele ainda vai se alistar
#ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento, seu programa tbm deve mostrar
#o tempo que falta ou que passou do prazo

from datetime import date
anoAtual = date.today().year

nascimento = int(input("Digite o ano de nascimento do usuário: "))

idade = anoAtual - nascimento

if idade == 18:
    print("Você precisa se alistar AGORA!")
elif idade < 18:
    tempoRestante = 18 - idade
    print(f"Você não precisa se alistar, volte em {tempoRestante} anos")
else:
    tempoRestante = idade - 18
    print(f"Você está atrasado em {tempoRestante} para o alistamento..")