print("Esse programa calcula a quantidade de cédula ou moedas em um troco de restaurante")

valor_pago = int(input("Digite o valor pago: "))
valor_conta = int(input("Diigite o valor da conta: "))

troco = valor_pago - valor_conta
print("O troco é: ", troco)

ced200 = troco // 200
print("O número da quantidade de cédulas de R$ 200 foi:", ced200)
troco = troco % 200

ced100 = troco // 100
print("O número da quantidade de cédulas de R$ 100 foi:", ced100)
troco = troco % 100

ced50 = troco // 50
print("O número da quantidade de cédulas de R$ 50 foi:", ced50)
troco = troco % 50

ced20 = troco // 20
print("O número da quantidade de cédulas de R$ 20 foi:", ced20)
troco = troco % 20

ced10 = troco // 10
print("O número da quantidade de cédulas de R$ 10 foi:", ced10)
troco = troco % 10

ced5 = troco // 5
print("O número da quantidade de cédulas de R$ 5 foi:", ced5)
troco = troco % 5

ced2 = troco // 2
print("O número da quantidade de cédulas de R$ 2 foi:", ced2)
troco = troco % 2
print("O troco é: ", troco)
