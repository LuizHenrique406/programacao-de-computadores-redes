# 20261014050035 - LUIZ HENRIQUE TEIXEIRA E SILVA
# 20261014050009 - VINÍCIUS GOMES ALVES

#- U (cima); 
#- D (baixo); 
#- R (direita);
#- L (esquerda); 
#- O (noroeste/cima-esquerda); 
#- N (nordeste/cima-direita); 
#- E (sudeste/baixo-direita);  
#- W (sudoeste/baixo-esquerda)

validos = 0

x = int(input("Informe a posição em X:"))
y = int(input("Informe a posição em Y:"))

comando = input("Qual o seu comando? ")

for m in comando.upper():
    
    if "U" in m:
        y = y + 1
        validos = validos + 1

    elif "D" in m:
        y = y - 1
        validos = validos + 1
    
    elif "R" in m:
        x = x + 1
        validos = validos + 1

    elif "L" in m:
        x = x - 1
        validos = validos + 1

    elif "O" in m:
        y = y + 1
        x = x - 1
        validos = validos + 1

    elif "N" in m:
        y = y + 1
        x = x + 1
        validos = validos + 1

    elif "E" in m:
        y = y - 1
        x = x + 1
        validos = validos + 1
    
    elif "W" in m:
        y = y - 1
        x = x + 1
        validos = validos + 1  

print(f"Posição final:{x}, {y}")
print(f"Movimentos válidos: {validos}") 