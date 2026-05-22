print("Esse programa valida o seu CPF")

cpf = int(input("Digite os 9 primeiros digitos do seu CPF: "))
dv1 = int(input("Digite o seu primeiro digito verificador: "))
soma = dv1 * 2

for m in range(3,11):
    u2 = cpf % 10
    soma += (u2 * m)
    cpf = cpf // 10



dv2 = soma % 11
if dv2 >= 2:
    dv2 = 11 - dv2
else:
    dv2 = 0

print(f"O seu segundo digito verificador é {dv2}")