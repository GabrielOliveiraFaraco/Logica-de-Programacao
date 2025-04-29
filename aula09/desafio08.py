estoque = 100
venda = 0
reposicao = 0

def realizar_venda(estoque_atual):
    total_vendas = 0
    while True:
        try:
            quantidade = input("\nQuantos produtos deseja vender? (digite 'sair' para voltar) ")
            if quantidade.lower() == "sair":
                print("\nSaindo do modo de vendas...")
                return total_vendas
            
            quantidade = int(quantidade)
            if quantidade <= 0:
                print("\nA quantidade deve ser maior que zero!")
            elif quantidade > estoque_atual:
                print(f"\nDesculpe, não temos estoque suficiente. Temos apenas {estoque_atual} produtos.")
            else:
                total_vendas += quantidade
                estoque_atual -= quantidade
                print(f"Venda de {quantidade} unidades realizada. Estoque restante: {estoque_atual}")
                
        except ValueError:
            print("\nValor inválido! Digite um número inteiro ou 'sair'.")

def realizar_reposicao():
    total_reposicoes = 0
    while True:
        try:
            quantidade = input("\nQuantos produtos deseja adicionar ao estoque? (digite 'sair' para voltar) ")
            if quantidade.lower() == "sair":
                print("\nSaindo do modo de reposição...")
                return total_reposicoes
            
            quantidade = int(quantidade)
            if quantidade <= 0:
                print("\nA quantidade deve ser maior que zero!")
            else:
                total_reposicoes += quantidade
                print(f"Reposição de {quantidade} unidades realizada.")
                
        except ValueError:
            print("\nValor inválido! Digite um número inteiro ou 'sair'.")

print("\nBem vindo ao sistema de gerenciamento de estoque!")
print("Opções disponíveis:\n1 = Modo Venda\n2 = Modo Reposição\n3 = Verificar estoque\n4 = Sair do sistema")

while True:
    try:
        opcao = int(input("\nDigite a opção desejada: "))
        
        if opcao == 1:
            vendas_realizadas = realizar_venda(estoque)
            estoque -= vendas_realizadas
            venda += vendas_realizadas
            print(f"Total de vendas realizadas: {vendas_realizadas}")
            
        elif opcao == 2:
            reposicoes_realizadas = realizar_reposicao()
            estoque += reposicoes_realizadas
            reposicao += reposicoes_realizadas
            print(f"Total de reposições realizadas: {reposicoes_realizadas}")
            
        elif opcao == 3:
            print(f"\nEstoque atual: {estoque} unidades")
            print(f"Total de vendas: {venda} unidades")
            print(f"Total de reposições: {reposicao} unidades")
            
        elif opcao == 4:
            print("\nRelatório final:")
            print(f"- Total de produtos vendidos: {venda}")
            print(f"- Total de produtos repostos: {reposicao}")
            print(f"- Estoque final: {estoque}")
            print("\nEncerrando o sistema...")
            break
            
        else:
            print("\nOpção inválida! Por favor, digite um número entre 1 e 4.")
            
    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas números para selecionar a opção.")