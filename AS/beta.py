import json
import os

livrosCadastrados = {
    
}

usuariosCadastrados = {
    
}

livrosEmprestados = {
    
}

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    
    if titulo in livrosCadastrados:
        print("Livro já cadastrado.")
    else:
        livrosCadastrados[titulo] = {
            "autor": autor,
            "ano_publicacao": ano_publicacao
        }
        print("Livro cadastrado com sucesso.")

def cadastrar_usuario():
    while True:
        try:
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            
            if cpf in usuariosCadastrados:
                print("Usuário já cadastrado.")
                break
            elif len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido. Deve conter 11 dígitos numéricos.")
            else:
                usuariosCadastrados[cpf] = {
                    "nome": nome
                }
                print("Usuário cadastrado com sucesso.")
                break
        except ValueError:
            print("Erro ao cadastrar usuário. Tente novamente.")

def emprestar_livro():
    titulo = input("Digite o título do livro a ser emprestado: ")
    cpf = input("Digite o CPF do usuário: ")
    
    if titulo not in livrosCadastrados:
        print("Livro não cadastrado.")
    elif cpf not in usuariosCadastrados:
        print("Usuário não cadastrado.")
    elif titulo in livrosEmprestados:
        print("Livro já emprestado.")
    elif livrosEmprestados.get(titulo) == cpf:
        print("Livro já emprestado para este usuário.")
    else:
        livrosEmprestados[titulo] = cpf
        print(f"Livro '{titulo}' emprestado para {usuariosCadastrados[cpf]['nome']}.")

def devolver_livro():
    titulo = input("Digite o título do livro a ser devolvido: ")
    
    if titulo not in livrosEmprestados:
        print("Livro não emprestado.")
    else:
        del livrosEmprestados[titulo]
        print(f"Livro '{titulo}' devolvido com sucesso.")

def listar_livros():
    if not livrosCadastrados:
        print("Nenhum livro cadastrado.")
    else:
        print("\nLivros cadastrados:")
        for titulo, info in livrosCadastrados.items():
            status = "Disponível" if titulo not in livrosEmprestados else "Emprestado"
            print(f"Título: {titulo}, Autor: {info['autor']}, Ano: {info['ano_publicacao']}, Status: {status}")

def main():
    while True:
        try:
            print("\nMenu:")
            print("1. Cadastrar Livro")
            print("2. Cadastrar Usuário")
            print("3. Emprestar Livro")
            print("4. Devolver Livro")
            print("5. Listar Livros")
            print("0. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                cadastrar_livro()
            elif escolha == '2':
                cadastrar_usuario()
            elif escolha == '3':
                emprestar_livro()
            elif escolha == '4':
                devolver_livro()
            elif escolha == '5':
                listar_livros()
            elif escolha == '0':
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")