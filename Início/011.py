#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
#necessária para pintá-la sabendo que cada litro de tinta ocupa uma área de 2m2

#area = largura * altura

largura = float(input('Largura da parede: '))
altura =  float(input('Altura da parede: '))

area = largura * altura

print(f"Sua parede tem a dimensão de {altura}x{largura} e sua área é de {area}m")

tintaNescessaria = area / 2

print(f'Para pintar sua parede, será nescessário {tintaNescessaria}l de tinta')