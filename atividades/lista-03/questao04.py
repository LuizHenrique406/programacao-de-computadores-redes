print("Esse programa classifica indereços IPs")
print()
print("Digite números inteiros de 0 a 255")
num1 = int(input("Digite o primeito número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

if num1 < 0 or num2 < 0 or num3 < 0 or num4 < 0:
    print("Erro! Número não pode ser negativo")
else:
    if num1 < 255 and num2 < 255 and num3 < 255 and num4 < 255:
        if num1 + num2 + num3 + num4 == 0:
            print("Endereço Default de Rede")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 == 10:
            print("Endereço Reservado Classe A")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 == 127:
            print("Endereço de Loopback")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 == 169 and num2 == 254:
            print("Endereço de APIPA")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 == 192 and num2 == 168:
            print("Endereço Reservado Classe C")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 + num2 + num3 + num4 == 1.020:
            print("Endereço de Broadcast")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 == 1 or num1 <= 126:
            print("Endereço Classe A")
            print(num1,".", num2,".", num3,".",num4)
        if num1 >= 128 and num1 <= 191:
            print("Endereço Classe B")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 >= 192 and num1 <= 223:
            print("Endereço Classe C")
            print(num1, ".", num2, ".", num3, ".", num4)
        if num1 >= 224 and num1 <= 239:
            print("Emdereço de Multicast")
            print(num1, ".", num2, ".", num3, ".", num4)
    else:
        print("Digite um número inteiro maior que 1 e igual ou menor que 255!!!")