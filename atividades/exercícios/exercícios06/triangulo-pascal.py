print("Esse programa lhe apresenta o Triângulo de Pascal")

e = [1,2,1]

linha = 3

x = 2
e[x] = e[x] + e[x - 1]
x = 1
e[x] = e[x] + e[x - 1]
e.append(1)
print(e)

