print("Esse programa encontra a soma dos únicos onze primos que são simultaneamente truncáveis da esquerda para a direita e da direita para a esquerda.")
def num_primo(n):
    divs = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divs += 1
    if divs == 2:
        return True
    else:
        return False
def veri_esquerda(n):
    s = str(n)
    while len(s) > 0:
        if not num_primo(int(s)):
            return False
        s = s[1:]
    return True
def veri_direita(n):
    s = str(n)
    while len(s) > 0:
        if not num_primo(int(s)):
            return False
        s = s[:-1]
    return True
onze_trunc = []
soma = 0
for i in range(11, 1000001):
    if veri_esquerda(i) and veri_direita(i):
        onze_trunc.append(i)
print(f"Os 11 primos truncáveis são: {onze_trunc}")
print(f"A soma dos números truncáveis é {sum(onze_trunc)}")