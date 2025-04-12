estoque = 100
vendas = 0
reposicao = 0

while True:

    options = int(input("\nEscolha entre as quatro opções seguintes:\n1- Vender\n2- Repor produto\n3- Consultar estoque\n4- Encerrar turno\n\nVocê vai: "))

    if options == 1:
        quantidade = int(input("\nQuantos produtos serão vendidos? "))
        if estoque == 0:
            print("\nNão pôde ser vendido, reponha o estoque.")
        else:
            estoque -= quantidade
            vendas += quantidade

    elif options == 2:
        quantidade = int(input("\nQuantos produtos serão repostos? "))
        estoque += quantidade
        reposicao += quantidade
        print(f"\nForam repostos {quantidade} produtos.")

    elif options == 3:
        print(f"\nEstoque atual: {estoque}")

    elif options == 4:
        print(f"\nEstoque: {estoque}\nVendas: {vendas}\nReposições: {reposicao}")
        break
    else:
        print("\nPor favor, digite um número válido.")