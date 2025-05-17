registro = [
    
]

def adicionar_reserva():
    nome = input("Digite o nome do hóspede: ")
    quarto = int(input("Digite o número do quarto: "))
    diaria = float(input("Digite a quantidade de dias desejados: "))
    registro.append([nome, quarto, diaria])
    print(f"Reserva em nome de {nome} adicionada com sucesso!")

def remover_reserva():
    nome = input("Digite o nome da reserva a ser removida: ")
    for item in registro:
        if item[0] == nome:
            registro.pop(registro.index(item))
            print(f"Reserva em nome de {nome} removida com sucesso!")
            return
    print(f"Reserva em nome de {nome} não encontrado no registro.")

def listar_reservas():
    if not registro:
        print("Registro não encontrado.")
        return
    print("Reservas registradas:")
    for item in registro:
        print(f"Hóspede: {item[0]}, Quarto: {item[1]}, Diárias: {item[2]}")

def receita_total():
    total = 0
    for item in registro:
        total += 150 * item[2]
    print(f"Receita total do hotel: R$ {total:.2f}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar reserva")
        print("2. Remover reserva")
        print("3. Listar reservas")
        print("4. Calcular receita total")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_reserva()
        elif opcao == "2":
            remover_reserva()
        elif opcao == "3":
            listar_reservas()
        elif opcao == "4":
            receita_total()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()