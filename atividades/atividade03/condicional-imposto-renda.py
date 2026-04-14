print("Esse programa calcula o seu imposto de renda")

renda = float(input("Coloque o seu salário mensal: "))

if renda < 2.428.80:
    pritn("Não precisa pagar imposto de renda")
else:
    if renda <= 2.826.65:
        imposto_renda1 = renda * 7.5 / 100 - 182.16
        print("Você irá precisar pagar: "), imposto_renda1)
            else:
                imposto_renda2 = renda * 15 / 100 - 394.16
                print("Você irá precisar pagar: "), imposto_renda2)
                      if renda <= 4.664.68:
                            imoposto_renda3 = renda * 22.5 / 100 - 675.49
                            print("Você irá precisar pagar: "), imposto_renda3)
                                else:  
                                    imposto_renda4 = renda * 27.5 / 100 - 908,73
                                    print("Você irá precisar pagar: "), imposto_renda4)
