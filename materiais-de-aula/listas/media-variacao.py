print("Esse programa calcula a variância")

soma = 0
variancia = 0
x = int(input("Digite um número: "))
z = [x]
b = []

while x > 0:
    soma += x
    x = int(input("Digite um número: "))
    z.append(x)

media = soma / len(z)

for i in z:
    a = (i - media) ** 2
    b.append(a)

v = sum(b)

variancia = v / len(z)

print(f"{variancia:.2f}")