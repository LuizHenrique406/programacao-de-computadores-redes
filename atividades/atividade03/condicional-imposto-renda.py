print("Esse programa calcula o seu imposto de renda")

renda = float(input("Digite o seu salário mensal: "))

if renda < 2428.80:
    print("Não precisa pagar imposto de renda")
elif renda <= 2826.65:
    imposto_renda1 = renda * 7.5 / 100 - 182.16
    print("Você irá precisar pagar: ", imposto_renda1)
elif renda <= 3751.05:
    imposto_renda2 = renda * 15 / 100 - 394.16
    print("Você irá precisar pagar: ", imposto_renda2)
elif renda <= 4664.68:
    imposto_renda3 = renda * 22.5 / 100 - 675.49
    print("Você irá precisar pagar: ", imposto_renda3)
else:
    imposto_renda4 = renda * 27.5 / 100 - 908.73
    print("Você irá precisar pagar: ", imposto_renda4)
