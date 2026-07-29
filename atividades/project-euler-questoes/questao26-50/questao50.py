def num_primo(n):
    divs = 1
    for i in range(2, n + 1):
        if n % i == 0:
            divs += 1
    if divs == 2:
        return n
    else:
        return 1
def soma_num_primo(n):
    primos = []
    nums = []
    veri = False
    soma = 0
    for i in range(2, n + 1):
        divs = 1
        for j in range(2, i + 1):
            if i % j == 0:
                divs += 1
        if divs == 2:
            primos.append(i)
    while not veri:  
        soma = 0
        nums = []
        for i in primos:
            soma += i
            nums.append(i)
            if soma == n:
                veri = True
                break
        primos = primos[1:]
        if len(primos) == 0:
            break
    if soma == n and len(nums) > 1:
        return nums, len(nums), soma
    else:
        return 0, 0, 0
for i in range(2, 100):
    num = num_primo(i)
    primos, contagem, soma = soma_num_primo(num)
    if soma == num:
        print(f"número primo: {num}\nprimos e a quantidade de primos: {primos}, {contagem}\nsomando os a quantidade de primos: {soma}")