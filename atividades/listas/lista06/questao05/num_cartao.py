def num_cartao(num):
    impares_str = []
    pares_srt = []
    pares_int = []
    impares_int = []
    converor = 0
    num_para_srt = 0
    guardar_num_srt = 0
    list_2num_srt = 0
    pos = 0
    total = 0
    for i in range(len(num)):
        pos += 1 
        if pos % 2 == 0:
            pares_srt.append(num[i])       
        else:
            impares_str.append(num[i])
    for i in pares_srt:
        converor = int(i)
        pares_int.append(converor)
    for i in impares_str:
        converor = int(i)
        impares_int.append(converor)
    for i in pares_int:
        pares_srt = []
        if i * 2 <= 9:
            total += i * 2
        else:
            num_para_srt = i * 2
            guardar_num_srt = str(num_para_srt)
            list_2num_srt = list(guardar_num_srt)
            for i in list_2num_srt:
                converor = int(i)
                total += converor
    total += sum(impares_int)
    if total % 10 == 0:
        return total, "Número de cartão válido"
    else:
        return total, "Número de cartão inválido"
cartao = input("16 digitos: ")
print(num_cartao(cartao))