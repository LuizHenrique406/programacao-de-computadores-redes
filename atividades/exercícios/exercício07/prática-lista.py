str_uf        = 'Alagoas;Bahia;Ceará;Maranhão;Paraíba;Pernambuco;Piauí;Rio Grande do Norte;Sergipe'
str_siglas    = 'AL;BA;CE;MA;PB;PE;PI;RN;SE'
str_populacao = '3365351;14985284;9240580;7153262;4059905;9674793;3289290;3560903;2338474'

str_uf = str_uf.split(";")
str_siglas = str_siglas.split(";")
str_populacao2 = str_populacao.split(";")

uf = 0
siglas = 0
populacao = []

for i in str_populacao2:
    x = int(i)
    populacao.append(x)

max = 0
pos = 0

for i in range(len(populacao)):
    if i > max:
        max = populacao[i]
        pos = i

for i in range(len(str_uf)):
    if i == pos:
        uf = str_uf[i]

for i in range(len(str_siglas)):
    if i == pos:
        siglas = str_siglas[i]

print(f"O estado que possui maior população é {uf} com a sigla {siglas}, com populaão de {max}")