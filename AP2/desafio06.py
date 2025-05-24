# Crie uma função que verifica se um número está presente em um vetor e retorna a posição (ou -1 se não estiver).

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pedir_numero = int(input("Digite um número: "))
def verificar_numero():
    idx = 0
    for i in lista:
        if i == pedir_numero:
            return idx
        else:
            idx += 1
    idx += 1
    return -1

resultado = verificar_numero()
if resultado != -1:
    print(f"O número {pedir_numero} está na posição {resultado}.")
else:
    print(f"O número {pedir_numero} não está na lista. (posição {resultado})")