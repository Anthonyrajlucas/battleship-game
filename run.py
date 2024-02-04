import random

def get_positive_integer_input(prompt):
    """
    Get positive integer input from the user.
    """
    while True:
        try:
            user_input = input(prompt)
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter valid integer coordinates.")

class BattleshipGame:
    def __init__(self, rows, cols, num_ships, ship_widths, input_function):
        self.rows = rows
        self.cols = cols
        self.num_ships = num_ships
        self.ship_widths = ship_widths
        self.board = self.create_battleship_board()
        self.input_function = input_function

    def create_battleship_board(self):
        """
        Create an empty battleship board with specified dimensions.
        """
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("Number of rows and columns must be positive integers.")

        return [['O' for _ in range(self.cols)] for _ in range(self.rows)]        

    def print_battleship_board(self):
        """
        Print the battleship board with legend.
        """
        if self.board.size == 0:
            raise ValueError("Board cannot be empty.")

        print("  " + " ".join(str(i) for i in range(1, self.cols + 1)))
        print(" +" + "-" * (2 * self.cols - 1) + "+")
        for i in range(self.rows):
            print(f"{i + 1}| {' '.join(self.board[i, :])} |")
        print(" +" + "-" * (2 * self.cols - 1) + "+")
        print("Legend:")
        print("O : Represents an empty cell or the ocean")
        print("X : Represents a hit or a sunk battleship")
        print("S : Represents a battleship\n")

    def place_battleships_on_board(self):
        """
        Randomly place battleships on the board.
        """
        if self.num_ships <= 0:
            raise ValueError("Number of ships must be positive.")

        ships_placed = 0
        while ships_placed < self.num_ships:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - self.ship_widths[ships_placed])  # Adjusted col calculation
            ship_fits = True
            for i in range(self.ship_widths[ships_placed]):
                if col + i >= self.cols or self.board[row, col + i] == "S":
                    ship_fits = False
                    break
            if ship_fits:
                for i in range(self.ship_widths[ships_placed]):
                    self.board[row, col + i] = "S"
                ships_placed += 1

    def play_game(self):
        """
        Play the battleships game.
        """
        try:
            turns = self.num_ships * 2

            print("Welcome to Battleships!")
            print("Game Information:")
            print("- In this game, you need to sink all the battleships to win.")
            print("- You have a limited number of turns to guess the positions of the battleships.")
            print("- Each turn, you will enter coordinates to guess where the battleships are.")
            print("Let's begin!\n")

            ships_sunk = 0
            for turn in range(turns):
                print(f"Turn {turn + 1}")
                self.print_battleship_board()
                guess_row = self.input_function("Guess Row:\n")
                guess_col = self.input_function("Guess Col:\n")
                guess_row -= 1
                guess_col -= 1

                if 0 <= guess_row < self.rows and 0 <= guess_col < self.cols:
                    if self.board[guess_row, guess_col] == "S":
                        print("Congratulations! You sank my battleship!")
                        self.board[guess_row, guess_col] = "X"
                        ships_sunk += 1
                        if ships_sunk == self.num_ships:
                            print("Congratulations! You sank all the battleships!")
                            break
                    elif self.board[guess_row, guess_col] == "X":
                        print("You guessed that one already.")
                    else:
                        print("You missed my battleship!")
                        self.board[guess_row, guess_col] = "X"
                else:
                    print("Oops, that's not even in the ocean. Please enter valid coordinates.")

            if ships_sunk < self.num_ships:
                print("Game Over. You ran out of turns.")
                print("The remaining battleships were at the following positions:")
                self.print_battleship_board()
        except ValueError as ve:
            print(f"Error: {ve}")

def main():
    """
    Main function to start the game.
    """
    try:
        print("Welcome to Battleships!")
        print("Game Information:")
        print("- In this game, you need to sink all the battleships to win.")
        print("- You have a limited number of turns to guess the positions of the battleships.")
        print("- Each turn, you will enter coordinates to guess where the battleships are.")
        print("Let's set up the game parameters.\n")

        # Proceed with the game setup
        rows = get_positive_integer_input("Enter the number of rows (maximum 20):\n")
        while rows > 20:
            print("Error: The number of rows cannot exceed 20.")
            rows = get_positive_integer_input("Please enter the number of rows (maximum 20):\n")

        cols = get_positive_integer_input("Enter the number of columns (maximum 20):\n")
        while cols > 20:
            print("Error: The number of columns cannot exceed 20.")
            cols = get_positive_integer_input("Please enter the number of columns (maximum 20):\n")

        num_ships = get_positive_integer_input("Enter the number of ships (maximum 5):\n")
        while num_ships > 5:
            print("Error: The number of ships cannot exceed 5.")
            num_ships = get_positive_integer_input("Please enter the number of ships (maximum 5):\n")

        ship_widths = []
        for i in range(num_ships):
            width = get_positive_integer_input(f"Enter the width for ship {i + 1}:\n")
            while width > cols:
                print(f"Ship width cannot exceed the number of columns ({cols}).")
                width = get_positive_integer_input(f"Enter the width for ship {i + 1}:\n")
            ship_widths.append(width)

        game = BattleshipGame(rows, cols, num_ships, ship_widths, get_positive_integer_input)
        game.place_battleships_on_board()
        game.play_game()
    except KeyboardInterrupt:
        print("\n Game aborted by the user.")

if __name__ == "__main__":
    main()
