import time

def temporizador(segundos):
    if segundos < 0:
        raise ValueError("O valor de segundos deve ser um número não negativo.")
    
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    
    print("Tempo esgotado!")