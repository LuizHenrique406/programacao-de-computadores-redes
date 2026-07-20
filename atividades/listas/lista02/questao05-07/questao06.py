print("Esse programa dá o maior número")

num1 = int(input("Digite o valor do primeiro número: "))
num2 = int(input("Digite o valor do segundo número: "))
num3 = int(input("Digite o valor do terceiro número: "))
num4 = int(input("Digite o valor do quarto número: "))

valores = [num1, num2, num3, num4]
max = 0

#print(f"O maior valor é {max(valores)}") # pode ser feito assim tbm, mas é bom praticar só o basíco por agora

for i in valores:
    if i > max:
        max = i
print(f"O maior valor é: {max}")




