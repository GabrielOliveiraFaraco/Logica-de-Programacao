# Crie uma função que receba um vetor de inteiros e um número x, e retorne quantas vezes x aparece no vetor.  

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]
x = 5
def contar_ocorrencias(lista, x):
    contador = 0
    for i in lista:
        if i == x:
            contador += 1
    return contador

resultado = contar_ocorrencias(lista, x)
print(f"O número {x} aparece {resultado} vezes na lista.")