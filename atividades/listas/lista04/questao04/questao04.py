print("Esse programa analisa o quão estável está a sua rede")

time1 = int(input("Digite o tempo de seu ping: "))
time2 = int(input("Digite o tempo de seu ping: "))
time3 = int(input("Digite o tempo de seu ping: "))
time4 = int(input("Digite o tempo de seu ping: "))

ping_rapido = 0
jitter1 = 0
jitter2 = 0
jitter3 = 0
latencia_med = 0
soma = 0
med = 0
maior_jitter = 0

while time1 > 0 and time2 > 0:
    time1 = int(input("Digite o tempo de seu ping: "))
    time2 = int(input("Digite o tempo de seu ping: "))
    time3 = int(input("Digite o tempo de seu ping: "))
    time4 = int(input("Digite o tempo de seu ping: "))
    if time1 < 0 and time2 < 0 and time3 < 0 and time4 < 0:
        print("Apenas números inteiros positivos")
        break

    jitter1 = abs(time1 - time2)
    jitter2 = abs(time2 - time3)
    jitter3 = abs(time3 - time4)

    if jitter1 < jitter2:
        maior_jitter = jitter1
    else:
        if jitter2 < jitter1:
            maior_jitter = jitter2
        else:
            if jitter3 < jitter1:
                maior_jitter = jitter3
            else:
                if jitter3 < jitter2:
                    maior_jitter = jitter3

    soma = soma + time1 + time2
    med = med + 2

    if time1 > 0 and time1 < time2 and time1 < time3 and time1 < time4:
        ping_rapido = time1
    else:
        if time2 > 0 and time2 < time1 and time2 < time3 and time2 < time4:
            ping_rapido = time1
        else:
            if time3 > 0 and time3 < time1 and time3 < time2 and time3 < time4:
                ping_rapido = time1
            else:
                if time4 > 0 and time4 < time1 and time4 < time2 and time4 < time3:
                    ping_rapido = time1

latencia_med = soma / med

print("A latência média foi de", latencia_med)
print("E seu ping mais rápido foi de", ping_rapido)
print("O menor Jitter da sequência foi", maior_jitter)