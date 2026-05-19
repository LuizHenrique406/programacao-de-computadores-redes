print("Ese programa encontra os dois digítos verificadores do seu CPF")

cpf1 = int(input("Digite seu CFP: "))
soma1 = 0
soma2 = 0
cpf2 = cpf1

for m in range(2,11):
    n1 = cpf1 % 10
    soma1 = soma1 + (n1 * m)
    cpf1 = cpf1 // 10

dv1 = soma1 % 11
if dv1 >= 2:
    dv1 = 11 - dv1
else:
    dv1 = 0

for i in range(2,11):
    n2 = cpf2 % 11
    soma2 = soma2 + (n2 * i)
    cpf2 =  cpf2 // 10

soma2 = soma2 + (dv1 * 1)

dv2 = soma2 % 11
if dv2 >= 2:
    dv2 = 11 - dv2
else:
    dv2 = 0

print(f"O seus dois digitos verficadores são, repectivamente, {dv1} e {dv2}")