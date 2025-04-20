import random
import tkinter as tk
from tkinter import messagebox

# Constantes
BUTTON_WIDTH = 3
BUTTON_HEIGHT = 1
BUTTON_PADDING = 1
WINDOW_SIZE = "500x500"
WINDOW_BG_COLOR = "lightblue"
GAME_TITLE = "Campo Minado"
TUTORIAL_TEXT = "Clique em uma célula para revelar. Evite as minas!"

def create_board(size, num_mines):
    """Cria o tabuleiro e posiciona as minas."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()
    while len(mines) < num_mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        mines.add((x, y))
    for x, y in mines:
        board[x][y] = 'M'
    return board, mines

def count_adjacent_mines(board, x, y):
    """Conta o número de minas adjacentes a uma célula."""
    size = len(board)
    return sum(
        1 for dx in [-1, 0, 1] for dy in [-1, 0, 1]
        if 0 <= x + dx < size and 0 <= y + dy < size and board[x + dx][y + dy] == 'M'
    )

def reveal(board, revealed, x, y):
    """Revela uma célula e suas adjacências se não houver minas próximas."""
    if revealed[x][y]:
        return
    revealed[x][y] = True
    if board[x][y] == 'M':
        return
    count = count_adjacent_mines(board, x, y)
    board[x][y] = str(count)
    if count == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board):
                    reveal(board, revealed, nx, ny)

class MinesweeperGame:
    def __init__(self, root, size, num_mines):
        self.root = root
        self.size = size
        self.num_mines = num_mines
        self.board, self.mines = create_board(size, num_mines)
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.create_widgets()

    def create_widgets(self):
        """Cria os botões do tabuleiro e exibe o título e tutorial."""
        # Título do jogo
        title_label = tk.Label(self.root, text=GAME_TITLE, font=("Arial", 16, "bold"), bg=WINDOW_BG_COLOR)
        title_label.pack(pady=10)

        # Texto tutorial
        tutorial_label = tk.Label(self.root, text=TUTORIAL_TEXT, font=("Arial", 10), bg=WINDOW_BG_COLOR)
        tutorial_label.pack(pady=5)

        # Tabuleiro de botões
        frame = tk.Frame(self.root, bg=WINDOW_BG_COLOR)
        frame.pack(expand=True)
        for i in range(self.size):
            for j in range(self.size):
                btn = tk.Button(
                    frame, text='', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                    command=lambda x=i, y=j: self.on_click(x, y)
                )
                btn.grid(row=i, column=j, padx=BUTTON_PADDING, pady=BUTTON_PADDING)
                self.buttons[i][j] = btn

    def on_click(self, x, y):
        """Lida com o clique em uma célula."""
        if (x, y) in self.mines:
            self.reveal_all_mines()
            messagebox.showinfo("Game Over", "Você acertou uma mina!")
            self.root.quit()
        else:
            reveal(self.board, self.revealed, x, y)
            self.update_buttons()
            if self.check_victory():
                messagebox.showinfo("Parabéns", "Você venceu!")
                self.root.quit()

    def update_buttons(self):
        """Atualiza o estado dos botões com base no tabuleiro revelado."""
        for i in range(self.size):
            for j in range(self.size):
                if self.revealed[i][j]:
                    self.buttons[i][j].config(text=self.board[i][j], state='disabled')

    def reveal_all_mines(self):
        """Revela todas as minas no tabuleiro."""
        for x, y in self.mines:
            self.buttons[x][y].config(text='M', bg='red')

    def check_victory(self):
        """Verifica se o jogador venceu o jogo."""
        return all(
            self.revealed[i][j] or self.board[i][j] == 'M'
            for i in range(self.size) for j in range(self.size)
        )

def main():
    """Função principal para iniciar o jogo."""
    root = tk.Tk()
    root.title("Minesweeper")
    root.geometry(WINDOW_SIZE)
    root.configure(bg=WINDOW_BG_COLOR)
    MinesweeperGame(root, size=10, num_mines=20)
    root.mainloop()

if __name__ == "__main__":
    main()