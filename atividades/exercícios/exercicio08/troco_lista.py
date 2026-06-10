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
print(f"Cédula de 200: {quant[0]}\nCédula de 100: {quant[1]}\nCédula de 50: {quant[2]}\nCédula de 20: {quant[3]}\nCédula de 10: {quant[4]}\nCédula de 5: {quant[5]}\nCédula de 2: {quant[6]}\nmoedas: {quant[7]}")