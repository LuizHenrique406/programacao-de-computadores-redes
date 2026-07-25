def num_perfeito(n):
    divs = 0
    for i in range(1, n):
        if n % i == 0:
            divs += i
    if n == divs:
        return divs
    else:
        return 0
soma = 0
for i in range(1, 28123):
    soma += num_perfeito(i)
print(soma)