def soma(a, b):
    result = a + b
    return result
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
print(soma(a,b))

c = int(input("Digite um valor: "))
def multi(c):
    result = c * soma(a,b)
    return result
print(multi(c))

d = int(input("Digite um valor: "))
def div(d):
    result = d / (soma(a,b) + multi(c))
    return result
print(div(d))