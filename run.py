# Function to create the game board
def create_battleship_board(rows, cols):
    board = []
    for i in range(rows):
        board.append(["O"] * cols)
    return board
