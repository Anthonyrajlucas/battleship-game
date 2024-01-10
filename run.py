import random

class BattleshipGame:
    def __init__(self, rows, cols, num_ships):
        self.rows = rows
        self.cols = cols
        self.num_ships = num_ships
        self.board = [["O"] * cols for _ in range(rows)]
        self.ship_widths = []

    def add_ship_widths(self, ship_widths):
        self.ship_widths = ship_widths
        self.place_ships()

    def place_ships(self):
        ships_placed = 0
        while ships_placed < self.num_ships:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - self.ship_widths[ships_placed])
            if all(self.board[row][col + i] != "S" for i in range(self.ship_widths[ships_placed])):
                for i in range(self.ship_widths[ships_placed]):
                    self.board[row][col + i] = "S"
                ships_placed += 1

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def is_on_board(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def make_guess(self, row, col):
        if not self.is_on_board(row, col):
            print("Oops, that's not even in the ocean.")
            return False
        elif self.board[row][col] == "S":
            print("Congratulations! You sank my battleship!")
            self.board[row][col] = "X"
            return True
        elif self.board[row][col] == "X":
            print("You guessed that one already.")
            return False
        else:
            print("You missed my battleship!")
            self.board[row][col] = "X"
            return False

def get_input(prompt, cast_type=int, condition=lambda x: True):
    while True:
        try:
            value = cast_type(input(prompt))
            if condition(value):
                return value
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid number.")

def main():
    rows = get_input("Enter the number of rows:\n", condition=lambda x: x > 0)
    cols = get_input("Enter the number of columns:\n", condition=lambda x: x > 0)
    num_ships = get_input("Enter the number of ships:\n", condition=lambda x: x > 0 and x <= rows * cols)

    game = BattleshipGame(rows, cols, num_ships)

    ship_widths = []
    for i in range(num_ships):
        width = get_input(f"Enter the width for ship {i + 1}:\n", condition=lambda x: x > 0 and x <= cols)
        ship_widths.append(width)

    game.add_ship_widths(ship_widths)

    turns = num_ships * 2
    print("Let's play Battleships!")
    for turn in range(turns):
        print(f"Turn {turn + 1}")
        game.print_board()

        guess_row = get_input("Guess Row:\n", condition=lambda x: 1 <= x <= rows) - 1
        guess_col = get_input("Guess Col:\n", condition=lambda x: 1 <= x <= cols) - 1
        if game.make_guess(guess_row, guess_col):
            break

        if turn == turns - 1:
            print("Game Over")
            game.print_board()

if __name__ == "__main__":
    main()
