import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [' ']*9
        self.current_player = 'X'
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=' ', width=20, height=10, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        self.window.mainloop()

    def click(self, i, j):
        if self.board[i*3+j] == ' ':
            self.board[i*3+j] = self.current_player
            self.buttons[i][j]['text'] = self.current_player
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.destroy()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.window.destroy()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

TicTacToe()