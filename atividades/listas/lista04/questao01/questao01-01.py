print("Esse programa encontra 137 número primo")
div = 1
num = 2
div_quanti = 1
contagem = 1

while div_quanti < 3 and contagem < 6:
    if num % div == 0:
        num = num + 1
        contagem = contagem + 1
    else:
        div = div + 1