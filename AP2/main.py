# Gerenciador de Tarefas Diárias

tarefas = []
concluidas = []

def adicionar_tarefa():
    try:
        tarefa = input("Digite a tarefa a ser adicionada: ").upper()
        while True:
            try:
                relevancia = int(input("Digite a relevância da tarefa (1 - 5): "))
                if 1 <= relevancia <= 5:
                    break
                else:
                    print("Relevância inválida. Por favor, insira um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para relevância.")
                return
        tempo_estimado = int(input("Digite o tempo estimado para a tarefa (em minutos): "))
        tarefas.append([tarefa, relevancia, tempo_estimado])
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para relevância e tempo estimado.")
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def editar_tarefa():
    try:
        tarefa = input("Digite o nome da tarefa a ser editada: ").upper()
        for t in tarefas:
            if t[0] == tarefa:
                try:
                    tarefa_item = input("Digite o item a ser editado (nome/relevancia/tempo): ").lower()
                    if tarefa_item == "nome":
                        novo_nome = input("Digite o novo nome da tarefa: ").upper()
                        t[0] = novo_nome
                    elif tarefa_item == "relevancia":
                        nova_relevancia = int(input("Digite a nova relevância (1 - 5): "))
                        t[1] = nova_relevancia
                    elif tarefa_item == "tempo":
                        novo_tempo = int(input("Digite o novo tempo estimado (em minutos): "))
                        t[2] = novo_tempo
                    else:
                        print("Item inválido. Tente novamente.")
                        return
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")
                    return
                print(f"Tarefa '{tarefa}' editada com sucesso!")
                return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

def remover_tarefa():
    try:
        tarefa = input("Digite o nome da tarefa a ser removida: ").upper()
        for i, t in enumerate(tarefas):
            if t[0] == tarefa:
                tarefas.pop(i)
                print(f"Tarefa '{tarefa}' removida com sucesso!")
                return
        print(f"Tarefa '{tarefa}' não encontrada.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

def concluir_tarefa():
    try:
        tarefa = input("Digite o nome da tarefa a ser concluída: ").upper()
        for i, t in enumerate(tarefas):
            if t[0] == tarefa:
                tarefa_removida = tarefas.pop(i)
                concluidas.append(tarefa_removida)
                print(f"Tarefa '{tarefa}' concluída com sucesso!")
                return
        print(f"Tarefa '{tarefa}' não encontrada.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

def exibir_tarefas():
    try:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        opcao = int(input("Deseja ver as tarefas pendentes(1) ou concluídas(2)? "))
        if opcao == 1:
            print("\nTarefas Pendentes:")
            for t in tarefas:
                print(f"Tarefa: {t[0]}, Relevância: {t[1]}, Tempo Estimado: {t[2]} minutos")
        elif opcao == 2:
            print("\nTarefas Concluídas:")
            for t in concluidas:
                print(f"Tarefa: {t[0]}, Relevância: {t[1]}, Tempo Estimado: {t[2]} minutos")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

def menu():
    while True:
        try:
            print("\nMenu:\n1. Adicionar Tarefa\n2. Editar Tarefa\n3. Remover Tarefa\n4. Concluir Tarefa\n5. Exibir Tarefas\n6. Sair")
            opcao = int(input("\nEscolha uma opção: "))
            
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
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

if __name__ == "__main__":
    menu()