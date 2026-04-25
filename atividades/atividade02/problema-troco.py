print("esse programa calcula as cédulas de um troco")

valor_pago = int(input("Qual o valor pago?: "))
valor_conta = int(input("Qual o valor da conta?: "))

troco = valor_pago - valor_conta
print("O valor do troco é: ", troco)

ced200 = troco // 200
print("#ced200: ", ced200)
troco = troco % 200

ced200 = troco // 100
print("#ced100: ", ced200)
troco = troco % 100

ced200 = troco // 2
print("#ced2: ", ced200)
troco = troco % 2
print("#moedas1: ", troco)
