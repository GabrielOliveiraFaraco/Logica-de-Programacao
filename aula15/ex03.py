lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 2]

def frequencia(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

print(f"A frequência do elemento 2 na lista é: {frequencia(lista, 2)}")