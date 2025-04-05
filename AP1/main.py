print("Olá, aqui você fara um teste de qual área de programação você se encaixa melhor!\n\nEntre elas, estão:\nA. Desenvolvimento de Software\nB. Área de Produtos (UX/UI, Product Owner, Product Manager, etc.)\nC. Área de Qualidade (Testes, QA, automação de testes, etc.)\n\nPara isso, você responderá algumas perguntas utilizando números de 1 a 5.\n\nA pontuação de cada pergunta será:\n1. Discordo totalmente\n2. Discordo\n3. Neutro\n4. Concordo\n5. Concordo totalmente\n\nVamos começar!\n")

# definindo as perguntas de Desenvolvimento de Software
perguntas1 = ["Gosto de programar e resolver problemas com código.",
                "Tenho interesse em criar aplicativos e sites.",
                "Gosto de aprender novas linguagens de programação.",
                "Prefiro trabalhar com lógica e estruturação de código.",
                "Tenho paciência para depurar erros e otimizar código."]

# coletando as respostas do usuário para o tema 1
respostas1 = []
for pergunta in perguntas1:
    while True:
        try:
            resposta = int(input(f"{pergunta} (1-5): "))
            if resposta >= 1 and resposta <= 5:
                respostas1.append(resposta)
                break
            else: print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 1 e 5.")

# somando as respostas do tema 1
soma1 = sum(respostas1)

# definindo as perguntas para o tema 2
perguntas2 = ["Gosto de pensar na experiência do usuário ao usar um sistema.",
                "Tenho interesse em pesquisa de mercado e comportamento do usuário.",
                "Me interesso por criar soluções inovadoras e intuitivas.",
                "Gosto de trabalhar com design, wireframes ou prototipagem.",
                "Quero entender e definir estratégias para melhorar produtos digitais."]

# coletando as respostas do usuário de Área de Produtos
respostas2 = []
for pergunta in perguntas2:
    while True:
        try:
            resposta = int(input(f"{pergunta} (1-5): "))
            if resposta >= 1 and resposta <= 5:
                respostas2.append(resposta)
                break
            else: print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 1 e 5.")

# somando as respostas do tema 2
soma2 = sum(respostas2)

# definindo as perguntas de Área de Qualidade
perguntas3 = ["Gosto de testar e garantir que sistemas funcionem corretamente.",
                "Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.",
                "Acredito que testes automatizados ajudam a evitar falhas em sistemas.",
                "Gosto de seguir padrões e documentar processos para garantir qualidade.",
                "Quero trabalhar garantindo que um software funcione bem para todos os usuários."]

# coletando as respostas do usuário para o tema 3
respostas3 = []
for pergunta in perguntas3:
    while True:
        try:
            resposta = int(input(f"{pergunta} (1-5): "))
            if resposta >= 1 and resposta <= 5:
                respostas3.append(resposta)
                break
            else: print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 1 e 5.")

#  somando as respostas do tema 3
soma3 = sum(respostas3)

# definindo qual o maior número entre as somas
total = max(soma1, soma2, soma3)

# criando uma lista para armazenar as áreas correspondentes
vencedor = []

# verificando qual área corresponde à maior soma
if total == soma1:
    vencedor.append("Desenvolvimento de Software")
if total == soma2:
    vencedor.append("Área de Produtos (UX/UI, Product Owner, Product Manager, etc.)")
if total == soma3:
    vencedor.append("Área de Qualidade (Testes, QA, automação de testes, etc.)")

# imprimindo o resultado
print("\n\nVocê se encaixa melhor na(s) área(s) de:\n")
for i in vencedor:
    print(f"- {i}")
print("\nObrigado por participar do teste!\n")