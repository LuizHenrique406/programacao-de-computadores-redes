opcao = 0
paciente = []
while opcao != 4:
    print("1. Registrar chegada de paciente")
    print("2. Atender paciente")
    print("3. Registrar desistência de paciente")
    print("4.Sair")
    opcao = int(input("Digite a sua opcão: "))
    if opcao == 1:
        if len(paciente) == 10:
            print("A fila esta cheia!!!")
            print()
        else:
            nome = str(input("Digite o seu nome: "))
            if nome in paciente:
                print("Digite outro nome!!!")
            else:
                paciente.append(nome)
                print(paciente)
    if opcao == 2:
        print("Paciente atendido!!!")
        paciente.pop(0)
        print(paciente)
    if opcao == 3:
        nome = str(input("Digite o seu nome: "))
        #if nome in paciente:
            #paciente.remove(nome) pode ser assim tbm, mas é melhor a parte difícil
        for i in range(len(paciente)):
            if nome == paciente[i]:
                paciente.remove(nome)
                print("Paciente removido!!!")
                break
            print(paciente)
        else:
            print("Nome não encontrado!!!")
print("Clínica fechada!!!")