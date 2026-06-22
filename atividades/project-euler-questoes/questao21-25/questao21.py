def divisores(n):
    div = []
    for i in range(1, n - 1):
        if n % i == 0:
            div.append(i)
    return sum(div)
divs = []
for i in range(1, 10001):
    div1 = divisores(i)
    div2 = divisores(div1)
    if i not in divs:
        if i == div2:
            print(div1, div2)
            divs.append(div1)
            divs.append(div2)
total = sum(divs)
print(F"A soma total dos números amigáveis foi {total}")