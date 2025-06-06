lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def eh_par(numero):
    return numero % 2 == 0

def soma_pares(lista):
    soma = 0
    for numero in lista:
        if eh_par(numero):
            soma += numero
    return soma

resultado = soma_pares(lista)
print(f"A soma dos números pares na lista é: {resultado}")