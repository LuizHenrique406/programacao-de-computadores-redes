valor_conta = float(input("Digite o valor da conta: "))
valor_pago =  float(input("Digite o valor pago: "))
troco = valor_pago - valor_conta
cedulas = [200, 100, 50, 20, 10, 5, 2]
quant = []
for i in cedulas:
    x = troco // i
    quant.append(x)
    troco = troco % i
quant.append(troco)
print(quant)