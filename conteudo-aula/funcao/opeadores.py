b = int(input("num1: "))
a = int(input("num2: "))
def soma(a,b):
    result = a + b
    return result
print(soma(a,b))
c = int(input("num3: "))
def multi(c):
    result = c * soma(a,b)
    return result
print(multi(c))