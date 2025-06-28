import time

def relogio_digital():
    horas = 0
    minutos = 0
    segundos = 0

    while True:
        print(f"{horas:02}:{minutos:02}:{segundos:02}", end="\r")
        time.sleep(1)
        segundos += 1

        if segundos == 10:
            break

    print("\nRelógio digital finalizado.")