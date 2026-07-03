def num_cartao(num):
    impares = []
    pares = []
    pares_soma = []
    for i in range(len(num[::-1])):
        if i % 2 == 0:
            pares.append(num[i])
        else:
            impares.append(int(num[i]))
    for i in pares:
        multi = int(i) * 2
        if multi <= 9:
            pares_soma.append(multi)
        else:
            for i in str(multi):
                pares_soma.append(int(i))
    if (sum(impares) + sum(pares_soma)) % 10 == 0:
        return "Número de cartão válido"
    else:
        return "Número de cartão inválido"

cartao = input("Digite os 16 digitos do seu cartão: ")
print(num_cartao(cartao))