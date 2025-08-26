#Desenvolva um programa que pergunte a distância de uma viagem em KM, e calcule o preço da passagem cobrando
#R%0.50 por km para viagens de até 200KM e R$0.45 Para viagens mais longas

distancia = int(input("Quantos KM tem sua viagem?: KM "))

if distancia <= 200:
    valorDaPassagem = 0.50 * distancia
else:
    valorDaPassagem = 0.45 * distancia

print(f"Sua viagem de {distancia}KM, vai custar {valorDaPassagem}")