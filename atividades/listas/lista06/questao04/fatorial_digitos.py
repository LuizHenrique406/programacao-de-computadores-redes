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
        conversor = int(i)
        multi = fatorial(conversor)
        soma += multi
    return soma
def verificar_curiosidade(numero):
    resultado_soma = soma_fatoriais_digitos(numero)
    if numero == resultado_soma:
        return True
    else:
        return False
def calcular_soma_total(limite):
    nums = []
    for i in range(limite + 1):
        if verificar_curiosidade(i) is True:
            nums.append(i)
    return sum(nums)
print(calcular_soma_total(10000))