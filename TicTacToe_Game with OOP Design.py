import os
import random
import oxo_data


class Game:
    def __init__(self):
        """Initialize a new empty game board."""
        self.board = [" "] * 9

    def new_game(self):
        """Reset the game board to start a new game."""
        self.board = [" "] * 9

    def save_game(self):
        """Save the current game board."""
        oxo_data.saveGame(self.board)

    def restore_game(self):
        """Restore the game board from a saved state."""
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
            else:
                self.new_game()
        except IOError:
            self.new_game()

    def _generate_move(self):
        """Generate a random move from available cells."""
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def _is_winning_move(self):
        """Check if the current board has a winning line."""
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == "XXX" or chars == "OOO":
                return True
        return False

    def user_move(self, cell):
        """Make a move for the user ('X') and check for win."""
        if self.board[cell] != " ":
            raise ValueError("Invalid cell")
        self.board[cell] = "X"
        return "X" if self._is_winning_move() else ""

    def computer_move(self):
        """Make a move for the computer ('O') and check for win or draw."""
        cell = self._generate_move()
        if cell == -1:
            return "D"  # Draw
        self.board[cell] = "O"
        return "O" if self._is_winning_move() else ""

    def display_board(self):
        """Display the board for debugging purposes."""
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print(" | ".join(row))
        print("\n")


# Test run
if __name__ == "__main__":
    game = Game()
    game.display_board()

    result = ""
    while not result:
        try:
            result = game.user_move(game._generate_move())
        except ValueError:
            print("Oops, that shouldn't happen")

        if not result:
            result = game.computer_move()

        if result == "D":
            print("It's a draw!")
        elif result:
            print(f"Winner is: {result}")

        game.display_board()
