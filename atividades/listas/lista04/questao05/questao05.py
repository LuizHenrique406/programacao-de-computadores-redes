# perguntar ao usuário qual será a posição inicial do robô
# depois perguntar uma string, que é com ela que o robô vai andar
# depois definir as string com seus respectivos movimentos
# depois fazer o plano cartesiano de alguma forma aí
# no final, indicar a posição final do robô e quantos movimentos válidos ele fez(fazer um for com pos para verificação)
# validar letras maiúsculas e minúsculas, e ignorar aquelas que não forem estabelecidas

U = 1
D = -1
R = 1
L = -1
O = -1
N = 1
E = -1
W = 1

print("Esse programa simula os movimentos de um robô")
print("Os movimentos são: \nU, D, R, L\nO, N, E, W")
pos_inicial = str(input("Digite uma posição inicial para o robô: "))
x = 0
y = 0
movimentos1 = 0
movimentos2 = 0

while movimento1 != "1":

    print("Digite 1 para sair")
    print("Os movimentos são: \nU, D, R, L\nO, N, E, W")
    movimento1 = str(input("Digite os movimentos: "))
    movimento2 = str(input("Digite os movimentos: "))
    
    
