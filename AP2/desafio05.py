# Crie uma função que receba uma matriz 6x2 e retorne um vetor com a média de cada linha.

matriz = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [11, 12]
]

def media_linhas():
    medias = []
    for linha in matriz:
        media = sum(linha) / len(linha)
        medias.append(media)
    return medias

resultado = media_linhas()

print(resultado)