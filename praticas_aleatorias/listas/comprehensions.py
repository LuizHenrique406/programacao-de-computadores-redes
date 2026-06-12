a = [i for i in range(1,11) if i % 2 == 1]
b = [i for i in range(1,11) if i % 2 == 0]
print(f"Apenas ímapres menosres que 10: {a}\nApenas pares menores que 10: {b}")
# isso aqui é de boa, piora quando é comparação ou fazer a partir de outra lista :(
S = [ x**2 for x in range(20) ]
K = [ x//1024 for x in S if x % 1024 == 0]
print(f"{K}")
# tipo essa aqui, mas essa aqui também tá de boa, deve ter outras piores