print("Esse programa calcula que precisas tirar na última prova")

traba1 = float(input("Digite a nota do seu primeiro trabalho: "))
prova1 = float(input("Digite a nota da sua primeira prova: "))
traba2 = float(input("Digite a nota do seu segundo trabalho: "))


traba1 = (traba1 * 30) / 100
prova1 = (prova1 * 70) / 100
unidade1 = traba1 + prova1

traba2 = (traba2 * 30) / 100

unidade2 = traba2

med_final = ((unidade1 * 40  + unidade2 * 60) / 100)


print(f"A nota que você precisa tirar na última prova é {med_final}")
