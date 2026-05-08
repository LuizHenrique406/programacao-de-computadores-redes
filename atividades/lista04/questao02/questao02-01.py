print("Esse programa calcula quantos políndromos tem entre 10 e 1000000")

contagem_poli = 0
num1 = 10
num2 = num1
num_invertido = 0

while num1 < 1000001:
    num2 = num1
    while num2 > 0:
        num_invertido = num_invertido * 10 + (num2 % 10)
        num2 = num2 // 10

    if num_invertido == num1:
        num_invertido = 0
        num1 = num1 + 1
        contagem_poli = contagem_poli + 1
    else:
        num_invertido = 0
        num1 = num1 + 1

print("Existem", contagem_poli, "políndromos entre 10 e 1000000")