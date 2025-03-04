import unittest
from oxo_logic import newGame, userMove, computerMove, saveGame, restoreGame  # Importing functions

class TestOxoGame(unittest.TestCase):

    def test_new_game(self):
        """Test if newGame() creates an empty game board."""
        game = newGame()
        self.assertEqual(game, [' '] * 9)  # Board should be 9 empty spaces

    def test_user_move_valid(self):
        """Test if a valid user move works."""
        game = newGame()
        result = userMove(game, 0)  # User makes a move in cell 0
        self.assertEqual(game[0], 'X')  # Cell 0 should now have 'X'
        self.assertEqual(result, '')  # No winner yet

    def test_user_move_invalid(self):
        """Test if an invalid move raises an error."""
        game = newGame()
        userMove(game, 0)  # User makes a valid move in cell 0
        with self.assertRaises(ValueError):
            userMove(game, 0)  # Trying to play in the same cell should raise an error

    def test_computer_move(self):
        """Test if the computer makes a valid move."""
        game = newGame()
        result = computerMove(game)
        self.assertIn('O', game)  # 'O' should appear somewhere on the board
        self.assertIn(result, ['', 'O', 'D'])  # No winner, or computer wins, or draw

    def test_draw(self):
        """Test if the game identifies a draw."""
        game = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']  # Full board, no winner
        result = computerMove(game)
        self.assertEqual(result, 'D')  # Should be a draw

    def test_save_and_restore_game(self):
        """Test saving and restoring game state."""
        game = ['X', 'O', 'X', ' ', 'O', ' ', 'X', ' ', 'O']
        saveGame(game)  # Saving the game state
        restored_game = restoreGame()  # Restoring the game state
        self.assertEqual(game, restored_game)  # Restored game should match saved game

if __name__ == '__main__':
    unittest.main(verbosity=2)  # Verbose mode activated!
