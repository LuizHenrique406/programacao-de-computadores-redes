print("Esse programa calcula divisores uniformemete")
num = 2
div = 2
while div < 21:
    if num % div == 0:
        div = div + 1
    else:
        num = num + 1

if div == 20:
    print("o número dividido uniformemente por 20 foi", num)
else:
    print("nada encontrado")