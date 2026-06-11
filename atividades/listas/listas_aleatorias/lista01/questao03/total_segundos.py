dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segudnos: "))
total = 0
total += dias * 24 * 60 * 60
total += horas * 60 * 60
total += minutos * 60
total += segundos
print(f"O total de segundos foram {total}sec")