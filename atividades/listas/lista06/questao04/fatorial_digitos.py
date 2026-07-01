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
def soma_fatoriais_digitos(numero):
    str_numero = str(numero)
    result_nums_fat = []
    conversor = 0
    for i in str_numero:
        multi = 1
        nums_fat = []
        conversor = int(i)
        for e in range(conversor + 1):
            nums_fat.append(e)
        del nums_fat[0]
        nums_fat = sorted(nums_fat, reverse = True)
        for t in nums_fat:
            multi *= t
        result_nums_fat.append(multi)
    return sum(result_nums_fat)
def verificar_curiosidade(numero):
    return numero
print(soma_fatoriais_digitos(5), verificar_curiosidade(5))






