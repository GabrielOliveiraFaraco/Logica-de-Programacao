lista = [1, 2, 3, 3, 4, 5, 6, 3, 7, 7, 8, 9, 10]
def remover_duplicados(lista):
    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    return lista_unica
print(f"A lista original é: {lista}")
print(f"A lista sem duplicados é: {remover_duplicados(lista)}")