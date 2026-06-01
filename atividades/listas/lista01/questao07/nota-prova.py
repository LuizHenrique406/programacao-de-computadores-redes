print("Esse programa calcula que precisas tirar na última prova")

traba1 = float(input("Digite a nota do seu primeiro trabalho: "))
prova1 = float(input("Digite a nota da sua primeira prova: "))
traba2 = float(input("Digite a nota do seu segundo trabalho: "))


traba1 = traba1 * (30 / 100)
prova1 = prova1 * (70 / 100)

unidade1 = (traba1 + prova1) * (40 / 100)

traba2 = (traba2 * (30 / 100)) * (60 / 100)

prova2 = abs((unidade1 + traba2) - 200)

print(f"A nota que você precisa tirar na última prova é {prova2}")
