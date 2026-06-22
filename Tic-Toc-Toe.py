import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Button grid
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_draw():
    return all(all(cell != "" for cell in row) for row in board)

def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"🎉 Player {winner} wins!")
            reset_board()
            return
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# UI layout
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=('Arial', 24), width=5, height=2,
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Restart button
restart_button = tk.Button(root, text="Restart", font=('Arial', 16), bg="lightblue",
                           command=reset_board)
restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=10)

# Start GUI loop
root.mainloop()