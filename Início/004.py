#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações
#Possíveis sobre ele

dado = input('Digite algo:')

print(f'O tipo primitivo desse dado é {type(dado)}')
print('Só tem espaços? ', dado.isspace())
print(f'É um número? {dado.isnumeric()}')
print('É alfabético?', dado.isalpha())
print(f'É alfanumérico? {dado.isalnum()}') #Números e letras
print('Está em maiúsculas? ', dado.isupper())
print(f'Está em minúsculas? {dado.islower()}')
print('Está capitalizada? ', dado.istitle()) #Primeira letra maiúscula