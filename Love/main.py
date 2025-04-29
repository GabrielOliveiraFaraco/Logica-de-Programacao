nome = str(input("Nome: "))

def resposta(pergunta):
    while True:
        try:
            resposta = int(input(pergunta))
            if resposta <= 1 or resposta >= 5:
                print("Por favor, responda com um dígito de 1 a 5.")
            else:
                return resposta
        except ValueError:
            print("Valor inválido! Tente novamente.")

print(f"Olá {nome}, seja bem-vindo(a)!\nPara continuar, responda as perguntas com um dígito de 1 a 5 (sendo 1 discordo totalmente e 5 concordo totalmente).Ao final do teste, você verá qual área de tecnologia mais combina com você.\n\n")

pergunta1 = resposta("1. Gosto de programar e resolver problemas com código.\n: ")
pergunta2 = resposta("2. Tenho interesse em criar aplicativos e sites.\n: ")
pergunta3 = resposta("3. Gosto de aprender novas linguagens de programação.\n: ")
pergunta4 = resposta("4. Prefiro trabalhar com lógica e estruturação de código.\n: ")
pergunta5 = resposta("5. Tenho paciência para depurar erros e otimizar código.\n: ")

resultado1 = (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5)

pergunta6 = resposta("6. Gosto de pensar na experiência do usuário ao usar um sistema.\n: ")
pergunta7 = resposta("7. Tenho interesse em pesquisa de mercado e comportamento do usuário.\n: ")
pergunta8 = resposta("8. Me interesso por criar soluções inovadoras e intuitivas.\n: ")
pergunta9 = resposta("9. Gosto de trabalhar com design, wireframes ou prototipagem.\n: ")
pergunta10 = resposta("10. Quero entender e definir estratégias para melhorar produtos digitais.\n: ")

resultado2 = (pergunta6 + pergunta7 + pergunta8 + pergunta9 + pergunta10)

pergunta11 = resposta("11. Gosto de testar e garantir que sistemas funcionem corretamente.\n: ")
pergunta12 = resposta("12. Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.\n: ")
pergunta13 = resposta("13. Acredito que testes automatizados ajudam a evitar falhas em sistemas.\n: ")
pergunta14 = resposta("14. Gosto de seguir padrões e documentar processos para garantir qualidade.\n: ")
pergunta15 = resposta("15. Quero trabalhar garantindo que um software funcione bem para todos os usuários.\n: ")

resultado3 = (pergunta11 + pergunta12 + pergunta13 + pergunta14 + pergunta15)

total = max(resultado1, resultado2, resultado3)

print(f"\n\n{nome}, o resultado do seu teste é:\n")

if resultado1 == total:
    print("Desenvolvimento de Software")
if resultado2 == total:
    print("Área de Produtos")
if resultado3 == total:
    print("Área de Qualidade\n")