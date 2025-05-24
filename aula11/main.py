""" lista = ["palavra", 10, True]

tupla = ("palavra", 10, True)

print(lista[0])
print(tupla[0])

lista[0] = "outra palavra"
print(lista[0])

lista.append("nova palavra")

lista.pop(0)

print(lista) """

""" matriz = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

for i in matriz:
    for j in i:
        print(j) """

""" lista = ("banana", "mamão", "uva", "café")
idx = 0

for item in lista:
    print(idx, item)
    idx += 1
idx = 0

lista.append(input("Digite um item: "))

for item in lista:
    print(idx, item)
    idx += 1
idx = 0

lista.pop(int(input("Digite o índice do item a ser removido: ")))

for item in lista:
    print(idx, item)
    idx += 1
idx = 0 """

matriz  = [

]

num = 0

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(num)
        num += 1
    matriz.append(linha)

for i in matriz:
    for j in i:
        print(j)



""" for i in range(4):
    linha = []
    for j in range(4):
        linha.append(num)
        num += 1
    matriz.append(linha)

print(matriz)

for i in matriz:
    for j in i:
        print(j) """