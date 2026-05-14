import random 

print("Seu objetivo é acertar a palavra sorteada")
palavras = [ "ARARA", "TURMA", "LIMÃO", "ABACAXI"]
sorteada = palavras[random.randint(0,3)]
digitada = "_" * len(sorteada)

tentativas = 0

while tentativas < 5:

    print(digitada)
    letra = input("Digite uma letra: ")
    
    for pos in range(len(sorteada)):
        if sorteada[pos] == letra:
            digitada = digitada[:pos] + letra + digitada[pos+1:]

    tentativas = tentativas + 1

    if sorteada == digitada:
        break

if digitada == sorteada:
    print("Acertou!!! a palavra é", digitada)
else:
    print("Errou!!! a palavra era", sorteada)
