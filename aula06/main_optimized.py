while True:
    numero = str(input("Digite um número de 4 dígitos: "))
    if len(numero) == 4 and numero.isdigit():
        break
    print("Erro: Digite um número que contenha exatamente 4 dígitos numéricos.")
    
posicoes = {1: "Unidade", 2: "Dezena", 3: "Centena", 4: "Milhar"}
numero_reverso = numero[::-1]

for posicao, digito in enumerate(numero_reverso, start=1):
    valor = posicoes.get(posicao, "Desconhecido")
    print(f"Posição {posicao}º: {digito} ({valor})")
    
print("Existem números repetidos!" if len(numero) != len(set(numero)) else "Não existem números repetidos.")

soma = sum(int(dig) for dig in numero)
print(f"A soma de todos os números é {soma}.")

print("O número é um palíndromo!" if numero == numero_reverso else "O número não é um palíndromo.")

maior_digito = max(numero)
print(f"O maior número é {maior_digito}.")