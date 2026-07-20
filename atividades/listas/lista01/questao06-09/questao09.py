print("Programa Computador de Bordo")

viagem_tempo = int(input("Digite quanto tempo a sua viagem durou(em minutos): "))
gasto_combustivel = float(input("Digite quando L de combustível foi gasto: "))
preco_combustivel = float(input("Digite qual o preço do litro de combustível: "))
distancia_viagem =  float(input("Digite qual a distância percorrida no total: "))

vm = distancia_viagem / (viagem_tempo / 60)  
print(f"A sua velocidade média foi de {vm:.2f}km/h")

desempenho_carro = distancia_viagem / gasto_combustivel
litro_hora = gasto_combustivel / (viagem_tempo / 60)
custo_km = preco_combustivel / desempenho_carro
print(f"O desempenho do seu carro foi de {desempenho_carro:.2f}km/l, {litro_hora:.2f}l/h e {custo_km:.2f}R$/km")

custo_viagem = (distancia_viagem / desempenho_carro) * preco_combustivel
print(f"Você gastou {custo_viagem:.2f}R$ na viagem")
