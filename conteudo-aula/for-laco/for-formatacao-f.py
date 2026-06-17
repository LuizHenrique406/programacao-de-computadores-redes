for i in range(11):                     # o i vai passar a ser o 0 na primeira chamada    
  print(f"Tabuada do {i}")              # aqui vai imprimir "Tabuada do" e entre essas chaves o valor do na hora
  for j in range(11):                   # aqui o j vai passear do 0 até o 10, quando chegar em 10, volta pro i e adiciona mais um valor a ele, ex.: era 1 antes, depois do j passa a ser 2 e assim vai, até chegar no 10.
      print(f"{i} * {j}: {i*j}")        # aqui vai imprimir a multiplicação do i com o j, esse "f" mostra o valor da variável que está enter as chave