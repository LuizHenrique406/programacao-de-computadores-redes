cigarros_dias = int(input("Digite quantos cigarros você fuma por dia: "))
anos_fumando = int(input("Digite a quantidade de anos você fuma: "))
minutos = cigarros_dias * 20
perda_vida = (anos_fumando * 365) * (minutos / 60)
perda_vida = perda_vida / 24
print(f"Você perdeu {perda_vida:.0f} dias de vida")