print("Esse programa analisa o quão estável está a sua rede")

time1 = int(input("Digite o tempo de seu ping: "))
time2 = int(input("Digite o tempo de seu ping: "))

ping_rapido = 0
cal_jitter = 0
jitter = 0
latencia_med = 0
soma = 0
med = 0


while time1 > 0 and time2 > 0:
    time1 = int(input("Digite o tempo de seu ping: "))
    time2 = int(input("Digite o tempo de seu ping: "))
    soma = soma + time1 + time2
    med = med + 1

    if time1 < time2:
        ping_rapido = time1
    else:
        ping_rapido = time2

latencia_med = soma / med

print("A latência média foi de", latencia_med)
print("E seu ping mais rápido foi de", ping_rapido)