nota = [0, 0, 0]

def calcular_media(lista_de_notas):
    if not lista_de_notas:
        return 0
    return sum(lista_de_notas) / len(lista_de_notas)

def avaliar_desempenho(media):
    if media >= 6:
        return "Aprovado"
    elif 0 < media < 6:
        return "Recuperação"
    else:
        return "Reprovado"

print(avaliar_desempenho(calcular_media(nota)))