print("Esse programa calcula a sua Capuitalização Acumulada")

capital = float(input("Digite o seu capital: "))
taxa_fixa = float(input("Digite o seu juros: "))
tempo = int(input("Digite o tempo em anos: "))
taxa_fixa = taxa_fixa / 100

montante = capital * ((1 + taxa_fixa / 100)**tempo)

print("Montante: R$", montante)