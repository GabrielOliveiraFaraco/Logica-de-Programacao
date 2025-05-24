# Crie uma função que receba um vetor de números inteiros e retorne a soma apenas dos números primos.  

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_primos = []

def e_primo():
    for i in lista:
        if i < 2:
            continue
        elif all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            numeros_primos.append(i)
    return sum(numeros_primos)

resultado = e_primo()
print(f"A soma dos números primos é: {resultado}")