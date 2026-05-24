print("Esse programa calcula a variância")

qtde = 0
soma = 0
variancia = 0
x = int(input("Digite um número: "))
z = [x]

while x > 0:
    soma += x
    qtde += 1
    x = int(input("Digite um número: "))
    z.append(x)

media = soma / qtde

for i in z:
    variancia += (i - media) ** 2

variancia = variancia / qtde

print(f"{variancia:.2f}")