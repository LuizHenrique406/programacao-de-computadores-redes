usuario1 = int(input("Digite um valor: "))

num_invertido = 0
usuario2 = usuario1

while usuario2 > 0: 
    usuario2 = usuario1

    while usuario2 > 0 :
        num_invertido = num_invertido * 10 + (usuario2 % 10)
        usuario2 = usuario2 // 10
        
if num_invertido == usuario1:
    print("Esse número é um polídromo!!!")
else:
    print("Esse número não é um polídromo!!!")