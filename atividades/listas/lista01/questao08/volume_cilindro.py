import math

print("Esse programa calcula o volume de um cilindro")

base = float(input("Digite a base do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

raio = base / 2

volume = math.pi * ((raio ** 2) * altura)

print(f"O volume do cilindro é {volume:.2f}cm³")