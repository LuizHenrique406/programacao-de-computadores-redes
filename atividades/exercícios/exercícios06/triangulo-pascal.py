print("Esse programa lhe apresenta linhas do Triângulo de Pascal")
print()
print("Pode ser 0, caso deseje")
linha = int(input("Digite quantas linhas que deseja do Triângulo de Pascal: "))

quant = 0
l = [1]
print(l)

for _ in range(linha):

    out = [1]

    for i in range(len(l) - 1):
        x = l[i] + l[i + 1]
        out.append(x)

    out.append(1)
    print(out)
    l = out[:]
    out.clear()