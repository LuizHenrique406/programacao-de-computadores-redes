print("Esse programa calcula os números de Collatz")

num = int(input("Digite um número inteiro: "))

veri_termos = 1
termo5 = 0

while num >= 2:

    if num % 2 == 0:
        num = num // 2
        veri_termos = veri_termos + 1
    else:
        num = 3 * num + 1
        veri_termos = veri_termos + 1

    if veri_termos == 5:
        termo5 = num
        
if termo5 == True:
    print("Esse número tem", veri_termos, "de sequência", "e seu 5° termo é", termo5)
else:
    print("Esse número tem", veri_termos, "de sequência")