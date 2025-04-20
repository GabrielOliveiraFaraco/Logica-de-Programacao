estoque = 100
vendas = 0
reposicao = 0

print("Seja bem vindo ao sistema! Aqui você vai encontrar algumas opções que o ajudarão no manejamendo do estoque.\n\nAlgumas das opções são:\n\n1 - Vender um produto\n2 - Repor o estoque\n3 - Verificar o estoque\n4 - Sair do sistema")

while True:
    try:
        opcao = int(input("\nQual opção você deseja? "))

        if opcao == 1:
            quantidade = int(input("\nQuantos produtos deseja vender? "))

            if quantidade > estoque:
                print("\nVocê não tem produtos suficientes no estoque, reponha o estoque e tente novamente.")
            else:
                estoque -= quantidade
                vendas += quantidade
                print(f"\nVocê vendeu {quantidade} produtos, agora você tem {estoque} produtos no estoque.")

        elif opcao == 2:
            quantidade = int(input("\nQuanto do estoque você deseja repor? "))
            estoque += quantidade
            reposicao += quantidade

        elif opcao == 3:
            print(f"\nVocê tem {estoque} produtos no estoque.")

        elif opcao == 4:
            print(f"Você escolheu sair do sistema, aqui está um resumo do seu dia!\n\nEstoque: {estoque}.\nVendas: {vendas}.\nReposições: {reposicao}.")
            break

        else:
            print("\nDigite um número válido!")
    except ValueError:
        print("\nDigite um valor válido!")