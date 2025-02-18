# bootcamp-Exercise-Design-Your-Own-Treasure-Hunt-Game


Background You're tasked with creating a simple board game. In this game, players are treasure hunters, and they need a board to visualize where they might find hidden treasures. Your job is to create this board and allow players to place the treasure at a location of their choice.

Objectives Board Creation: Create a grid or board of size n x m, where n represents the number of rows and m represents the number of columns. The board should be filled with asterisks (*), which symbolize empty spaces. Player Interaction: Prompt the user (player) to specify a location (row and column) to hide the treasure.

Board Display: Using nested loops, construct and display the game board. Use an asterisk (*) for empty cells and a T for the cell with the treasure.

Requirements The program should start by asking the player to specify the size of the board by entering the number of rows (n) and columns (m). After creating the board, prompt the player to specify where they want to hide the treasure. Make sure they provide a valid row and column number. Handle potential input errors gracefully. For example, if the user tries to place the treasure outside the board's dimensions, display an error message and ask them to enter a valid location.

Bonus Challenge Add a Trap: Randomly place a trap (X) on the board in addition to the treasure. Ensure that the trap does not overlap with the treasure. Player Guess: Ask the player to guess the location of the treasure. If they find it, display a winning message. If they land on the trap, display a message that they've been trapped. Otherwise, inform them to try again.

Tips

Utilize nested loops for constructing the game board.
Integrate conditional statements to determine the content to display in each cell of the board.
