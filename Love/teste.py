nome = str(input("Nome: "))

print(f"Olá {nome}, seja bem-vindo(a)!\nPara continuar, responda as perguntas com um dígito de 1 a 5 (sendo 1 discordo totalmente e 5 concordo totalmente).Ao final do teste, você verá qual área de tecnologia mais combina com você.\n\n")

pergunta1 = int(input("1. Gosto de programar e resolver problemas com código.\n: "))
pergunta2 = int(input("2. Tenho interesse em criar aplicativos e sites.\n: "))
pergunta3 = int(input("3. Gosto de aprender novas linguagens de programação.\n: "))
pergunta4 = int(input("4. Prefiro trabalhar com lógica e estruturação de código.\n: "))
pergunta5 = int(input("5. Tenho paciência para depurar erros e otimizar código.\n: "))

resultado1 = (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5)

pergunta6 = int(input("6. Gosto de pensar na experiência do usuário ao usar um sistema.\n: "))
pergunta7 = int(input("7. Tenho interesse em pesquisa de mercado e comportamento do usuário.\n: "))
pergunta8 = int(input("8. Me interesso por criar soluções inovadoras e intuitivas.\n: "))
pergunta9 = int(input("9. Gosto de trabalhar com design, wireframes ou prototipagem.\n: "))
pergunta10 = int(input("10. Quero entender e definir estratégias para melhorar produtos digitais.\n: "))

resultado2 = (pergunta6 + pergunta7 + pergunta8 + pergunta9 + pergunta10)

pergunta11 = int(input("11. Gosto de testar e garantir que sistemas funcionem corretamente.\n: "))
pergunta12 = int(input("12. Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.\n: "))
pergunta13 = int(input("13. Acredito que testes automatizados ajudam a evitar falhas em sistemas.\n: "))
pergunta14 = int(input("14. Gosto de seguir padrões e documentar processos para garantir qualidade.\n: "))
pergunta15 = int(input("15. Quero trabalhar garantindo que um software funcione bem para todos os usuários.\n: "))

resultado3 = (pergunta11 + pergunta12 + pergunta13 + pergunta14 + pergunta15)

total = max(resultado1, resultado2, resultado3)

print(type(total))