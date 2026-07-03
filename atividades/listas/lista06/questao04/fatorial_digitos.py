def fatorial(n):
    soma = 1
    num = []
    for i in range(n + 1):
        num.append(i)
    num = sorted(num, reverse = True)
    num.remove(0)
    for i in num:
        soma *= i
    return soma
def soma_fatoriais_digitos(numero):
    str_numero = str(numero)
    soma = 0
    for i in str_numero:
        soma += fatorial(int(i))
    return soma
def verificar_curiosidade(numero):
    resultado_soma = soma_fatoriais_digitos(numero)
    if numero == resultado_soma:
        return [numero, True]
    else:
        return [False]
def calcular_soma_total(limite):
    validos = []
    nums = []
    for i in range(limite + 1):
            veri = verificar_curiosidade(i)
            validos.append(veri)
    for i in validos:
        if len(i) == 2:
            nums.append(i[0])
    return sum(nums)
print(calcular_soma_total(10000))