# Dada uma lista de inteiros, retorne o menor número e a posição (índice) onde ele aparece.

lista = [34, 56, 78, 7, 90, 23, 45, 67, 89, 12, 45, 90, 23]

def menor_numero():
    idx = 0
    for item in lista:
        if item == min(lista):
            print(f"O menor número é {item} e está na posição {idx}")
        else:
            idx += 1

menor_numero()