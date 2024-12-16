import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    for row in board:
        if " " in row:
            return None

    return "Tie"

def on_click(row, col):
    global current_player
    if board[row][col] == " " and not game_over:
        board[row][col] = players[current_player]
        buttons[row][col].config(text=players[current_player])
        result = check_winner(board)
        if result:
            end_game(result)
        else:
            switch_player()

def switch_player():
    global current_player
    current_player = 1 - current_player

def end_game(result):
    global game_over
    game_over = True
    if result == "Tie":
        messagebox.showinfo("Game Over", "It's a tie!")
    else:
        messagebox.showinfo("Game Over", f"Player {result} wins!")
    root.quit()

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

players = ["X", "O"]
current_player = 0
game_over = False

board = [[" " for _ in range(3)] for _ in range(3)]
buttons = []

for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2, 
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
