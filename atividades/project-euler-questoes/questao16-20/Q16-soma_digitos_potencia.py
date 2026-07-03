print("Esse programa soma os digitos de uma potência")
def soma_digi_pote(a, b):
    pote = a ** b
    pote_str = str(pote)
    soma = 0
    for i in pote_str:
        soma += int(i)
    return soma
num = int(input("Digite um numero: "))
potencia = int(input("Agora digite a potência desse número: "))
print(soma_digi_pote(num, potencia))