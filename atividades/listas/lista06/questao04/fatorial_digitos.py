def fatorial(n):
    soma = 1
    num = []
    for i in range(n + 1):
        num.append(i)
    num = sorted(num, reverse = True)
    num.remove(0)
    for i in num:
        soma = soma * i
    return soma
def 
