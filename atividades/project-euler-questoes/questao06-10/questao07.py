contador = 0
ndiv = 0
num = 0
for e in range(1, 20000):
    ndiv = 1
    for i in range(2, e + 1):
        if e % i == 0:
            ndiv += 1
        if ndiv < 2:
            contador += 1
            num = e
            break
    if contador == 10000:
        break
print(num, contador)