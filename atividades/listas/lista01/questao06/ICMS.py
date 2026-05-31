print("Esse programa calucula o imposto do ICMS")

compra = float(input("Digite o valor da compra da sua mercadoria: "))
venda = float(input("Digite o valor da venda de seu mercadoria: "))


icms = compra - venda

icms = icms * (17 / 100)

if icms > 0:
    print(f"O valor a ser recolhido pela empresa é de {icms}")
if icms < 0:
    print(f"Sua empresa irá acumula {icms:.2f} de crédito")