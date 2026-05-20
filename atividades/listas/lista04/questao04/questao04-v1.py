ping = 1
primeiroPing = True
ping_anterior = 0
ping_rapido = 0
qtd_pings = 0

primeiro_jitter = True
menor_jitter = 0

soma = 0

while ping > 0:
    ping = int(input("Ping: "))

    if ping > 0:
        if primeiroPing:
                ping_rapido = ping
                primeiroPing = False
        else:
             jitter = abs(ping_anterior - ping)
             
             if primeiro_jitter:
                  menor_jitter = jitter
                  primeiro_jitter = False
             
             if jitter < menor_jitter:
                menor_jitter = jitter
                  
        if ping < ping_rapido:
             ping_rapido = ping

        ping_anterior = ping        
        
        qtd_pings = qtd_pings + 1
        soma = soma + ping


media = soma/qtd_pings

print("Ping mais rápido:", ping_rapido)
print("Media de latencia", media)
print("Menor Jitter:", menor_jitter)