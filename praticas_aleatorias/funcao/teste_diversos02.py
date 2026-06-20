def par_impar(num):
    if num % 2 == 0:
        return "Este número é par"
    else:
        return "Este número é ímpar"
print("Verificação de par ou ímpar!")
while True:
    try:
        valor = int(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, apenas números inteiros!!!")
print(par_impar(valor))
def radar_velocidade(velocidade):
    if velocidade > 80:
        return "Multado! Você passou do limite atribuído!"
    else:
        return "Velocidade permitida! Boa viagem!"
print("Verificação de velocidade!")
while True:
    try:
        carro_velocidade = int(input("Digite a sua velocidade: "))
        break
    except ValueError:
        print("Por favor, apenas números inteiros!!!")
print(radar_velocidade(carro_velocidade))
def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Não é possível dividir por zero!!!"
        else:
            return num1 / num2
print(f"OPERAÇÕES:\n+. Soma\n-. Subtração\n*. Multiplicação\n/. Divisão")
operacao = str(input("Digite uma operação: "))
while True:
    if operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/":
        print("Por favor, apenas os operadores listados!!!")
        print()
        print(f"OPERAÇÕES:\n+. Soma\n-. Subtração\n*. Multiplicação\n/. Divisão")
        operacao = str(input("Digite uma operação: "))
    else:
        break
print()
while True:
    try:
        num1 = int(input("Digite um valor: "))
        num2 = int(input("Digite um valor: "))
        break
    except ValueError:
        print("Por favor, apenas números inteiros!!!")
if num2 <= 0:
    print(calculadora(num1, num2, operacao))
elif num2 > 0 and operacao == "/":
    print(f"O resultado foi: {calculadora(num1, num2, operacao):.2f}")