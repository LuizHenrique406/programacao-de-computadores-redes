import socket
rede = socket.gethostbyname_ex(socket.getfqdn())
endere_rede = []
ips_srt = []
ips_int = []
convresor = 0
# bloco split; organizando as strings
for i in rede:
    endere_rede.append(i)
del endere_rede[0:2]
for i in endere_rede:
    for e in i:
        ips_srt.append(e.split("."))
# bloco de conversão das strings
for i in ips_srt:
    lista_reseva = []
    for e in i:
        convresor = int(e)
        lista_reseva.append(convresor)
    ips_int.append(lista_reseva)
# bloco de classificação
for i in ips_int:
    if i[0:4] == 0:
        print("Endereço de Rede")
    elif i[0] == 10:
        print("classe A privado")
    elif i[0] == 127:
        print("Endereço loopback")
    elif i[0] == 172 and i[1] >= 16 and i[1] <= 31:
        print("classe B privado")
    elif i[0] == 169 and i[1] == 254:
        print("APIPA privado")
    elif i[0] == 192 and i[1] == 168:
        print("classe C privado")
    elif i[0] >= 224 and i[0] <= 240:
        print("Endereço Multicast")
    elif i[0] >= 241 and i[0] <= 255:
        print("Endereço Reservado")
    elif i[0:4] == 255:
        print("Broadcast")
    else:
        print("Endereço público")