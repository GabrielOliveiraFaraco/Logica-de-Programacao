# Escreva uma função que gere uma matriz identidade de ordem 4 Em matemática, matriz identidade é uma matriz diagonal, cujos elementos da diagonal principal são todos iguais. Sua função, então, deve criar uma matriz 4x4 com preenchida com 0, mas sua diagonal deve ser preenchida com 1.

matriz = [
    
]

def matriz_identidade():
    for i in range(4):
        linha = []
        for j in range(4):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    print(matriz)

matriz_identidade()