import math
print("Esse programa lhe aprensenta um menu")

opcao = 0

while opcao != 3:
    
    print("1. Capitalização Acumulada")
    print("2. Tempo em que a Dívida chega a um valor")
    print("3. Sair")
    opcao = int(input("Qual é sua opcão?: "))

    if opcao == 1:
        capital = float(input("Digite o seu capital: "))
        taxa_fixa = float(input("Digite o seu juros: "))
        tempo = int(input("Digite o tempo em anos: "))
        montante = capital * ((1 + taxa_fixa / 100)**tempo)

        print(f"O seu montante foi de R${montante:.2f}")
    
    if opcao == 2:
        capital = float(input("Digite o seu capital: "))
        taxa_fixa = int(input("Digite o seu juros: "))
        valor_esperado = float(input("Digite o valor esperado da sua dívida: "))

        tempo = abs(math.log(valor_esperado) - math.log(capital)) / math.log(1 + taxa_fixa / 100)

        print(f"Vai levar {tempo:.1f} anos para chegar em R${valor_esperado}")

print("Valeu!!!")



    