user = str(input("Usuário: "))
password = str(input("Senha: "))

if user == "admin" and password == "password":
    print("Acesso Permitido!")
else:
    print("Acesso Negado!")