import random 

print("Seu objetivo é acertar a palavra sorteada")
palavras = [ "ARARA", "TURMA", "LIMÃO", "ABACAXI"]
sorteada = palavras[random.randint(0,3)]
digitada = "_" * len(sorteada)

while digitada != sorteada:
    print(digitada)
    letra = input("Digite uma letra: ")
    for pos in range(len(sorteada)):
        if sorteada[pos] == letra:
            digitada = digitada[:pos] + letra + digitada[pos+1]
