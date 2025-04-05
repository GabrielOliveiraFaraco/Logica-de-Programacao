l1 = float(input("Digite um número: "))
l2 = float(input("Digite um número: "))
l3 = float(input("Digite um número: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 >l2:
    if l1 == l2 == l3:
        print("É um Triângulo Equilatero")
    elif l1 ==l2 or l2 == l3 or l3 == l1:
        print("É um Triângulo Isósceles.")
    else:
        print("É um Triângulo Escaleno.")
else:
    print("Não é um Triângulo.")