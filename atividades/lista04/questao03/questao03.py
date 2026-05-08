# receber um número
# depois verificar se ele é ímpar ou par
# se ele for par, divide por 2
# se ele for ímpar, multiplica por 3 e soma + 1
# daí pega o resultado da primeira verificação e faz tudo de novo
# toda vez que ele for dividindo, aumenta + 1 na contagem de termos
# e no quinto termo, se tiver, guarda esse valor e imprime ele no final do código
# par = num / 2
# impar = 3 * num + 1


print("Esse programa calcula os números de Collatz")

num = int(input("Digite um número inteiro: "))

veri_termos = 1
termo5 = 0

while num >= 2:

    if num % 2 == 0:
        num = num // 2
        veri_termos = veri_termos + 1
        print(num)
    else:
        num = 3 * num + 1
        veri_termos = veri_termos + 1
        print(num)

    if veri_termos == 5:
        termo5 = num

print("Esse número tem", veri_termos, "de sequência", "e seu 5° termo é", termo5)