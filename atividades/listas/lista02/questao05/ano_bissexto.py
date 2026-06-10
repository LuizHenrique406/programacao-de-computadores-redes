print("Esse programa analisa se o ano é bissexto ou não")

ano = int(input("Digite o ano: "))
ultimos = ano % 100

if ultimos == 0:
    if ano % 400 ==0 and ano % 4 == 0:
        print("É bissexto")
    elif ano % 400 == 0:
        ("É bissexto")
    else:
        print("Não é bissexto")
else:
    if ano % 4 == 0:
        print("É bissexto")
    else:
        print("Não é bissexto")