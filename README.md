# Battleships-Game 

 - Ultimate Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

 - This is a simple implementation of the Battleships game in Python. The game allows you to play against the computer by guessing the locations of battleships on a game board.

 - The game board will be generated and the battleships will be placed randomly on the board.

 - The game board is randomly generated and the battleships are placed on the board in random positions.

 - Here is the live version of my project.

## How to Play

1. Run the code in a Python environment.
2. Enter the number of rows for the game board when prompted.
3. Enter the number of columns for the game board when prompted.
4. Enter the number of ships you want to play with when prompted.
5. For each ship, enter the width of the ship when prompted.
6. The game board will be displayed with ships randomly placed on it.
7. The game begins, and you and the computer take turns guessing the locations of each other's battleships.
8. When it's your turn, enter the row and column you want to guess.
9. If your guess hits an opponent's battleship, you will be notified, and the battleship will be marked as sunk on the game board.
10. If your guess misses, you will be notified, and the corresponding position on the game board will be marked as 'X'.
11. The computer will take its turn and follow the same rules.
12. The game continues until either all the battleships are sunk or the maximum number of turns is reached.
13. At the end of the game, the final game board will be displayed along with the game over message.

Have fun playing Battleships!





## Features
-----------------------------------------------------------------------------------------
## Existing Features

- Creating the game board: The create_battleship_board function creates a game board with the specified number of rows and columns.

- Printing the game board: The print_battleship_board function displays the current state of the game board.

- Placing battleships on the board: The place_ships_on_the_board function randomly places battleships on the game board based on the specified number of ships and their widths.

- Checking if a guess is on the board: The is_on_board function checks if the user's guess is within the boundaries of the game board.

- Getting the user's guess: The get_guess_from_player function prompts the user to enter their guess for the row and column.

- Playing the game: The code implements the main game loop where the player and the computer take turns guessing the locations of the battleships. The result of each guess is displayed, and the game ends when all ships have been sunk or the maximum number of turns is reached.

Overall, the code allows users to play a basic version of the Battleships game against the computer.

## Future Features


## Data Model
## Testing 
## Bugs 
### Solved Bugs 

## Remaining Bugs 

- No bugs remaining

## Validator Testing 

- PEP8 -- No errors were returned from PEP8online.com

## Deployment 

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the build backs to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

## Credits 

- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game
- How to play the Battleships game know the information from youtube 
