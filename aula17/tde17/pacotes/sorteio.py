import random

def sorteio_numeros(inicio, fim):
    if inicio >= fim:
        raise ValueError("O valor de início deve ser menor que o valor de fim.")
    
    numeros = random.sample(range(inicio, fim + 1), 5)
    return numeros