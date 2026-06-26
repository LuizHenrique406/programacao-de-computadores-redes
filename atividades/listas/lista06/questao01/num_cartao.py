def num_cartao(num_srt):
    par_inicio = []
    pares_resul_final = []
    impares = []
    total = []
    pares_resul_str = []
    num = 0
    multi_par = 0
    conversor = 0
    str_resul_par = 0
    par9_str = 0
    for i in num_srt:
        num += 1
        conversor = int(i)
        if num % 2 == 0:
            par_inicio.append(conversor)
        else:
            impares.append(conversor)
    impares = sum(impares)
    for i in par_inicio:
        multi_par = i * 2
        if multi_par <= 9:
            pares_resul_final.append(multi_par)
        else:
            pares_resul_final = []
            par9_str = str(multi_par)
            str_resul_par = list(par9_str)
            for i in str_resul_par:
                conversor = int(i)
                pares_resul_str.append(conversor)
            for i in range(len(pares_resul_str)):
                num = pares_resul_str[i] + pares_resul_str[i + 1]
                pares_resul_final.append(num)
                break
    pares_resul_final = sum(pares_resul_final)
    total = impares + pares_resul_final
    if total % 10 == 0:
        return total, "Esse número de cartão é válido!!!"
    else:
        return total, "Esse número de cartão não é válido"

num = str(input("Digite 14 digitos: "))
print(num_cartao(num))

# receber primeiro uma sequência de caracteres
# depois usar um for in range e caminhar nessas caracteres
# verificar se o índice é par ou ímpar
# se for ímpar, colocar na lista "impar", depois somar essa lista e colocar o resultado na lista "total"
# se for par, multiplicar por 2 e depois ver se é menor ou igual a 9
# se for menor, colocar na lista "par"
# se for maior, pegamos esse resultado e convertemos para str
# após converter, criar uma novo variável, transforma essa str em lista e colocar ela nessa nova variável
# depois, usar um for pegando essas str, converter essas strs para int, criar uma nova lista e appendar esses ints nessa lista
# depois utilizar um for somando o primeiro índice com o segundo índice