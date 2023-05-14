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
def place_ships_on_the_board(board, num_ships):
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] != "S":
            board[row][col] = "S"
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

# Set the grid size
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))  

# Create the game board and place the battleships
board = create_battleship_board(rows, cols)
num_ships = min(rows, cols) // 2
place_ships_on_the_board(board, num_ships)


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
    if board[comp_row][comp_col] == "S":
        print("Oh no! The computer sank one of your battleships!")
        board[comp_row][comp_col] = "X"
    else:
        print("Phew! The computer missed your battleship!")
