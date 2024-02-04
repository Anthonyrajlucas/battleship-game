import random

def create_battleship_board(rows, cols):
    board = []
    for _ in range(rows):
        board.append(["O"] * cols)
    return board

def print_battleship_board(board):
    print("Legend:")
    print("O : Empty space")
    print("X : Part of ship that was hit")
    print("S : Empty location hit\n")
    for row in board:
        print(" ".join(row))

def place_battleships_on_board(board, num_ships, ship_widths):
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - ship_widths[ships_placed])  # Adjusted col calculation
        ship_fits = True
        for i in range(ship_widths[ships_placed]):
            if col + i >= len(board[0]) or board[row][col + i] == "S":
                ship_fits = False
                break
        if ship_fits:
            for i in range(ship_widths[ships_placed]):
                board[row][col + i] = "S"
            ships_placed += 1


def is_on_board(guess_row, guess_col, rows, cols):
    return 0 <= guess_row < rows and 0 <= guess_col < cols

def get_guess_from_player(rows, cols):
    while True:
        try:
            guess_row = int(input("Guess Row:\n"))
            guess_col = int(input("Guess Col:\n"))
            if is_on_board(guess_row - 1, guess_col - 1, rows, cols):
                return guess_row - 1, guess_col - 1
            else:
                print("Oops, that's not even in the ocean. Please enter valid coordinates.")
        except ValueError:
            print("Invalid input. Please enter valid integer coordinates.")

def get_positive_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        else:
            print("Please enter a positive integer.")

def play_battleships(rows, cols, num_ships, ship_widths):
    board = create_battleship_board(rows, cols)
    place_battleships_on_board(board, num_ships, ship_widths)
    turns = num_ships * 2

    print("Welcome to Battleships!")
    print("In this game, you need to sink all the battleships to win.")
    print("You have a limited number of turns to guess the positions of the battleships.")
    print("Each turn, you will enter coordinates to guess where the battleships are.")
    print("Let's begin!\n")
    
    ships_sunk = 0
    for turn in range(turns):
        print(f"Turn {turn + 1}")
        print_battleship_board(board)
        guess_row, guess_col = get_guess_from_player(rows, cols)

        if board[guess_row][guess_col] == "S":
            print("Congratulations! You sank my battleship!")
            board[guess_row][guess_col] = "X"
            ships_sunk += 1
            if ships_sunk == num_ships:
                print("Congratulations! You sank all the battleships!")
                break
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

    if ships_sunk < num_ships:
        print("Game Over. You ran out of turns.")
        print("The remaining battleships were at the following positions:")
        print_battleship_board(board)

def main():
    rows = get_positive_integer_input("Enter the number of rows:\n")
    cols = get_positive_integer_input("Enter the number of columns:\n")
    num_ships = get_positive_integer_input("Enter the number of ships:\n")

    ship_widths = []
    for i in range(num_ships):
        width = get_positive_integer_input(f"Enter the width for ship {i + 1}:\n")
        while width > cols:
            print(f"Ship width cannot exceed the number of columns ({cols}).")
            width = get_positive_integer_input(f"Enter the width for ship {i + 1}:\n")
        ship_widths.append(width)

    play_battleships(rows, cols, num_ships, ship_widths)

if __name__ == "__main__":
    main()
