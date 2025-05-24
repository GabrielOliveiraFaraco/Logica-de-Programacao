listaMercado = ["Banana", "Laranja", "Morango"]
def adicionar_item():
    fruta = input("Digite o nome da fruta que deseja adicionar: ")
    listaMercado.append(fruta)
    print(f"{fruta} foi adicionada à lista de mercado.")
    for i in listaMercado:
        print(i)

adicionar_item()






""" def adicionar_item():
    fruta = input("Digite o nome da fruta que deseja adicionar: ")
    listaMercado.append(fruta)
    print(f"{fruta} foi adicionada à lista de mercado.")
    for i in listaMercado:
        print(i)
"""