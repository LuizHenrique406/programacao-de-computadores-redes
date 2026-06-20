def dobrar(num):
    resultado = num * 2
    return resultado
valor = int(input("Digite um valor: "))
print(dobrar(valor))

def saudacao(texto):
    resultado = "Eae " + texto + ", Suave?"
    return resultado
nome = input("Digite seu nome: ")
print(saudacao(nome))

def dividir_conta(valor_total, qtd_amigos):
    resultado = valor_total / qtd_amigos
    return resultado
conta = float(input("Qual o valor da sua conta?: "))
amigos = int(input("Quantos amigos você tem aí?: "))
print(f"{dividir_conta(conta, amigos): .2f}")