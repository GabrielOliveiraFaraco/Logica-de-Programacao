def conversor_temperatura():
    print("Conversor de Temperaturas")
    print("Escolha a temperatura de origem:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    origem = int(input("Digite a opção (1-3): "))
    
    valor = float(input(f"Digite o valor em {origem}: "))
    try:
        if origem == 1:
            fahrenheit = (valor * 9/5) + 32
            kelvin = valor + 273.15
            print(f"{valor}°C é igual a {fahrenheit}°F e {kelvin}K")
            
        elif origem == 2:
            celsius = (valor - 32) * 5/9
            kelvin = celsius + 273.15
            print(f"{valor}°F é igual a {celsius}°C e {kelvin}K")
            
        elif origem == 3:
            celsius = valor - 273.15
            fahrenheit = (celsius * 9/5) + 32
            print(f"{valor}K é igual a {celsius}°C e {fahrenheit}°F")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError as e:
        print(f"Erro: {e}. Certifique-se de inserir um número válido.")