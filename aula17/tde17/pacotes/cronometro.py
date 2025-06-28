import time

def cronometro():
    segundos = 0
    valor = int(input("Digite o valor máximo do cronômetro (em segundos): "))

    while True:
        print(f"Tempo decorrido: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos += 1

        if segundos == valor:  # Para o cronômetro após 10 segundos
            break

    print("\nCronômetro finalizado.")