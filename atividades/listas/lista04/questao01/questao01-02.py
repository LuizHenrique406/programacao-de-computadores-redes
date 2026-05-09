print("Esse programa acha o número primo na posição 137")

contagem_num = 0
ndiv = 0

while contagem_num < 137:
    div = 1
    ndiv = 0
    
    while div <= num:
        if num % div == 0:
            ndiv = ndiv + 1
        div = div + 1
    
    if ndiv == 2:
        contagem_num = contagem_num + 1

    num = num + 1
    
print("O número primo da posição 137 é", num - 1)