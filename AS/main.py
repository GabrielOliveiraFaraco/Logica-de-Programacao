import json
import os

ARQUIVO_JSON = 'biblioteca.json'

dados_biblioteca = {
    "livros": {},
    "usuarios": {},
    "emprestimos": {}
}

def carregar_dados():
    global dados_biblioteca
    try:
        if os.path.exists(ARQUIVO_JSON):
            with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
                dados_biblioteca = json.load(f)
    except json.JSONDecodeError:
        print("\nErro: Arquivo JSON corrompido. Iniciando com dados vazios.")
    except Exception as e:
        print(f"\nErro ao carregar dados: {e}. Iniciando com dados vazios.")

def salvar_dados():
    try:
        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
            json.dump(dados_biblioteca, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"\nErro ao salvar dados: {e}")

def cadastrar_livro():
    titulo = input("\nDigite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    
    if titulo in dados_biblioteca["livros"]:
        print("\nLivro já cadastrado.")
    else:
        dados_biblioteca["livros"][titulo] = {
            "autor": autor,
            "ano_publicacao": ano_publicacao
        }
        salvar_dados()
        print("\nLivro cadastrado com sucesso.")

def cadastrar_usuario():
    while True:
        try:
            nome = input("\nDigite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            
            if cpf in dados_biblioteca["usuarios"]:
                print("\nUsuário já cadastrado.")
                break
            elif len(cpf) != 11 or not cpf.isdigit():
                print("\nCPF inválido. Deve conter 11 dígitos numéricos.")
            else:
                dados_biblioteca["usuarios"][cpf] = {
                    "nome": nome
                }
                salvar_dados()
                print("\nUsuário cadastrado com sucesso.")
                break
        except ValueError:
            print("\nErro ao cadastrar usuário. Tente novamente.")

def emprestar_livro():
    titulo = input("\nDigite o título do livro a ser emprestado: ")
    cpf = input("Digite o CPF do usuário: ")
    
    if titulo not in dados_biblioteca["livros"]:
        print("\nLivro não cadastrado.")
    elif cpf not in dados_biblioteca["usuarios"]:
        print("\nUsuário não cadastrado.")
    elif titulo in dados_biblioteca["emprestimos"]:
        print("\nLivro já emprestado.")
    elif dados_biblioteca["emprestimos"].get(titulo) == cpf:
        print("\nLivro já emprestado para este usuário.")
    elif cpf in dados_biblioteca["emprestimos"].values():
        print("\nUsuário já possui um livro emprestado.")
    else:
        dados_biblioteca["emprestimos"][titulo] = cpf
        salvar_dados()
        print(f"\nLivro '{titulo}' emprestado para {dados_biblioteca['usuarios'][cpf]['nome']}.")

def devolver_livro():
    titulo = input("\nDigite o título do livro a ser devolvido: ")
    
    if titulo not in dados_biblioteca["emprestimos"]:
        print("\nLivro não emprestado.")
    else:
        del dados_biblioteca["emprestimos"][titulo]
        salvar_dados()
        print(f"\nLivro '{titulo}' devolvido com sucesso.")

def listar_livros():
    if not dados_biblioteca["livros"]:
        print("\nNenhum livro cadastrado.")
    else:
        print("\nLivros cadastrados:\n")
        for titulo, info in dados_biblioteca["livros"].items():
            status = "Disponível" if titulo not in dados_biblioteca["emprestimos"] else "Emprestado"
            print(f"Título: {titulo}, Autor: {info['autor']}, Ano: {info['ano_publicacao']}, Status: {status}")

def excluir_livro():
    titulo = input("\nDigite o título do livro a ser excluído: ")
    
    if titulo not in dados_biblioteca["livros"]:
        print("\nLivro não cadastrado.")
    else:
        del dados_biblioteca["livros"][titulo]
        salvar_dados()
        print(f"\nLivro '{titulo}' excluído com sucesso.")

def main():
    carregar_dados()
    
    while True:
        try:
            print("\nMenu:\n")
            print("1. Cadastrar Livro")
            print("2. Cadastrar Usuário")
            print("3. Emprestar Livro")
            print("4. Devolver Livro")
            print("5. Listar Livros")
            print("0. Sair")
            
            escolha = int(input("\nEscolha uma opção: "))
            
            if escolha == 1:
                cadastrar_livro()
            elif escolha == 2:
                cadastrar_usuario()
            elif escolha == 3:
                emprestar_livro()
            elif escolha == 4:
                devolver_livro()
            elif escolha == 5:
                listar_livros()
            elif escolha == 6:
                excluir_livro()
            elif escolha == 0:
                salvar_dados()
                print("\nSaindo do sistema.\n")
                break
            else:
                print("\nOpção inválida. Tente novamente.")
        except Exception as e:
            print(f"\nErro: {e}. Tente novamente.")

if __name__ == "__main__":
    main()