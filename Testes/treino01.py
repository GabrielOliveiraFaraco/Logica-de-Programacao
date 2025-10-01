saldo = 1000

def opcoes():
    print("Bem vindo ao sistem de Banco!")
    print("\nEscolha o que gostaria de fazer:")
    print("\n1 - Verificar Saldo")
    print("\n2 - Depositar")
    print("\n3 - Sacar")
    print("\n4 - Ver as opções novamente")
    print("\n5 - Sair")


def sacar():
    global saldo
    valor = float(input("\nDigite o valor que deseja sacar: "))
    
    if valor > saldo:
        print(f"\nNão foi possível sacar. Você tem apenas R${saldo:.2f} na conta.")
        return saldo
    else:
        saldo -= valor
        print(f"\nValor de R${valor:.2f} sacado com sucesso!")

def depositar():
    global saldo
    valor = float(input("\nDigite o valor que deseja depositar: "))
    if valor <= 0:
        print("\nO valor não pode ser menor ou igual que zero.")
    else:
        saldo += valor
        print(f"\nValor de R${valor:.2f} foi depositado com sucesso!")

def verificarSaldo():
    print(f"\nSaldo: R${saldo:.2f}.")

def menu():
    opcoes()

    while True:
        try:
            
            opcao = int(input("\nDigite uma opção do menu: "))
            
            if opcao == 1:
                verificarSaldo()
            elif opcao == 2:
                depositar()
            elif opcao == 3:
                sacar()
            elif opcao == 4:
                opcoes()
            elif opcao == 5:
                break
            else:
                print("Digite um valor válido entre 1 - 5!")
            
        except ValueError:
            print("Entrada inválida! Digite um numero entre 1 - 5.")

if __name__ == __name__:
    menu()