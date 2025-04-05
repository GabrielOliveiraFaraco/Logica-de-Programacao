ano = int(input("Digite um ano: "))

if ano % 4 == 0 or ano % 100 and ano % 400 == 0:
    print("É um ano bissexto!")
else:
    print("Não é um ano bissexto!")