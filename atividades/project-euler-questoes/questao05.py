print("Esse programa calcula divisores uniformemete")
num = int(input("Digite um valor: "))
div = 1
while div < 21:
    if num % div == 0:
        div = div + 1
