print("Esse programa simula um pagamento")

conta = float(input("Digite o valor da conta: "))
pago = int(input("Digite o valor a ser dado: "))

troco = pago - conta

ced200 = troco // 200
print(f"Cédulas de 200: {ced200}")
troco = troco % 200

ced100 = troco // 100
print(f"Cédulas de 100: {ced100}")
troco = troco % 100

ced50 = troco // 50
print(f"Cédulas de 50: {ced50}")
troco = troco % 50

ced20 = troco // 20
print(f"Cédulas de 20: {ced20}")
troco = troco % 20

ced10 = troco // 10
print(f"Cédulas de 10: {ced10}")
troco = troco % 10

ced5 = troco // 5
print(f"Cédulas de 5: {ced5}")
troco = troco % 5

ced2 = troco // 2
print(f"Cédulas de 2: {ced2}")
troco = troco % 2
print(f"Moedas: {troco}")