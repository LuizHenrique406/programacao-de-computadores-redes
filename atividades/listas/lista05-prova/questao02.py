print("Esse programa valida o seu CPF")

cpf = int(input("Digite os 9 primeiros digitos do seu CPF: "))
dv1 = int(input("Digite o seu primeiro digito verificador: "))
soma = 0

for m in range(3,11):
    u2 = cpf % 10
    soma = soma + (u2 * m)
    cpf = cpf // 10

soma = soma + (dv1 * 2)

dv1 = soma % 11
if dv1 >= 2:
    dv1 = 11 - dv1
else:
    dv1 = 0

print(f"O seu segundo digito verificador é {dv1}")