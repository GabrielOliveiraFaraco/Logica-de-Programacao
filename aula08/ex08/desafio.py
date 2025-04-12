estoque = 100
vendas = 0
reposicoes = 0

print("\nBem vindo de volta!, o que gostaria de fazer?\n\n1 = Vender um produto\n2 = Adicionar um produto\n3 = Verificar o estoque\n4 = Sair do sistema")
while True:
    opcao = int(input("\nDigite a opção desejada: "))
    if opcao == 1:
        print(f"\nEstoque atual: {estoque}")
        quantidade = int(input("\nQuantos produtos deseja vender? "))
        if quantidade > estoque:
            print(f"\nDesculpe, não temos estoque suficiente. Temos apenas {estoque} produtos.")
        else:
            estoque -= quantidade
            vendas += quantidade
            print(f"\nVenda realizada com sucesso! Estoque atual: {estoque}")
    elif opcao == 2:
        quantidade = int(input("\nQuantos produtos deseja adicionar? "))
        estoque += quantidade
        reposicoes += quantidade
        print(f"\nProdutos adicionados com sucesso! Estoque atual: {estoque}")
    elif opcao == 3:
        print(f"\nEstoque atual: {estoque}")
    elif opcao == 4:
        print(f"\nHistórico de vendas: {vendas} produtos vendidos\n\nHistórico de reposições: {reposicoes} produtos adicionados\n\nEstoque final: {estoque}")
        break
    else:
        print("\nOpção inválida! Tente novamente.")