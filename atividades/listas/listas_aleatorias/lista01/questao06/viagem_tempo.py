distancia = int(input("Qual a distância que você irá percorrer?: "))
velocidade = int(input("Qual a sua velocidade média esperada?: "))
tempo = distancia / velocidade
tempo1 = tempo * 60
print(f"O tempo da sua viagem será de {tempo:.1f}h ou {tempo1:.0f}min")
