import tkinter as tk

def set_tile(row, column):
    global current_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player
    moves[current_player].append((row, column))

    # Check if the current player has made 4 moves
    if len(moves[current_player]) > 3:
        # Remove the first move and reset that tile
        first_move = moves[current_player].pop(0)
        board[first_move[0]][first_move[1]]["text"] = ""
        board[first_move[0]][first_move[1]].config(foreground=color_blue)

    # Highlight the move that will disappear
    if len(moves[current_player]) >= 3:
        first_move = moves[current_player][0]
        board[first_move[0]][first_move[1]].config(foreground=color_warning)

    # Switch players
    if current_player == playerX:
        current_player = playerO
    else:
        current_player = playerX

    label["text"] = current_player + "'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_red)
            for column in range(3):
                board[row][column].config(foreground=color_red, background=color_background_hovered)
            game_over = True
            return
    
    # Vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_red)
            for row in range(3):
                board[row][column].config(foreground=color_red, background=color_background_hovered)
            game_over = True
            return
    
    # Diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_red)
        for i in range(3):
            board[i][i].config(foreground=color_red, background=color_background_hovered)
        game_over = True
        return

    # Anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_red)
        board[0][2].config(foreground=color_red, background=color_background_hovered)
        board[1][1].config(foreground=color_red, background=color_background_hovered)
        board[2][0].config(foreground=color_red, background=color_background_hovered)
        game_over = True
        return

def restart():
    global turns, game_over, current_player, moves

    turns = 0
    game_over = False
    current_player = playerX
    moves = {playerX: [], playerO: []}

    label.config(text=current_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_background)

rows = 3
columns = 3

playerX = "X"
playerO = "O"

current_player = playerX

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Colors
color_red = "#f44336"
color_blue = "#4237DB"
color_warning = "#201b6d"
color_yellow = "#ffde57"
color_background = "#171719"
color_background_hovered = "#262323"

turns = 0
game_over = False
moves = {playerX: [], playerO: []}

window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=current_player + "'s turn", font=("Consolas", 20), background=color_background,
                  foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(rows):
    for column in range(columns):
        board[row][column] = tk.Button(frame, text="", font=("Consolas", 50, "bold"),
                                       background=color_background, foreground=color_blue, width=4, height=1,
                                       command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tk.Button(frame, text="new game", font=("Consolas", 20),
                   command=restart)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_height / 2))
window_y = int((screen_height / 2) - (window_width / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()