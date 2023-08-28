tarefa_pendente = []

while True:
    print('DIGITE O QUE FAZER:')
    print('\n1. Adicionar Tarefa')
    print('2. Processar Tarefas')
    print('3. Sair')
    escolha = input("Digite o número da sua opção desejada: ")
    
    if escolha == "1":
        tarefa = input("Digite a tarefa: ")
        tarefa_pendente.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à pilha.")
    elif escolha == "2":
        if tarefa_pendente:
            tarefa = tarefa_pendente.pop()
            print(f"Executando tarefa: '{tarefa}'")
        else:
            print("A pilha de tarefas está vazia.")
    elif escolha == "3":
        print("Finalizando o programa.")
        break
    else:
        print("INVÁLIDO. Escolha novamente.")
