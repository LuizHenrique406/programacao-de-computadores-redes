str_uf        = 'Alagoas;Bahia;Ceará;Maranhão;Paraíba;Pernambuco;Piauí;Rio Grande do Norte;Sergipe'
str_siglas    = 'AL;BA;CE;MA;PB;PE;PI;RN;SE'
str_populacao = '3365351;14985284;9240580;7153262;4059905;9674793;3289290;3560903;2338474'

str_uf = str_uf.split("; ")
str_siglas = str_siglas.split("; ")
str_populacao = str_populacao.split("; ")

max = 0

for i in range(len(str_populacao) - 1):
    if str_populacao[i] > str_populacao[i + 1]:
        max = str_populacao[i]
    else:
        max = str_populacao[i + 1]
print(str_populacao)
print(max)