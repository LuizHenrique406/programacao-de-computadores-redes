import random

print("Esse programa simula um jogo de adivinhação")

num_sorte = random.randint(1,100)
num_usuario = int(input("Tentativa 1! Digite um número: "))

minimo = 0
maximo = 100

# tentativa 1
if num_usuario == num_sorte:
    print("Acertou de primeira! Bela intuição!")
if num_usuario != num_sorte:
    if num_usuario > num_sorte:
        maximo = num_usuario
    if num_usuario < num_sorte:
        minimo = num_usuario
    print("Errado! Tente Novamente! O número está entre", maximo, "e", minimo)
    # tentativa 2
    num_usuario = int(input("2° Tentativa! Digite outro número: "))
    if num_usuario == num_sorte:
        print("Acertou na 2° tentativa! Bom jogo!")
    if num_usuario != num_sorte:
        if num_usuario > num_sorte:
            maximo = num_usuario
        if num_usuario < num_sorte:
            minimo = num_usuario
        print("Errado novamente! Tente De novo! O número está entre", maximo, "e",minimo)
        # 3 tentativa
        num_usuario = int(input("3° Tentativa! Digite outro númeoro: "))
        if num_usuario == num_sorte:
            print("Acertou! Quase que não vai, hein? :)")
        if num_usuario != num_sorte:
            if num_usuario > num_sorte:
                maximo = num_usuario
            if num_usuario < num_sorte:
                minimo = num_usuario
            print("Erraro Novamente! Tente De Novo! O número está entre", maximo, "e", minimo)
            # 4 tentativa
            num_usuario = int(input("4° e Última Tentativa! Digite Outro Número: "))
            if num_usuario == num_sorte:
                print("Acertou na última, hein? Grande sorte!")
            if num_usuario != num_sorte:
                print("Errado! Fim de Jogo! O número era", num_sorte)

