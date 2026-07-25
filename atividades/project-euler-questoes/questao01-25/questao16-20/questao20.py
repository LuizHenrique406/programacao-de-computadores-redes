def fatorial(n):
    soma = 1
    num = []
    for i in range(1, n + 1):
        num.append(i)
    num = num[::- 1]
    for i in num:
        soma = soma * i
    return soma
def soma_dig(n):
    num = str(n)
    for i in num:
        soma += i