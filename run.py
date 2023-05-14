# Function to create the game board
def create_battleship_board(rows, cols):
    board = []
    for i in range(rows):
        board.append(["O"] * cols)
    return board

# Function to randomly place the battleships on the board
def place_ships_on_the_board(board, num_ships):
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] != "S":
            board[row][col] = "S"
            ships_placed += 1    
