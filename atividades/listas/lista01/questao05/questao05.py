print("Reformas de Previdência")

capital_incial = float(input("Digite o seu capital inicial: "))
novo_capital = float(input("Digite o seu novo depósito: "))
taxa_mensal = int(input("Digite o seu juros mensal: "))
meses = int(input("Quanto tempo a sua previdência ficou rendendo?: "))

novo_capital = meses * novo_capital

saldo = capital_incial * (1 + taxa_mensal/100) ** meses + novo_capital * ((1 + taxa_mensal/100)**meses - (1 + taxa_mensal//100)) / (taxa_mensal/100)

print(f"{saldo:.2f}")