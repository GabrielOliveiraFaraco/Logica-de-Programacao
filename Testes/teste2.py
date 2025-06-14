import tkinter as tk
from tkinter import messagebox, simpledialog

my_dict = {}

def cadastrar_aluno():
    nome = entry_nome.get()
    try:
        nota = float(entry_nota.get())
        if nota < 0 or nota > 10:
            messagebox.showerror("Erro", "Nota deve ser entre 0 e 10.")
            return
        if nome.upper() in my_dict:
            messagebox.showinfo("Info", f"Aluno(a) {nome} já cadastrado.")
        else:
            my_dict[nome.upper()] = nota
            messagebox.showinfo("Sucesso", f"Aluno(a) {nome} cadastrado com nota {nota}.")
            atualizar_lista()
    except ValueError:
        messagebox.showerror("Erro", "Nota inválida.")

def atualizar_nota():
    nome = entry_nome.get()
    try:
        nova_nota = float(entry_nota.get())
        if nova_nota < 0 or nova_nota > 10:
            messagebox.showerror("Erro", "Nota deve ser entre 0 e 10.")
            return
        if nome.upper() in my_dict:
            my_dict[nome.upper()] = nova_nota
            messagebox.showinfo("Sucesso", f"Nota do(a) aluno(a) {nome} atualizada para {nova_nota}.")
            atualizar_lista()
        else:
            messagebox.showerror("Erro", f"Aluno(a) {nome} não encontrado.")
    except ValueError:
        messagebox.showerror("Erro", "Nota inválida.")

def remover_aluno():
    nome = entry_nome.get()
    if nome.upper() in my_dict:
        del my_dict[nome.upper()]
        messagebox.showinfo("Sucesso", f"Aluno(a) {nome} removido.")
        atualizar_lista()
    else:
        messagebox.showerror("Erro", f"Aluno(a) {nome} não encontrado.")

def calcular_media():
    if not my_dict:
        messagebox.showinfo("Média", "Nenhum aluno cadastrado.")
        return
    media = sum(my_dict.values()) / len(my_dict)
    messagebox.showinfo("Média", f"Média das notas: {media:.2f}")

def listar_aprovados():
    aprovados = [f"{nome}: {nota}" for nome, nota in my_dict.items() if nota >= 7]
    if not aprovados:
        messagebox.showinfo("Aprovados", "Nenhum aluno aprovado.")
    else:
        messagebox.showinfo("Aprovados", "\n".join(aprovados))

def verificar_aluno():
    nome = entry_nome.get()
    if nome.upper() in my_dict:
        messagebox.showinfo("Encontrado", f"Aluno(a) {nome.upper()} encontrado com nota {my_dict[nome.upper()]}.")
    else:
        messagebox.showinfo("Não encontrado", f"Aluno(a) {nome.upper()} não encontrado.")

def limpar_dicionario():
    my_dict.clear()
    messagebox.showinfo("Limpo", "Dicionário de alunos limpo.")
    atualizar_lista()

def contar_alunos():
    messagebox.showinfo("Total", f"Número total de alunos cadastrados: {len(my_dict)}")

def nomes_alunos():
    if not my_dict:
        messagebox.showinfo("Nomes", "Nenhum aluno cadastrado.")
    else:
        messagebox.showinfo("Nomes", "\n".join(my_dict.keys()))

def nome_nota_alunos():
    if not my_dict:
        messagebox.showinfo("Alunos", "Nenhum aluno cadastrado.")
    else:
        alunos = [f"{nome}: {nota}" for nome, nota in my_dict.items()]
        messagebox.showinfo("Alunos", "\n".join(alunos))

def atualizar_lista():
    listbox.delete(0, tk.END)
    for nome, nota in my_dict.items():
        listbox.insert(tk.END, f"{nome}: {nota}")

# Interface
root = tk.Tk()
root.title("Gerenciamento de Alunos")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Nome do aluno:").grid(row=0, column=0, sticky="e")
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1)

tk.Label(frame, text="Nota:").grid(row=1, column=0, sticky="e")
entry_nota = tk.Entry(frame)
entry_nota.grid(row=1, column=1)

tk.Button(frame, text="Cadastrar", command=cadastrar_aluno).grid(row=2, column=0)
tk.Button(frame, text="Atualizar Nota", command=atualizar_nota).grid(row=2, column=1)
tk.Button(frame, text="Remover", command=remover_aluno).grid(row=2, column=2)
tk.Button(frame, text="Verificar", command=verificar_aluno).grid(row=2, column=3)

tk.Button(frame, text="Calcular Média", command=calcular_media).grid(row=3, column=0)
tk.Button(frame, text="Listar Aprovados", command=listar_aprovados).grid(row=3, column=1)
tk.Button(frame, text="Limpar Tudo", command=limpar_dicionario).grid(row=3, column=2)
tk.Button(frame, text="Contar Alunos", command=contar_alunos).grid(row=3, column=3)

tk.Button(frame, text="Nomes dos Alunos", command=nomes_alunos).grid(row=4, column=0)
tk.Button(frame, text="Nomes e Notas", command=nome_nota_alunos).grid(row=4, column=1)

listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

atualizar_lista()

root.mainloop()