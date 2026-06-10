print("Esse programa indica qual é o tipo do triângulo a partir do números de lados")

a = int(input("Qual o valor do lado a?: "))
b = int(input("Qual o valor do lado b?: "))
c = int(input("Qual o valor do lado c?: "))

if a == b and b == c and c == a:
    print("Esse triãngulo é Equilátero")

if (a == b or b == c or c == a or c == b) and (a != b or b != c or c != b or c != a):
    print("Esse triângulo é Isósceles")

if a != b and b != c and c != a:
    print("Esse triângulo é Escaleno")