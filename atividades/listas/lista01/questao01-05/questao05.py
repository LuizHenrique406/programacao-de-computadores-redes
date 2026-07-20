print("Esse programa lhe apreseta um menu")

opcao = 0

while opcao != 3:

    print("1. Saldo da Previdência após n meses\n2. Saldo esperado da previdência após n meses\n3. sair ")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        capital_inicial = float(input("Digite o seu capital inicial: "))
        novo_capital = float(input("Digite o seu novo depósito: "))
        taxa_mensal = int(input("Digite o seu juros mensal: "))
        mes = int(input("Quanto tempo a sua previdência ficou rendendo?(em meses): "))

        novo_capital = mes * novo_capital

        saldo = capital_inicial * (1 + taxa_mensal/100) ** mes + novo_capital * ((1 + taxa_mensal/100)**mes - (1 + taxa_mensal//100)) / (taxa_mensal/100)

        print(f"O seu saldo foi de {saldo:.2f}")

    if opcao == 2:
        capital_inicial = float(input("Digite o seu capital inicial: "))
        novo_capital = float(input("Digite o seu novo depósito: "))
        taxa_mensal = int(input("Digite o seu juros mensal: "))
        valor_esperado = int(input("Qual valor deseja atingir?: "))

        mes = 0
        saldo = 0

        while valor_esperado >= saldo:

            mes += 1

            saldo = capital_inicial * (1 + taxa_mensal/100)**mes + novo_capital * ((1 + taxa_mensal/100)**mes - 1) / (taxa_mensal/100)

        anos = mes / 12

        print(f"Irá demorar {anos:.2f} anos ou {mes} meses para o seu saldo chegar nesse valor")
