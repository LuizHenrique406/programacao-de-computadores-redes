print("Esse programa calcula a soma dos múltiplos de 3 e 5")

num1 = 3
num2 = 5
x = 3
soma_total = 0  

while x < 1000:
    if x % num1 == 0 or x % num2 == 0:
        soma_total = x + soma_total
        x = x + 1
    else:
        x = x + 1

print("A soma dos múltiplos são", soma_total)
