reservas = [
    
]

def exibir_reservas():
    print("\nReservas atuais:")
    for reserva in reservas:
        print(f"{reserva[0]} - Quarto: {reserva[1]} - Dias: {reserva[2]} - Preço por dia: R${reserva[3]:.2f} - Total: R${reserva[2] * reserva[3]:.2f}")

def adicionar_reserva():
    try:
        nome = input("\nDigite o nome do cliente: ")
        quarto = input("Digite o número do quarto: ")
        quantidade = int(input("Digite a quantidade de dias: "))
        preco = float(input("Digite o preço por dia: "))
        reservas.append([nome.upper(), quarto, quantidade, preco])
        print(f"\nReserva para {nome} adicionada com sucesso!")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um número.")
        return

def remover_reserva():
    nome = input("\nDigite o nome do cliente a ser removido: ")
    for reserva in reservas:
        if reserva[0] == nome.upper():
            reservas.pop(reservas.index(reserva))
            print(f"\nReserva para {nome} removida com sucesso!")
            return
    print(f"\nReserva para {nome} não encontrada.")

def atualizar_reserva():
    try:
        nome = input("\nDigite o nome do cliente a ser atualizado: ")
        for reserva in reservas:
            if reserva[0] == nome.upper():
                novo_nome = input("Digite o novo nome do cliente: ")
                novo_quarto = input("Digite o novo número do quarto: ")
                nova_quantidade = int(input("Digite a nova quantidade de dias: "))
                novo_preco = float(input("Digite o novo preço por dia: "))
                reserva[0] = novo_nome.upper()
                reserva[1] = novo_quarto
                reserva[2] = nova_quantidade
                reserva[3] = novo_preco
                print(f"Reserva para {nome} atualizada com sucesso!")
                return
            else:
                print(f"\nReserva para {nome} não encontrada.")
    except ValueError:
        print("\nEntrada inválida. Por favor, insira um número.")
        return

def valor_total_reserva():
    total = 0
    for reserva in reservas:
        total += reserva[2] * reserva[3]
    print(f"\nValor total das reservas: R${total:.2f}")

def menu():
    while True:
        try:
            print("\nMenu:")
            print("1. Exibir reservas")
            print("2. Adicionar reserva")
            print("3. Remover reserva")
            print("4. Atualizar reserva")
            print("5. Calcular valor total das reservas")
            print("6. Sair")
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                exibir_reservas()
            elif opcao == 2:
                adicionar_reserva()
            elif opcao == 3:
                remover_reserva()
            elif opcao == 4:
                atualizar_reserva()
            elif opcao == 5:
                valor_total_reserva()
            elif opcao == 6:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    menu()