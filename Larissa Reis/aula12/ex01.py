estoque = [
    
]

def adicionar_produto():
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    estoque.append([produto, quantidade, preco])
    print(f"Produto {produto} adicionado com sucesso!")

def remover_produto():
    produto = input("Digite o nome do produto a ser removido: ")
    for item in estoque:
        if item[0] == produto:
            estoque.pop(estoque.index(item))
            print(f"Produto {produto} removido com sucesso!")
            return
    print(f"Produto {produto} não encontrado no estoque.")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
        return
    print("Produtos no estoque:")
    for item in estoque:
        print(f"Produto: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]}")

def total_estoque():
    total = 0
    for item in estoque:
        total += item[1] * item[2]
    print(f"Valor total do estoque: R$ {total:.2f}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Calcular valor total do estoque")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            total_estoque()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()