opcao = 0

while opcao != 5:
    print("1. soma")
    print("2. subitração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. sair")

    opcao = int(input("Digite sua opção: "))
 
    if opcao < 5:

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo númerpo: "))

        if opcao == 1:
            resultado = num1 + num2
        if opcao == 2:
            resultado = num1 - num2
        if opcao == 3:
            resultado = num1 * num2
        if opcao == 4:
            resultado = num1 / num2

        print(f"O resultado é {resultado}")
        
print("Bye!!!")