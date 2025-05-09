nome = str(input("Nome: "))

print(f"Olá {nome}, seja bem-vindo(a)!\nPara continuar, responda as perguntas com um dígito de 1 a 5 (sendo 1 discordo totalmente e 5 concordo totalmente).Ao final do teste, você verá qual área de tecnologia mais combina com você.\n\n")

areas = {
    "Desenvolvimento de Software": [
        "Gosto de programar e resolver problemas com código.",
        "Tenho interesse em criar aplicativos e sites.",
        "Gosto de aprender novas linguagens de programação.",
        "Prefiro trabalhar com lógica e estruturação de código.",
        "Tenho paciência para depurar erros e otimizar código."
    ],
    "Área de Produtos": [
        "Gosto de pensar na experiência do usuário ao usar um sistema.",
        "Tenho interesse em pesquisa de mercado e comportamento do usuário.",
        "Me interesso por criar soluções inovadoras e intuitivas.",
        "Gosto de trabalhar com design, wireframes ou prototipagem.",
        "Quero entender e definir estratégias para melhorar produtos digitais."
    ],
    "Área de Qualidade": [
        "Gosto de testar e garantir que sistemas funcionem corretamente.",
        "Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.",
        "Acredito que testes automatizados ajudam a evitar falhas em sistemas.",
        "Gosto de seguir padrões e documentar processos para garantir qualidade.",
        "Quero trabalhar garantindo que um software funcione bem para todos os usuários."
    ]
}

resultados = {}

for area, perguntas in areas.items():
    print(f"\n{area}:\n")
    resultados[area] = sum(int(input(f"{i + 1}. {pergunta}\n: ")) for i, pergunta in enumerate(perguntas))

melhor_area = max(resultados, key=resultados.get)

print(f"\n\n{nome}, o resultado do seu teste é:\n{melhor_area}\n")
