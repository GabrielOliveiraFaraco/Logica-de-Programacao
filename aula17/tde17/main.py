from pacotes import temporizador, calculadora, sorteio, relógio, cronometro, conversor
def opcoesMenu():
    print("\nOpções do Menu:")
    print("1. Temporizador")
    print("2. Calculadora")
    print("3. Sorteio de Números")
    print("4. Relógio Digital")
    print("5. Cronômetro")
    print("6. Conversor de Temperaturas")
    print("0. Sair\n")
def menu():
    opcoesMenu()
    
    while True:
        escolha = input("Escolha uma opção (0-6): ")
        
        if escolha == '0':
            print("\nSaindo do menu.")
            break
        elif escolha == '1':
            segundos = int(input("\nDigite o tempo em segundos: "))
            print("")
            temporizador.temporizador(segundos)
            opcoesMenu()
        elif escolha == '2':
            calculadora.menuCalculadora()
            opcoesMenu()
        elif escolha == '3':
            inicio = int(input("\nDigite o valor de início: "))
            fim = int(input("\nDigite o valor de fim: "))
            try:
                numeros = sorteio.sorteio_numeros(inicio, fim)
                print(f"\nNúmeros sorteados: {numeros}")
            except ValueError as e:
                print(e)
            opcoesMenu()
        elif escolha == '4':
            relógio.relogio_digital()
            opcoesMenu()
        elif escolha == '5':
            cronometro.cronometro()
            opcoesMenu()
        elif escolha == '6':
            conversor.conversor_temperatura()
            opcoesMenu()
        else:
            print("\nOpção inválida. Tente novamente.")
            opcoesMenu()

if __name__ == "__main__":
    menu()