def soma():
    valor_a = int(input("Digite o número 1 "))
    valor_b = int(input("Digite o número 2 "))
    print(valor_a + valor_b)

soma()

def verificacao(entrada):
    while True:
        opcao = input(entrada)
        if opcao != "sair":
            print(opcao)
        else:
            break

verificacao("Digite algo ou 'sair' para sair: ")
verificacao("Bom dia senhores! ")

def int_verificador(entrada):
    while True:
        valor = input(entrada)
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.") 

ano_nascimento = int_verificador("Digite seu ano de nascimento: ")

print(ano_nascimento)