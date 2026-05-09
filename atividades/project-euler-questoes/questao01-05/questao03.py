div = 2
num = int(input("Digite um número: "))
maior = 2
while num > 1:
    if num % div == 0:
        num = num // div
        maior = div
    else:
        div = div + 1
print("O maior divisor foi", maior)