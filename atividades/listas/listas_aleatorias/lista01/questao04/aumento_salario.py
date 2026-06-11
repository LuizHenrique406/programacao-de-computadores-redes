salario = float(input("Digite o seu sálario: "))
porcento = int(input("Digite a procentagem do aumento: "))
porcento = porcento / 100
aumento = salario * porcento
print(f"O aumento do seu sálario vai ser {aumento:.2f}R$")