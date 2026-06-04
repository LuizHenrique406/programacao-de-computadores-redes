print("Esse programa coloca 3 valores em Ordem Crescente")

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

valores = [num1, num2, num3]
ordem = []
valor = valores[1]

for i in range(len(valores)):
    if valores[i] < valor:
        ordem.append(valores[i])
    else:
        ordem.append(valores[i])
    valor = valores[i]
    

print(f"A a ordem ficou: {ordem}")