def validar_senha(senha):
    if len(senha) < 8:
        return "Senha inválida"
    
    tem_letra = False
    tem_numero = False
    
    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        elif caractere.isdigit():
            tem_numero = True
            
    if tem_letra and tem_numero:
        return "Senha válida"
    else:
        return "Senha inválida"

senha = input("Digite a senha: ")
print(validar_senha(senha))