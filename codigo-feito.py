print("Esse programa analisa os dados de uma viagem")
print()
print("hora no fomato HH e minuto no fomato MM")
horas1 = int(input("Digite a hora da sua partida: "))
minutos1 = int(input("Digite o minutos da sua partida: "))
horas2 = int(input("Digite a hora da sua chegada: "))
minutos2 = int(input("Digite o minuto da sua chegada: "))

total_minutos1 = horas1 * 60 + minutos1
total_minutos2 = horas2 * 60 + minutos2

print("Digite sim ou não")
viagem_dias = str(input("Sua viagem foi no mesmo dia?: "))

if viagem_dias == "sim":
    if total_minutos2 > total_minutos1:
        total_geral = total_minutos2 - total_minutos1
    else:
        print("Erro: horário de chegada deve ser maior que o de partida na mesma dia.")
        exit()
elif viagem_dias == "não":
    dias_viagem = int(input("Há quantos dias você estar viajando?: "))
    total_geral = (total_minutos2 - total_minutos1) + (dias_viagem * 24 * 60)

print()
print("Pausas, almoço e etc, em MINUTOS")
hora_descanso = int(input("Tempo total que seu carro ficou parado: "))
total_geral = total_geral + hora_descanso
print()
combustivel_gasto = float(input("Quantidade total de combustíel gasto em litros: "))
print()
print("Valor em R$")
preco_litro = float(input("Qual foi o valor em R$ do litro de combustível gasto?: "))
print()
print("Distância em Km")
distancia_percorrida = int(input("Qual a distância total percorrida da sua viagem?: "))

horas_final = total_geral // 60
minutos_final = total_geral % 60
print("O tempo tempo total da viagem foi de", horas_final, "horas e", minutos_final, "minutos")

vm = distancia_percorrida / (total_geral / 60)
print("A velocidade média global é", vm)

tempo_movimento = distancia_percorrida / vm
print("O tempo total em movimento foi de", tempo_movimento, "h")

desempenho_carro = distancia_percorrida / combustivel_gasto
print("O seu desempenho foi de:", desempenho_carro, "Km/l")

litros_hora = combustivel_gasto / (total_geral / 60)
print("Seu consumo por hora foi de", litros_hora, "L/h")

custo_total = (distancia_percorrida / desempenho_carro) * preco_litro
print("O seu gasto total na viagem foi de", custo_total, "R$")