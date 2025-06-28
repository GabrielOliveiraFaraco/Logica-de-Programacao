def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("\nDivisão por zero não é permitida.")
    return a / b

def menuCalculadora():
    print("\nCalculadora")
    print("1. Somar dois números")
    print("2. Subtrair dois números")
    print("3. Multiplicar dois números")
    print("4. Dividir dois números")
    print("5. Sair")

    while True:
        try:
            escolha = input("\nEscolha uma opção (1-5): ")
            if escolha == '5':
                print("\nSaindo da calculadora.")
                break
            elif escolha in ['1', '2', '3', '4']:
                a = float(input("\nDigite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                if escolha == '1':
                    print(f"\nResultado: {soma(a, b)}")
                elif escolha == '2':
                    print(f"\nResultado: {subtracao(a, b)}")
                elif escolha == '3':
                    print(f"\nResultado: {multiplicacao(a, b)}")
                elif escolha == '4':
                    try:
                        print(f"\nResultado: {divisao(a, b)}")
                    except ValueError as e:
                        print(e)
            else:
                print("\nOpção inválida. Tente novamente.")
        except ValueError as e:
            print(f"\nErro: {e}. Certifique-se de inserir um número válido.")