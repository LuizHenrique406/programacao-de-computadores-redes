cpf = int(input("Digite seu CFP: "))
soma = 0
for m in range(2,11):
    n = cpf % 10
    soma = soma + (n * m)
    cpf = cpf // 10

dv1 = soma % 11
if dv1 >= 2:
    dv1 = 11 - dv1
else:
    dv1 = 0

print(dv1)