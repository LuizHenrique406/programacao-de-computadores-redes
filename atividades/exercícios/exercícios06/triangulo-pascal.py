print("Esse programa lhe apresenta o Triângulo de Pascal")

e = [1,2,1]
g = e.copy()
linha = 2
print(e)

x = 2
e[x] = g[x] + g[x - 1]
x = 1
e[x] = g[x] + g[x - 1]
e.append(1)
linha = 3
print(e)
g = e.copy()

x = 1
e[x] = g[x] + g[x - 1]
x = 2
e[x] = g[x - 1] + g[x - 1]
x = 3
e[x] = g[x] + g[x - 1]
e.append(1)
linha = 4
g = e.copy()

print(e)

