print("Esse programa lhe aprensenta um menu")

opcao = 0
num_div = 0
soma_num = 0

while opcao != 5:
    print("1. Múltiplos de 3 e 5")
    print("2. soma")
    print("3. Dívisiveis de 3")
    print("4. Área do Triângulo")
    print("5. sair")

    opcao = int(input("Digite a sua opcão: "))

    if opcao < 4:

        intervalo1 = int(input("Digite qual o ínicio do intervalo: "))
        intervalo2 = int(input("Digite qual o final do intervalo: "))

        if opcao == 1:
            for o in range(intervalo1, intervalo2 + 1):
                if (o % 3 == 0) or (o % 5 == 0):
                    print(f"{o} é divísivel por 3 e 5")

        if opcao == 2:
            for w in range(intervalo1, intervalo2 + 1):
                soma_num = soma_num + w
                
            print(f"O resultado da soma entre os intervalos é {soma_num}")

        if opcao == 3:
            for t in range(intervalo1, intervalo2 + 1):
                if (t % 3 == 0):
                    num_div = num_div + 1

            print(f"Há {num_div} de dvisores por 3 nesse intervalo")

    if opcao == 4:
        base = int(input("Digite a base de um triângulo: "))
        altura = int(input("digite a altura de um triângulo: "))
        area = base * altura
        print(f"A área desse triângulo é {area}")
    
print("Bye!!!")