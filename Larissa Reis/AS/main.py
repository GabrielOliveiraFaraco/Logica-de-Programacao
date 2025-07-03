biblioteca = {
    "livro": {},
    "usuario": {},
    "emprestimo": {}
}

def cadastrar_livro():
    adicionar_livro = input("\nCadastrar um livro? (sim ou não): ").strip().lower()
    if adicionar_livro == "sim":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")

        if titulo in biblioteca["livro"]:
            print("\nLivro já cadastrado.")
        else:
            biblioteca["livro"][titulo] = {
                "autor": autor,
                "ano_publicacao": ano_publicacao
            }
            print("\nLivro adicionado com sucesso.")
    else:
        print("\nCadastro de livro cancelado.")

def cadastrar_usuario():
    adicionar_usuario = input("\nCadastrar um usuário? (sim ou não): ").strip().lower()
    if adicionar_usuario == "sim":
        while True:
            try:
                nome = input("Digite o nome do usuário: ")
                cpf = input("Digite o CPF do usuário: ")

                if cpf in biblioteca["usuario"]:
                    print("\nUsuário já cadastrado.")
                    break
                elif len(cpf) != 11 or not cpf.isdigit():
                    print("\nCPF inválido. Deve conter 11 dígitos numéricos.")
                else:
                    biblioteca["usuario"][cpf] = {
                        "nome": nome
                    }
                    print("\nUsuário cadastrado com sucesso.")
                    break
            except ValueError:
                print("\nErro ao cadastrar usuário. Tente novamente.")
    else:
        print("\nCadastro de usuário cancelado.")
        
def emprestimo_de_livro():
    emprestar_livro = input("\nRetirar um livro? (sim ou não): ").strip().lower()
    if emprestar_livro == "sim":
        titulo = input("Digite o título do livro a ser retirado: ")
        cpf = input("Digite o CPF do usuário: ")

        if titulo not in biblioteca["livro"]:
            print("\nLivro não cadastrado.")
        elif cpf not in biblioteca["usuario"]:
            print("\nUsuário não cadastrado.")
        elif titulo in biblioteca["emprestimo"]:
            print("\nLivro já retirado.")
        elif biblioteca["emprestimo"].get(titulo) == cpf:
            print("\nLivro já emprestado para este usuário.")
        elif cpf in biblioteca["emprestimo"].values():
            print("\nUsuário já possui um livro emprestado.")
        else:
            biblioteca["emprestimo"][titulo] = cpf
            print(f"\nLivro '{titulo}' emprestado para {biblioteca['usuario'][cpf]['nome']}.")
    else:
        print("\nEmprestimo de livro cancelado.")

def listar_livros():
    if biblioteca["livro"]:
        print("\nLivros cadastrados:")
        for titulo, detalhes in biblioteca["livro"].items():
            print(f"- {titulo} (Autor: {detalhes['autor']}, Ano: {detalhes['ano_publicacao']})")
        if biblioteca["emprestimo"]:
            print("\nLivros retirados:")
            for titulo, cpf in biblioteca["emprestimo"].items():
                print(f"- {titulo} (Emprestado para: {biblioteca['usuario'][cpf]['nome']})")
        else:
            print("\nNenhum livro retirado.")
    else:
        print("\nNenhum livro cadastrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Cadastrar usuário")
        print("3. Emprestímo de livro")
        print("4. Listar livros")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            emprestimo_de_livro()
        elif opcao == "4":
            listar_livros()
        elif opcao == "5":
            print("\nSistema encerrado.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    print("\nBem-vindo à biblioteca!")
    menu()