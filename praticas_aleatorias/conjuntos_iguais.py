a = list(input("Digite alguns números: "))
b = list(input("Digite alguns números novamente: "))
iguais = True
if len(a) != len(b):
    print("Esses conjuntos não são iguais!!!")
    exit()
else:
    for i in range(len(a)):
        encontrou = False
        for j in range(len(b)):
            if i == j:
                encontrou = True
                break
        if not encontrou:
            iguais = False
            break
    if iguais:
        print("Esse conjuntos são iguais!!!")
    else:
        print("Esses conjuntos não são iguais!!!")