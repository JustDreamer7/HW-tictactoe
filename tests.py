import unittest

from tictactoe import TicTacGame


class ValidateInputTest(unittest.TestCase):
    def setUp(self):
        self.inputs = ["0", "3 1", "15", "-1.5", "a", "b b", "3"]
        self.labels = [(0),
                       "There should be one number",
                       "Cell index should be [0-8]",
                       "Cell index should be int",
                       "Cell index should be int",
                       "There should be one number",
                       "Cell is busy"]
        self.game = TicTacGame()
        self.game.board = [" "] * 9
        self.game.board[3] = "X"

    def test_result(self):
        for inputs, labels in zip(self.inputs, self.labels):
            try:
                res = self.game.validate_input(inputs)
            except (ValueError, IndexError) as error:
                assert labels == str(error)
            else:
                assert labels == res

    def tearDown(self):
        pass


class ValidatePriority(unittest.TestCase):
    def setUp(self):
        self.inputs = ["a", "0", "y", "n"]
        self.game = TicTacGame()
        self.labels = ["There should be y or n",
                       "There should be y or n",
                       (0),
                       (0)]

    def test_result(self):
        for inputs, labels in zip(self.inputs, self.labels):
            try:
                res = self.game.validate_priority(inputs)
            except (ValueError) as error:
                assert labels == str(error)
            else:
                assert labels == res

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
