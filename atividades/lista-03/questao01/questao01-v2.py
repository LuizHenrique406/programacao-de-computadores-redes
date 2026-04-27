import random

print("Esse programa simula um jogo de adivinhação")

num_sorte = random.randint(1,100)
num_usuario = int(input("Digite um número: "))

minimo = 0
maximo = 100
tentativa = 1

while tentativa < 5:
    if num_usuario == num_sorte:
        print("Acertou!")
    if num_usuario != num_sorte:
        if num_usuario > num_sorte:
            maximo = num_usuario
        if num_usuario < num_sorte:
            minimo = num_usuario
        print("Errado! Tente Novamente! O número está entre", maximo, "e", minimo)
        # tentativa 2
        num_usuario = int(input("Digite outro número: "))
        tentativa = tentativa + 1
print("As tentativas acabaram!!! Reinicie o programa!!!")
print()
print("O número sorteado era", num_sorte)