print("Calculadora de Índice de Massa Corporal em idosos")

peso = int(input("Coloque o seu peso: "))
altura = float(input("Coloque a sua altura: "))

IMC = peso / (altura * altura)

if IMC < 22:
    print("Baixo peso")
if IMC >= 22 and IMC <= 27:
    print("Peso Adequado")
if IMC >= 27 and IMC <= 29:
    print("Sobrepeso")
if IMC > 30:
    print("Obesidade")
