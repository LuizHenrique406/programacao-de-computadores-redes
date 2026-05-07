print("Esse programa calcula quantos políndromos tem entre 10 e 1000000")

contagem_poli = 1

while contagem_poli < 1000:
    num = 11
    num_invertido = 0

    while num > 0:
        num_invertido = num_invertido * 10 + (num % 10)
        num = num // 10

    if num_invertido == num:
        num = num + 1

    contagem_poli = contagem_poli + 1
    
print("Existem", contagem_poli, "políndromos entre 10 e 1000000")