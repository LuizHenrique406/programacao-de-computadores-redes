print("Eesse programa encontra a soma de todos os números que podem ser escritos como a soma das quintas potências de seus dígitos")
def pot_dig(n):
    nums = []
    soma = 0
    for i in str(n):
        nums.append(i)
    for i in nums:
        soma += int(i) ** 5
    if soma == n:
        return soma
    else:
        return 0
soma = 0
for i in range(2, 194980):
    soma += pot_dig(i)
print(f"A soma desses números foi de {soma}")