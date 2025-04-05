while True: # Vai pedir para a pessoa digitar os números até ela colocar exatamente 4 dígitos
    numero = str(input("Digite um número de 4 dígitos: "))
    if len(numero) == 4:
        break
    print("Erro: Digite um número que contenha 4 dígitos.")

for posicao, digito in enumerate(numero[::-1], start=1): # Vai verificar se o número é "Unidade", "Dezena", "Centena" ou "Milhar"
    
    if posicao == 1:
        valor = "Unidade"
    elif posicao == 2:
        valor = "Dezena"
    elif posicao == 3:
        valor = "Centena"
    else: valor = "Milhar"
    
    print(f"Posição {posicao}º: {digito} ({valor})")
    
if len(numero) != len(set(numero)): # Verifica se existem números repetidos
    print("Existem números repetidos!")
else: print("Não existem números repetidos.")

soma = sum(int(dig) for dig in numero) # Soma todos os números
print(f"A soma de todos os números é {soma}.")

if numero == numero[::-1]: # Verifica de o número é um palindromo
    print("O número é um palíndromo!")
else: print("O numero não é um palíndromo.")

maxNum = max(numero) # Verifica qual o maior número
print(f"O maior número é {maxNum}.")