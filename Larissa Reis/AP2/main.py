# Gerenciador de Tarefas Diárias Simplificado

tarefas = []
concluidas = []

def adicionar_tarefa():
    nome = input("Digite a tarefa a ser adicionada: ").upper()
    try:
        relevancia = int(input("Digite a relevância da tarefa (1 - 5): "))
        if relevancia < 1 or relevancia > 5:
            print("Relevância deve ser entre 1 e 5.")
            return
    except ValueError:
        print("Relevância inválida.")
        return
    try:
        tempo = int(input("Digite o tempo estimado para a tarefa (em minutos): "))
        if tempo < 1:
            print("Tempo deve ser maior que zero.")
            return
    except ValueError:
        print("Tempo inválido.")
        return
    tarefas.append([nome, relevancia, tempo])
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def editar_tarefa():
    nome_busca = input("Digite o nome da tarefa: ").upper()
    idx = None
    for i, t in enumerate(tarefas):
        if t[0] == nome_busca:
            idx = i
            break
    if idx is None:
        print("Tarefa não encontrada.")
        return
    campo = input("Digite o item a ser editado (nome/relevancia/tempo): ").lower()
    if campo == "nome":
        novo_nome = input("Digite o novo nome da tarefa: ").upper()
        tarefas[idx][0] = novo_nome
    elif campo == "relevancia":
        try:
            nova_relevancia = int(input("Digite a nova relevância (1 - 5): "))
            if nova_relevancia < 1 or nova_relevancia > 5:
                print("Relevância deve ser entre 1 e 5.")
                return
            tarefas[idx][1] = nova_relevancia
        except ValueError:
            print("Relevância inválida.")
            return
    elif campo == "tempo":
        try:
            novo_tempo = int(input("Digite o novo tempo estimado (em minutos): "))
            if novo_tempo < 1:
                print("Tempo deve ser maior que zero.")
                return
            tarefas[idx][2] = novo_tempo
        except ValueError:
            print("Tempo inválido.")
            return
    else:
        print("Item inválido. Tente novamente.")
        return
    print("Tarefa editada com sucesso!")

def remover_tarefa():
    nome_busca = input("Digite o nome da tarefa: ").upper()
    idx = None
    for i, t in enumerate(tarefas):
        if t[0] == nome_busca:
            idx = i
            break
    if idx is not None:
        nome = tarefas[idx][0]
        tarefas.pop(idx)
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print("Tarefa não encontrada.")

def concluir_tarefa():
    nome_busca = input("Digite o nome da tarefa: ").upper()
    idx = None
    for i, t in enumerate(tarefas):
        if t[0] == nome_busca:
            idx = i
            break
    if idx is not None:
        nome = tarefas[idx][0]
        concluidas.append(tarefas.pop(idx))
        print(f"Tarefa '{nome}' concluída com sucesso!")
    else:
        print("Tarefa não encontrada.")

def exibir_tarefas():
    if not tarefas and not concluidas:
        print("Nenhuma tarefa cadastrada.")
        return
    try:
        ver = int(input("Deseja ver as tarefas pendentes(1) ou concluídas(2)? "))
    except ValueError:
        print("Opção inválida.")
        return
    if ver == 1:
        lista = tarefas
        titulo = "Pendentes"
    elif ver == 2:
        lista = concluidas
        titulo = "Concluídas"
    else:
        print("Opção inválida.")
        return
    if not lista:
        print(f"Nenhuma tarefa {titulo.lower()}.")
        return
    print(f"\nTarefas {titulo}:")
    for t in lista:
        print(f"Tarefa: {t[0]}, Relevância: {t[1]}, Tempo Estimado: {t[2]} minutos")

def sair():
    print("Saindo...")

while True:
    print("\nMenu:")
    print("1. Adicionar Tarefa")
    print("2. Editar Tarefa")
    print("3. Remover Tarefa")
    print("4. Concluir Tarefa")
    print("5. Exibir Tarefas")
    print("6. Sair")
    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número de 1 a 6.")
        continue

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        editar_tarefa()
    elif opcao == 3:
        remover_tarefa()
    elif opcao == 4:
        concluir_tarefa()
    elif opcao == 5:
        exibir_tarefas()
    elif opcao == 6:
        sair()
        break
    else:
        print("Opção inválida. Digite um número de 1 a 6.")