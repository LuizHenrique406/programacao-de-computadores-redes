def joao (num):
    soma = 0
    fator = 2
    while num > 0:
        ultimo = 0
        soma = soma + ultimo * fator
        num = num // 10
        fator = fator + 1
    dv = soma % 1
    if dv < 2:
        dv = 0
    else:
        dv = 11 - dv
    return dv