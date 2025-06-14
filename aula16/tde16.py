my_dict =  {
    
}

def cadastrar_aluno(nome, nota):
    if nome in my_dict:
        print(f"Aluno(a) {nome} já cadastrado.")
    else:
        my_dict[nome.upper()] = nota
        print(f"Aluno(a) {nome} cadastrado com nota {nota}.")

def atualizar_nota(nome, nova_nota):
    if nome.upper() in my_dict:
        my_dict[nome] = nova_nota
        print(f"\nNota do(a) aluno(a) {nome} atualizada para {nova_nota}.")
    else:
        print(f"\nAluno {nome} não encontrado.")

def calcular_media():
    if not my_dict:
        print("\nNenhum aluno cadastrado.")
        return
    media = sum(my_dict.values()) / len(my_dict)
    print(f"\nMédia das notas: {media:.2f}")


def listar_aprovados():
    aprovados = {nome: nota for nome, nota in my_dict.items() if nota >= 7}
    if not aprovados:
        print("\nNenhum aluno aprovado.")
    else:
        print("\nAlunos aprovados:\n")
        for nome, nota in aprovados.items():
            print(f"{nome}: {nota}")

def remover_aluno(nome):
    if nome in my_dict:
        del my_dict[nome]
        print(f"\nAluno(a) {nome} removido.")
    else:
        print(f"\nAluno(a) {nome} não encontrado.")

def verificar_aluno(nome):
    nome_upper = nome.upper()
    if nome_upper in my_dict:
        print(f"\nAluno(a) {nome_upper} encontrado com nota {my_dict[nome_upper]}.")
    else:
        print(f"\nAluno(a) {nome_upper} não encontrado.")

def limpar_dicionario():
    my_dict.clear()
    print("\nDicionário de alunos limpo.")

def contar_alunos():
    print(f"\nNúmero total de alunos cadastrados: {len(my_dict)}")

def nomes_alunos():
    if not my_dict:
        print("\nNenhum aluno cadastrado.")
    else:
        print("\nNomes dos alunos cadastrados:")
        for nome in my_dict.keys():
            print(nome)

def nome_nota_alunos():
    if not my_dict:
        print("\nNenhum aluno cadastrado.")
    else:
        print("\nNomes e notas dos alunos cadastrados:\n")
        for nome, nota in my_dict.items():
            print(f"{nome}: {nota}")

def menu():
    while True:
        try:
            print("\nMenu:\n\n1. Cadastrar aluno\n2. Atualizar nota\n3. Calcular média\n4. Listar aprovados\n5. Remover aluno\n6. Verificar aluno\n7. Limpar dicionário\n8. Contar alunos\n9. Nomes dos alunos\n10. Nomes e notas dos alunos\n11. Sair")
            opcao = input("\nEscolha uma opção (1-11): ")
            if opcao == '1':
                while True:
                    try:
                        nome = input("Digite o nome do aluno: ")
                        nota = float(input("Digite a nota do aluno: "))
                        if nota < 0 or nota > 10:
                            print("Nota deve ser entre 0 e 10.")
                        else:
                            cadastrar_aluno(nome, nota)
                            print("Aluno cadastrado com sucesso.")
                            break
                    except ValueError:
                        print("Nota inválida. Por favor, digite um número.")
            elif opcao == '2':
                nome = input("Digite o nome do aluno: ")
                try:
                    nova_nota = float(input("Digite a nova nota do aluno: "))
                    if nova_nota < 0 or nova_nota > 10:
                        print("Nota deve ser entre 0 e 10.")
                    else:
                        atualizar_nota(nome, nova_nota)
                except ValueError:
                    print("Nota inválida. Por favor, digite um número.")
            elif opcao == '3':
                calcular_media()
            elif opcao == '4':
                listar_aprovados()
            elif opcao == '5':
                nome = input("Digite o nome do aluno a ser removido: ")
                remover_aluno(nome)
            elif opcao == '6':
                nome = input("Digite o nome do aluno a ser verificado: ")
                verificar_aluno(nome)
            elif opcao == '7':
                limpar_dicionario()
            elif opcao == '8':
                contar_alunos()
            elif opcao == '9':
                nomes_alunos()
            elif opcao == '10':
                nome_nota_alunos()
            elif opcao == '11':
                print("Saindo do programa.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    print("Bem-vindo ao sistema de gerenciamento de alunos!")
    menu()