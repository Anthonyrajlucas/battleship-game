import random

# Function to create the game board
def create_battleship_board(rows, cols):
    board = []
    for i in range(rows):
        board.append(["O"] * cols)
    return board

# Function to print the game board
def print_battleship_board(board):
    for row in board:
        print(" ".join(row))

# Function to randomly place the battleships on the board
def place_ships_on_the_board(board, num_ships, ship_widths):
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - ship_widths[ships_placed])
        for i in range(ship_widths[ships_placed]):
            if board[row][col + i] == "S":
                break
        else:
            for i in range(ship_widths[ships_placed]):
                board[row][col + i] = "S"
            ships_placed += 1

# Function to check if a guess is on the board
def is_on_board(guess_row, guess_col, rows, cols):
    return guess_row >= 0 and guess_row < rows and \
           guess_col >= 0 and guess_col < cols

# Function to get the user's guess
def get_guess_from_player(rows, cols):
    while True:
        guess_row = int(input("Guess Row: ")) - 1
        guess_col = int(input("Guess Col: ")) - 1
        if is_on_board(guess_row, guess_col, rows, cols):
            return guess_row, guess_col
        else:
            print("Oops, that's not even in the ocean.")

# Set the grid size and ship widths
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
num_ships = int(input("Enter the number of ships: "))

ship_widths = []
for i in range(num_ships):
    width = int(input("Enter the width for ship {}: ".format(i + 1)))
    ship_widths.append(width)

# Create the game board and place the battleships
board = create_battleship_board(rows, cols)
place_ships_on_the_board(board, num_ships, ship_widths)

# Play the game
turns = num_ships * 2
print("Let's play Battleships!")
for turn in range(turns):
    print("Turn", turn + 1)
    print_battleship_board(board)
    guess_row, guess_col = get_guess_from_player(rows, cols)

    if board[guess_row][guess_col] == "S":
        print("Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "X"
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"

    if turn == turns - 1:
        print("Game Over")
        print_battleship_board(board)
        break

    computer_row = random.randint(0, rows - 1)
    computer_col = random.randint(0, cols - 1)
    if board[computer_row][computer_col] == "S":
        print("Oh no! The computer sank one of your battleships!")
        board[computer_row][computer_col] = "X"
    else:
        print("Phew! The computer missed your battleship!")