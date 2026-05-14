print("Programa encontra a maior cadeia de um número inteiro da conjectura de Collatz")

veri_cadeia1 = 0
veri_cadeia2 = 0
maior_cadeia = 0
for num in range(1000000):
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            veri_cadeia1 = veri_cadeia1 + 1
        else:
            num = 3 * num + 1
            veri_cadeia1 = veri_cadeia1 + 1

    if veri_cadeia1 > veri_cadeia2:
        maior_cadeia = num
    else:
        maior_cadeia = num

    veri_cadeia2 = veri_cadeia1