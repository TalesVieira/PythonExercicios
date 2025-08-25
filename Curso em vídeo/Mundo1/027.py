#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome 
#separadamente

nome = str(input("Digite seu nome completo: "))

nomeSeparado = nome.split()

print(f"Seu primeiro nome é {nomeSeparado[0]}")
print(f"Seu último nome é {nomeSeparado[-1]}")