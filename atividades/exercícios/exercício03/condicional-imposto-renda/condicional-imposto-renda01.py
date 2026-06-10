print("Esse programa calcula o seu Imposto de R6000enda")

renda = float(input("Digite o seu sálario mensal: "))

if renda < 2428.80:
    print("ISENTO")
else:
    if renda <= 2826.65:
        imposto = renda * 7.5 / 100 - 182.16
        print("Você irá pagar: ", imposto)
    else:
       if renda <= 3751.05:
            imposto = renda * 15/ 100 - 394.16
            print("Você irá pagar: ", imposto)
       else:
          if renda <= 4664.68:
            imposto = renda * 22.5 / 100 - 675.49
            print("Você irá precisar pagar: ", imposto)
          else:
            imposto = renda * 27.5 / 100 - 908.73
            print("Você irá precisar pagar: ", imposto)
