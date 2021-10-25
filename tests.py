import unittest

from tictactoe import TicTacGame


class ValidateInputTest(unittest.TestCase):
    def setUp(self):
        self.inputs = ["0", "3 1", "15", "-1.5", "a", "b b", "3"]
        self.labels = [(0),
                       "Должно быть в вводе целое число",
                       "Должно быть число от одного до восьми",
                       "Должно быть в вводе целое число",
                       "Должно быть в вводе целое число",
                       "Должно быть в вводе целое число",
                       "Эта клетка занята"]
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
        self.inputs = ["n", "y", "ds"]
        self.labels = [("n"), ("y"), "Должно быть либо y, либо n:"]
        self.game = TicTacGame()
        self.game.board = [" "] * 9

    def test_result(self):
        for inputs, labels in zip(self.inputs, self.labels):
            try:
                res = self.game.validate_priority(inputs)
            except ValueError as error:
                assert labels == str(error)
            else:
                assert labels == res

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
