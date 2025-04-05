def coletar_respostas(perguntas):
    respostas = []
    for pergunta in perguntas:
        while True:
            try:
                resposta = int(input(f"{pergunta} (1-5): "))
                if 1 <= resposta <= 5:
                    respostas.append(resposta)
                    break
                else:
                    print("Por favor, digite um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Digite um número entre 1 e 5.")
    return sum(respostas)

def main():
    print("Olá, aqui você fará um teste de qual área de programação você se encaixa melhor!\n\nEntre elas, estão:\n"
          "A. Desenvolvimento de Software\nB. Área de Produtos (UX/UI, Product Owner, Product Manager, etc.)\n"
          "C. Área de Qualidade (Testes, QA, automação de testes, etc.)\n\nPara isso, você responderá algumas perguntas "
          "utilizando números de 1 a 5.\n\nA pontuação de cada pergunta será:\n1. Discordo totalmente\n2. Discordo\n"
          "3. Neutro\n4. Concordo\n5. Concordo totalmente\n\nVamos começar!\n")

    areas = {
        "Desenvolvimento de Software": [
            "Gosto de programar e resolver problemas com código.",
            "Tenho interesse em criar aplicativos e sites.",
            "Gosto de aprender novas linguagens de programação.",
            "Prefiro trabalhar com lógica e estruturação de código.",
            "Tenho paciência para depurar erros e otimizar código."
        ],
        "Área de Produtos (UX/UI, Product Owner, Product Manager, etc.)": [
            "Gosto de pensar na experiência do usuário ao usar um sistema.",
            "Tenho interesse em pesquisa de mercado e comportamento do usuário.",
            "Me interesso por criar soluções inovadoras e intuitivas.",
            "Gosto de trabalhar com design, wireframes ou prototipagem.",
            "Quero entender e definir estratégias para melhorar produtos digitais."
        ],
        "Área de Qualidade (Testes, QA, automação de testes, etc.)": [
            "Gosto de testar e garantir que sistemas funcionem corretamente.",
            "Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.",
            "Acredito que testes automatizados ajudam a evitar falhas em sistemas.",
            "Gosto de seguir padrões e documentar processos para garantir qualidade.",
            "Quero trabalhar garantindo que um software funcione bem para todos os usuários."
        ]
    }

    resultados = {area: coletar_respostas(perguntas) for area, perguntas in areas.items()}
    maior_pontuacao = max(resultados.values())
    vencedores = [area for area, pontuacao in resultados.items() if pontuacao == maior_pontuacao]

    print("\n\nVocê se encaixa melhor na(s) área(s) de:\n")
    for vencedor in vencedores:
        print(f"- {vencedor}")
    print("\nObrigado por participar do teste!\n")

if __name__ == "__main__":
    main()
