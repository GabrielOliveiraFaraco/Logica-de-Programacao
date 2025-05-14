matriz = [

]

num = 1
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(num)
        num += 1
    matriz.append(linha)

print(matriz)

for i in matriz:
    for j in i:
        print(j)