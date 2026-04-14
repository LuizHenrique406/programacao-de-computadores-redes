print("Esse programa calcula o Índice de Massa Corporal")

peso = float(input("Coloque o seu peso: "))
altura = float(input("Coloque a sua altura: "))

imc = peso / (altura**2)
print("O seu IMC é: ", imc)

if imc < 18.5:
    print("MAGRESA")
else:
  if imc <= 24.9:
    print("NORMAL")
  else:
    print("SOBREPESO")
if imc <= 34.9:
    print("OBESIDADE GRAU I")
else:
   print("OBESIDADE GRAU II")
if imc > 40:
    print("OBESIDADE III")
