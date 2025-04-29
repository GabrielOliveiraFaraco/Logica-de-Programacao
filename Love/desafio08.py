estoque = 100
vendas = 0
reposicao = 0

def venda(valor):
    while True:
        quantidade = int(input(valor))
        try:
            if quantidade > estoque:
                print(f"\nDesculpe, não temos estoque suficiente. Temos apenas {estoque} produtos.")
            else:
                return quantidade
        except ValueError:
            print("\nValor inválido! Tente novamente.")

def reposicoes(valor):
    while True:
        try:
            quantidade = int(input(valor))
            return quantidade
        except ValueError:
            print("\nValor inválido! Tente novamente.")

while True:

    options = int(input("\nEscolha entre as quatro opções seguintes:\n1- Vender\n2- Repor produto\n3- Consultar estoque\n4- Encerrar turno\n\nVocê vai: "))

    if options == 1:
        quantidade = venda("\nQuantos produtos serão vendidos? ")
        estoque -= quantidade
        vendas += quantidade

    elif options == 2:
        quantidade = reposicoes("\nQuantos produtos serão repostos? ")
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