# Listas
## São agregadas de vários elementos armazenados num variável

### Criação de lista:
- l = [5, 3, 4.2, 9]
### Adição de elementos na lista
- l.append (12)
- print(l) = [5, 3, 4.2, 9, 12]
### Atualização de elemento da lista
- posições dos elementos = 0, 1... -> índice
- l[2] = 3.5 = [5, 3, 3.5, 9, 12]
### Uso de índices:
x = 3
- l[x] = 17 -> l[5, 3, 3.5, 17, 12]
- l[x + 1] = 14 -> l[5, 4, 3.5, 17, 14]
- l[x] = l[x - 1] -> l[3] = 3.5 -> l[5, 3, 3.5, 3.5, 14]
- l[x] = l[x - 1] + l[x + 1] -> l[3] = l[2] + l[4] -> l[3] = 17.5 -> l[5, 3, 3.5, 17.5, 14]
### Acesso a todos os elementos:
#### Usado para saber os elementos da lista:
- for x in l:
-    print(x)
- 5
- 3
- 3.5
- 17.5
- 14
#### Usado para saber os elementos e as posições desses elementos:
- for i in range (len(l)):
-    print(i, l[i])
- 0 5
- 1 3
- 2 3.5
- 3 17.5
- 4 14