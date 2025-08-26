#escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80kmh, mostre uma mensagem falando que
#ele foi multado, a multa vai custar 7 reais para cada km acima do limite

velocidadePermitida = 80

velocidadeCarro = int(input("A quantos km/h estava o veículo? kmh:"))

if velocidadeCarro > velocidadePermitida:
    multa = (velocidadeCarro - 80) * 7
    print(f"O veículo está acima da velocidade permitida de 80km/h, sua multa vai ser de R${multa:.2f}")
else:
    print("O veículo está dentro do limite de velocidade!")
