print("Esse programa a diferença entre a soma dos quadrados dos primeiros cem números naturais e o quadrado da soma")

soma100 = 0
sq = 0
for n in range(1,101):
    soma100 = soma100 + n
qs = soma100 ** 2

for n in range(1,101):
    sq = sq + n ** 2

print(qs - sq)