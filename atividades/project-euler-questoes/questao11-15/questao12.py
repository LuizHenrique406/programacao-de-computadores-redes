def num_triangulo(n):
    soma = 0
    divs = []
    for i in range(n + 1):
        soma += i
    for i in range(1, soma + 1):
        if soma % i == 0:
            divs.append(i)
    return soma, len(divs)

for i in range(2000):
    resul_soma, resul_divs = num_triangulo(i)
    if resul_divs > 200:
        print(f" O número triangular com mais de 500 divisores é {resul_soma}, com {resul_divs}")
