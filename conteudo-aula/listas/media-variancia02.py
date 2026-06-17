print("Esse programa calcula a variância")

qtde = 0
soma = 0
variancia = 0
desvio = 0
quadrado = 0

x = int(input("Digite um número: "))
z = [x]

while x > 0:
    soma += x
    qtde += 1
    x = int(input("Digite um número: "))
    z.append(x)

media = soma / qtde


for i in range(len(z)):
    desvio = z[i] - media
    z[i] = desvio

for i in range(len(z)):
    quadrado = z[i] ** 2
    z[i] = quadrado

for i in z:
    quadrado += i

variancia = quadrado / qtde

print(f"A variância foi de {variancia}")