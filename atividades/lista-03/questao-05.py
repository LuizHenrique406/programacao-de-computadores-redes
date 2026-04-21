print("Esse programa calcula o valor final da apólice de seguro de um veículo")
valor_carro = float(input("Qual o valor do carro a segurar?: "))
idade_condutor = int(input("Quantos anos você tem?: "))

if idade_condutor >= 18:
    valor_base = valor_carro * 0.05
    if idade_condutor >= 18 and idade_condutor <= 24:
        valor_base = valor_carro * 0.20
    else:
        if idade_condutor <= 60:
            print("Sem adicional")
        else:
            valor_base = valor_carro * 0,10

    print("Digite T para TRABALHO e L para LAZER")              
    trabalho_lazer = str(input("Uso do veículo é para TRABALHO ou LAZER?: "))

    if trabalho_lazer == "T":
        valor_base + 300
    else:
        valor_base - 100

    acidentes_ano = int(input("Quantos acidentes você teve no último ano?: "))

    valor_base = (acidentes_ano * 300) + valor_base
    if valor_base < 7000:
        print(valor_base)
        print("Seu seguro pode ser contratado")
    else:
        print("Seu seguro está sob análise") 
else:
    print("CONTRATAÇÃO REJEITADA")
