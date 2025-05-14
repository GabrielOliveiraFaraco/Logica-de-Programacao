# Realizar https://ulbra.instructure.com/courses/12728/assignments/61347?module_item_id=387610

user = "admin"
password = "admin"

def login():
    user_input = input("Digite o usuário: ")
    password_input = input("Digite a senha: ")

    if user_input == user and password_input == password:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False

def main():
    tentativas = 0
    max_tentativas = 3
    
    while tentativas < max_tentativas:
        if login():
            print("Bem-vindo ao sistema!")
            return
        else:
            tentativas += 1
            if tentativas < max_tentativas:
                print(f"Tente novamente. Tentativas restantes: {max_tentativas - tentativas}")
    
    print("Número máximo de tentativas excedido. Acesso bloqueado.")

if __name__ == "__main__":
    main()