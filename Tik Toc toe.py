import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to handle the player's move
def handle_move(row, col):
    global board, player, btns
    
    # Check if the move is valid
    if board[row][col] != " ":
        messagebox.showinfo("Invalid Move", "Invalid move. Try again.")
        return
    
    # Make the move
    board[row][col] = player
    
    # Update the button text
    btns[row][col].config(text=player, state=tk.DISABLED)
    
    # Check if the player has won
    if check_winner(board, player):
        messagebox.showinfo("Game Over", player_names[player] + " wins!")
        reset_game()
        return
    
    # Check if it's a tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
        return
    
    # Switch to the other player
    player = "O" if player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, player, btns
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    for i in range(3):
        for j in range(3):
            btns[i][j].config(text=" ", state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe Game")  # Updated title

# Dialog to get player names
player_names = {}
player_names["X"] = simpledialog.askstring("Player Names", "Enter Player 1 Name:")
player_names["O"] = simpledialog.askstring("Player Names", "Enter Player 2 Name:")

# Create the buttons for the Tic-Tac-Toe board
btns = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text=" ", width=10, height=5,
                        command=lambda row=i, col=j: handle_move(row, col))
        btn.grid(row=i, column=j)
        row.append(btn)
    btns.append(row)

# Initialize the game variables
board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

# Start the game
window.mainloop()