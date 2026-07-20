print("Esse programa soma aepnas números ímpares")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

valores = [num1, num2, num3, num4]
soma = 0
for i in valores:
    if i % 2 == 1:
        soma = soma + i

print(f"A soma dos números ímpares foi {soma}")