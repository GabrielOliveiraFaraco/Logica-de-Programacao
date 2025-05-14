lista = ["banana", "mamão", "uva", "café", "morango"]

def adicionar_fruta(lista, fruta):
    item = input(fruta)
    lista.append(item)
    return lista

def tem_fruta(lista, fruta):
    if fruta in lista:
        print("\nA fruta já está na lista.")
    else:
        print("\nA fruta não está na lista.")

def remover_fruta(lista, fruta):
    if fruta in lista:
        lista.remove(fruta)
        print("\nFruta removida com sucesso.")
        for i in lista:
            print(i)
    else:
        print("\nA fruta não está na lista.")

for i in lista:
    print(i)

temFruta = input("\nDigite uma fruta para verificar se está na lista: \n")
tem_fruta(lista, temFruta)

fruta = adicionar_fruta(lista, "\nDigite uma fruta a ser adicionada: \n")
for i in lista:
    print(i)

removerFruta = input("\nDigite uma fruta para remover da lista: \n")
remover_fruta(lista, removerFruta)