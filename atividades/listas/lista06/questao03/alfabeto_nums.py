nomes = [
    "ALESSANDRA", "BERNARDO", "CLEMENTINA", "DOMINGOS", "ESMERALDA",
    "FRANCISCO", "GABRIELLE", "HENRIQUETA", "ISADORA", "JEREMIAS",
    "KATARINA", "LEONARDO", "MARIANA", "NICOLAU", "OLÍMPIA",
    "PENÉLOPE", "QUINTILHA", "RAFAELLY", "SANDRINO", "TEODORO",
    "VALENTINA", "WILSON", "XIMENA", "YASMIN", "ZACHARY",
    "ALBERTO", "BÁRBARA", "CRISTIANO", "DIAMANTINA", "EMANUELLE",
    "FERNANDA", "GUILHERME", "HELENA", "IGOR", "JULIANNA",
    "KLEBER", "LUCIANA", "MAXIMILIANO", "NATÁLIA", "OTÁVIO",
    "PATRÍCIA", "QUELÉRIA", "RODRIGO", "SILVANA", "THIAGO",
    "URBANO", "VICTÓRIA", "WANDERLEY", "XAVIER", "YASMIM"
]
alfabeto = {
    "A":1, "B":2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, 
    "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
    "R": 18, "S": 19, "T": 20, "U,": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
    "Z": 26
            }
nomes_valores = {}
for i in nomes:
    soma = 0
    for e in i:
        if e in alfabeto:
            soma += alfabeto[e]
            nomes_valores[i] = soma
nomes_organi = nomes_valores.items()
nomes_orden = sorted(nomes_organi, key = lambda x:x[1])
print(nomes_orden[32])