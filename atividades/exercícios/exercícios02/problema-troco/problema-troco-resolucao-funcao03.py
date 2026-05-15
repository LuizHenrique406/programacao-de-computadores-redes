def calculo_troco(valor_pago, valor_conta):
    troco = valor_pago - valor_conta

    ced200 = troco // 200
    troco = troco % 200

    ced100 = troco // 100
    troco = troco % 100

    ced50 = troco // 50
    troco = troco % 50

    ced20 = troco // 20
    troco = troco % 20

    ced10 = troco // 10
    troco = troco % 10

    ced5 = troco // 5
    troco = troco % 5

    ced2 = troco // 2
    troco = troco % 2

    return f"Cédulas de 200: {ced200}\nCédulas de 100: {ced100}\nCédulas de 50: {ced50}\nCédulas de 20: {ced20}\nCédulas de 10: {ced10}\nCédulas de 5: {ced5}\nCédulas de 2: {ced2}\nTroco: {troco}"

valor_pago = int(input("Digite o valor pago: "))
valor_conta = int(input("Digite o valor da conta: "))
resultado = calculo_troco(valor_pago, valor_conta)
print()
print(resultado)