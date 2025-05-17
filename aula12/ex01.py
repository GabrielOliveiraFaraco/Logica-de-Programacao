estoque = [

]

def exibir_estoque():
    print("\nEstoque atual:")
    for produto in estoque:
        print(f"{produto[0]} - Quantidade: {produto[1]} - Preço: R${produto[2]:.2f}")

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    estoque.append([nome.upper(), quantidade, preco])
    print(f"\nProduto {nome} adicionado com sucesso!")

def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ")
    for produto in estoque:
        if produto[0] == nome.upper():
            estoque.pop(estoque.index(produto))
            print(f"\nProduto {nome} removido com sucesso!")
            return
    print(f"\nProduto {nome} não encontrado no estoque.")

def atualizar_produto():
    try:
        posicao = input("Digite o nome do produto a ser atualizado: ")
        for produto in estoque:
            if produto[0] == posicao:
                novo_nome = input("Digite o novo nome do produto: ")
                nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                novo_preco = float(input("Digite o novo preço do produto: "))
                produto[0] = novo_nome.upper()
                produto[1] = nova_quantidade
                produto[2] = novo_preco
                print(f"Produto {posicao} atualizado com sucesso!")
                return
            else:
                print(f"\nProduto {posicao} não encontrado no estoque.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

def valor_total_estoque():
    total = 0
    for produto in estoque:
        total += produto[1] * produto[2]
    print(f"\nValor total do estoque: R${total:.2f}")

def menu():
    while True:
        try:
            print("\nMenu:")
            print("1. Exibir estoque")
            print("2. Adicionar produto")
            print("3. Remover produto")
            print("4. Atualizar produto")
            print("5. Calcular valor total do estoque")
            print("6. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                exibir_estoque()
            elif opcao == "2":
                adicionar_produto()
            elif opcao == "3":
                remover_produto()
            elif opcao == "4":
                atualizar_produto()
            elif opcao == "5":
                valor_total_estoque()
            elif opcao == "6":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    menu()