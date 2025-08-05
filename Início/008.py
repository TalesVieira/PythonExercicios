#Escreva um programa que leia um valor em metros, e o exiba convertendo em cm e mm

medida = float(input('Digite uma distância em metros: '))

centimetros = medida * 100
milimetros = medida * 1000

print(f'A médida de {medida} metros corresponde a {centimetros:.0f} centímetros e {milimetros:.0f} milímetros')