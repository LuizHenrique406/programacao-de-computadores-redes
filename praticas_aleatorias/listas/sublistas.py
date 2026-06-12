idades = [54,65,769,5,234,54,76,23,43]
a = idades[1:5] # do índice 1 ao 5(4)
b = idades[::2] # pula de 2 em 2
c = idades[::-1] # inverte a lista
d = idades[:5:2] # respectivamente, (início)começa do 0, (fim)para antes do índice 5 e (passo)pula de 2 em 2
print(f"{a}\n{b}\n{c}\n{d}")