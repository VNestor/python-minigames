import tkinter as tk
from random import randrange

# Create tk instance
home_page = tk.Tk()

# Window title
home_page.title("Minigames by Victor Nestor")

# Disable resizing
home_page.resizable(False, False)

# Window sizing and position
window_height = 500
window_width = 500
screen_height = home_page.winfo_screenheight()
screen_width = home_page.winfo_screenwidth()
y_coordinate = int((screen_height/2) - (window_height/2))
x_coordinate = int((screen_width/2) - (window_width/2))

# Set the dimensions and position of window.
home_page.geometry("{}x{}+{}+{}".format(window_width,
                                        window_height, x_coordinate, y_coordinate))

# Grid geometry
# home_page.grid_rowconfigure(0, weight=1)
# home_page.grid_rowconfigure(1, weight=1)
# home_page.grid_rowconfigure(2, weight=1)
# home_page.grid_rowconfigure(3, weight=1)
# home_page.grid_rowconfigure(4, weight=1)
# home_page.grid_rowconfigure(5, weight=1)
# home_page.grid_rowconfigure(6, weight=1)
# home_page.grid_rowconfigure(7, weight=1)
# home_page.grid_rowconfigure(8, weight=1)
# home_page.grid_rowconfigure(9, weight=1)
# home_page.grid_rowconfigure(10, weight=1)
for num in range(0, 8):
    # Create 8 rows
    home_page.grid_rowconfigure(num, weight=1)

# home_page.grid_columnconfigure(0, weight=1)
# home_page.grid_columnconfigure(1, weight=1)
# home_page.grid_columnconfigure(2, weight=1)
# home_page.grid_columnconfigure(3, weight=1)
# home_page.grid_columnconfigure(4, weight=1)

for num in range(0, 5):
    # Create 5 columns
    home_page.grid_columnconfigure(num, weight=1)

# Create labels
home_label = tk.Label(home_page, text="Python Minigames!", font=(30))
first_line_break = tk.Label(
    home_page, text="*" * 75)
game_label = tk.Label(home_page, text="Pick A Game", font=(20))
chosen_label = tk.Label(home_page, text="Game chosen: \n\nNone", font=(20))
second_line_break = tk.Label(
    home_page, text="*" * 75)
third_line_break = tk.Label(
    home_page, text="*" * 75)

# Create buttons

# List of games
game_buttons = []
tic_tac_toe_button = tk.Button(
    home_page, text="Tic-Tac-Toe", command=lambda: set_game(1))
game_buttons.append(tic_tac_toe_button)
rock_paper_scissors_button = tk.Button(
    home_page, text="Rock, Paper, Scissors", command=lambda: set_game(2))
game_buttons.append(rock_paper_scissors_button)
guess_the_number_button = tk.Button(
    home_page, text="Guess The Number", command=lambda: set_game(3))
game_buttons.append(guess_the_number_button)
snake_game_button = tk.Button(
    home_page, text="Snake Game", command=lambda: set_game(4))
game_buttons.append(snake_game_button)

# Start game list
start_game_list = []
start_game_button = tk.Button(home_page, text="Start Game")
start_game_list.append(start_game_button)


# Append labels and buttons to home page
home_label.grid(row=0, column=0, columnspan=5)
first_line_break.grid(row=1, column=0, columnspan=5)
game_label.grid(row=2, column=0, columnspan=5)
second_line_break.grid(row=4, column=0, columnspan=5)
chosen_label.grid(row=5, column=0, columnspan=5)
third_line_break.grid(row=6, column=0, columnspan=5)

# Append game buttons
for row in range(0, 1):
    for col in range(0, 4):
        i = row * 4 + col
        game_buttons[i].grid(row=row+3, column=col+1)

start_game_list[0].grid(row=7, column=0, columnspan=5)


# Setup for selected game

# 0 for none selected
game_selected = 0

print(game_selected)

# Reset all variables


def init():
    global game_buttons, mode_buttons, game_selected, chosen_label
    game_selected = 0
    chosen_label["text"] = "Game chosen: \n\nNone"


def set_game(i):
    global game_buttons, mode_buttons, game_selected
    print(i)
    game_selected = i
    # Check which game is selected
    if game_selected == 1:
        chosen_label["text"] = "Game chosen: \n\nTic-Tac-Toe"
    elif game_selected == 2:
        chosen_label["text"] = "Game chosen: \n\nRock, Paper, Scissors"
    elif game_selected == 3:
        chosen_label["text"] = "Game chosen: \n\nGuess The Number"
    elif game_selected == 4:
        chosen_label["text"] = "Game chosen: \n\nSnake Game"


def start_game(i):
    global game_selected


# Mainloop keeps the program running until closed by the user.
home_page.mainloop()
