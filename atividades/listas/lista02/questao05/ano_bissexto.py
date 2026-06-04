print("Esse programa analisa se o ano é bissexto ou não")

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Esse ano é bissexto")
        else:
            print("Esse ano não é bissexto")
            
    print("Esse ano é bissexto")
