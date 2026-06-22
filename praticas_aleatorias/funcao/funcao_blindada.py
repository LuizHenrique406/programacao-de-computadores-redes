def calcular_total(valor_conta, porcentagem_gorgeta = 10):
    resultado = valor_conta + ((porcentagem_gorgeta / 100) * valor_conta)
    return f"O valor da conta foi {resultado}"
valor_conta = float(input("Qual o valor da conta?: "))
opcao = 0
while opcao != 2:
    print("Deseja dar uma porcentegem maior ao garçom?\n1. SIM\n2. NÃO")
    opcao = int(input("Qual sua escolha?: "))
    if opcao == 1:
        gorgeta = int(input("Qual a porcentagem da gorgeta?: "))
        break
    if opcao == 2:
        break
if opcao == 1:
    print(f"{calcular_total(valor_conta, gorgeta)}")
if opcao == 2:
    print(f"{calcular_total(valor_conta)}")

