def tercino(a, b, c):
    resultado = (a ** 2) + (b ** 2) + (c ** 2)
    return resultado
a = 0
b = 0
c = 0
num = 0

for i in range(1, 50):
    a = i
    for e in range(2, 50):
        b = e
        for w in range(3, 50):
            c = w
            num = tercino(a,b,c)
            print(num)
            break