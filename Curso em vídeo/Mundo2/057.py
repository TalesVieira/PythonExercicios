#Faça um programa que leia o sexo de uma pessoa, mas so aceite valors M ou F, caso esteja errado, peça a digitação novamente até 
#ter um valor correto

sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()

while sexo not in ("M", "F"):
    print(f"O valor digitado '{sexo}' não foi reconhecido, tente novamente")
    sexo = str(input("Qual é o seu sexo? [M/F]: ")).strip().upper()

