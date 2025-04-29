estoque = 100
venda = 0
reposicao = 0

def vendas():
    total_vendas = 0
    while True:
        try:
            quantidade = input("\nQuantos produtos deseja vender? ")
            if quantidade.lower() == "sair":
                print("\nSaindo de vendas...")
                return total_vendas
            quantidade = int(quantidade)
            if quantidade > estoque:
                print(f"\nDesculpe, não temos estoque suficiente. Temos apenas {estoque} produtos.")
            else:
                quantidade = int(quantidade)
                total_vendas += quantidade
        except ValueError:
            print("\nValor inválido! Tente novamente.")

def reposicoes(valor):
    total_reposicoes = 0
    quantidade = input(valor)
    if quantidade.lower() == "sair":
        print("\nSaindo de reposições...")
        return total_reposicoes
    else:
        quantidade = int(quantidade)
        total_reposicoes += quantidade

print("\nBem vindo de volta!, o que gostaria de fazer?\n\n1 = Vender um produto\n2 = Adicionar um produto\n3 = Verificar o estoque\n4 = Sair do sistema")

while True:
    try:
        opcao = int(input("\nDigite a opção desejada: "))
        if opcao == 1:
            quantidade = vendas()
            estoque -= quantidade
            venda += quantidade
        elif opcao == 2:
            quantidade = reposicoes("\nQuantos produtos deseja adicionar? ")
            estoque += quantidade
            reposicao += quantidade
        elif opcao == 3:
            print(f"\nEstoque atual: {estoque}")
        elif opcao == 4:
            print(f"\nHistórico de vendas: {venda} produtos vendidos\n\nHistórico de reposições: {reposicao} produtos adicionados\n\nEstoque final: {estoque}")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
    except ValueError:
        print("\nValor inválido! Tente novamente.")