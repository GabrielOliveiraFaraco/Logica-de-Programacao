nota = float(input("Digite a nota: "))
prazo = str(input("Foi entrgue no prazo? "))
apresentado = str(input("Foi apresentado? "))

if nota >= 6 and prazo.strip().lower() == "sim" and apresentado.strip().lower() == "sim":
    print("Aprovado no trabalho!")
else:
    print("Não foi aprovado no trabalho!")