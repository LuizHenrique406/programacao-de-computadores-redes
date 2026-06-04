import math

print("Calculaodra de Equação do 2° Grau")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > 0:
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print("Essa equeção não possui nenhuma raíz")

    if delta > 0:
        x1 = -(b + (math.sqrt(delta))) / (2 * a)
        x2 = -(b - (math.sqrt(delta))) / (2 * a)
        if x1 != x2:
            print(f"Essa equação possui duas raízes distintas: {x1} e {x2}")

    if delta == 0:
        x1 = -(b + (math.sqrt(delta))) / (2 * a)
        x2 = -(b - (math.sqrt(delta))) / (2 * a)
        if x1 == x2:
            print(f"Essa equação possui duas raízes iguais: {x1} e {x2}")         
else:
    print("O coeficiente a tem que ser maior que zero")

if b == 0 and c == 0:
    resultado = b / a
    x1 = +(math.sqrt(resultado))
    x2 = -(math.sqrt(resultado))
    print(f"Essa equação possui apenas uma raíz: {x1}")