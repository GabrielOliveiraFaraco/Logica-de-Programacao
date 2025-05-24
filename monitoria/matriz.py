matriz = [
    
]

num = 5

for i in range(3):
    lista = []
    for j in range(3):
        lista.append(num)
        num += 1
    matriz.append(lista)

for i in matriz:
    for j in i:
        print(j)