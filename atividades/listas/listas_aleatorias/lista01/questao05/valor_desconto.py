valor = float(input("Digite o valor da mercadoria: "))
desconto = int(input("Digite o valor do desconto: "))
desconto = desconto / 100
valor_desconto = valor * desconto
valor_final = valor - valor_desconto
print(f"Total a pagar: {valor_final:.2f}R$\nValor total do desconto: {valor_desconto:.2f}R$")