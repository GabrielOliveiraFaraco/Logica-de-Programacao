tupla = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

while True:
    try:
        dia = int(input("Digite o dia da semana: "))
        if dia == 1:
            print(tupla[0])
            break
        elif dia == 2:
            print(tupla[1])
            break
        elif dia == 3:
            print(tupla[2])
            break
        elif dia == 4:
            print(tupla[3])
            break
        elif dia == 5:
            print(tupla[4])
            break
        elif dia == 6:
            print(tupla[5])
            break
        elif dia == 7:
            print(tupla[6])
            break
        else:
            print("Digite um número entre 1 e 7.")
    except ValueError:
        print("Digite um número válido.")

lista = list(tupla)

print(type(lista))