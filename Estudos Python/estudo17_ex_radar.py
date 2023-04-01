velocidade = 70
local_carro = 94

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

radar_atingido = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if radar_atingido and velocidade > RADAR_1:
    print('Carro multado em radar 1')
elif radar_atingido and velocidade <= RADAR_1:
    print('Carro não passou do limite máximo')
else:
    print('Carro ainda não passou pelo radar')

# Chat gpt
'''
limite_velocidade = 80  # limite de velocidade em km/h
local_carro = input("Digite o local atual do carro: ")
local_radar = input("Digite o local do radar: ")

# loop para verificar a velocidade do carro
while True:
    velocidade_carro = float(input("Digite a velocidade do carro em km/h: "))

    if velocidade_carro > limite_velocidade:
        print("Você excedeu o limite de velocidade de", limite_velocidade, "km/h no local", local_radar)
        # aqui você pode adicionar outras ações, como uma multa ou pontuação na carteira
        break  # encerra o loop após verificar a velocidade do carro
    else:
        print("Sua velocidade está dentro do limite permitido no local", local_radar)

    # verifica se o carro passou do radar
    if local_carro == local_radar:
        print("O carro passou do radar.")
        break  # encerra o loop após verificar se o carro passou do radar
'''