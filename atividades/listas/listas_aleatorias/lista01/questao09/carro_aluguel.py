km_percorrido = float(input("Digite quantos quilômetros o carro rodou: "))
dias_usado = int(input("Quantos dias o carro ficou alugado: "))
total = (km_percorrido * (15 / 100)) + (dias_usado * 60)
print(f"Você irá pagar {total:.2f}R$")