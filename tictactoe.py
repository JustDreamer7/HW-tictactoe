
class TicTacGame:
    """TicTacGame class"""
    def __init__(self):
        self.board = [" "] * 9

    def start_game(self):
        """Logic of the game, literally main function"""
        computer, dermal_bag = self.priority()
        turn = "X"
        self.show_board()
        while not self.check_winner():
            if turn == dermal_bag:
                move = self.dermal_bag_move()
                self.board[move] = dermal_bag
            else:
                move = self.computer_move(computer, dermal_bag)
                self.board[move] = computer
            self.show_board()
            turn = self.next_turn(turn)
        result = self.check_winner()
        self.game_result(result, computer)

    def show_board(self):
        """Showing Board"""
        print("-------------")
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")
            print("-------------")

    @staticmethod
    def ask_player(question):
        """Inputs"""
        get_smooth = input(question)
        return get_smooth

    def priority(self):
        """Choosing first turn"""
        go_first = self.ask_player("Хочешь ходить первым? (y/n):")
        first_pl = self.validate_priority(go_first)
        if first_pl == "y":
            print("Играешь крестиками")
            dermal_bag = "X"
            computer = "O"
        else:
            print("Играешь ноликами")
            dermal_bag = "O"
            computer = "X"
        return computer, dermal_bag

    @staticmethod
    def validate_priority(queue):
        """Validate input of priority turn"""
        if queue not in ("y", "n"):
            raise ValueError("Должно быть либо y, либо n:")
        return queue

    def validate_input(self, move):
        """Validate inputs, raise errors"""
        if not move.isdigit():
            raise ValueError("Должно быть в вводе целое число")
        if int(move) < 0 or int(move) > 9:
            raise IndexError("Должно быть число от одного до восьми")
        if self.board[int(move)] != ' ':
            raise ValueError("Эта клетка занята")
        return int(move)

    def check_winner(self):
        """Checking winning turns"""
        win_ways = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for row in win_ways:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != " ":
                winner = self.board[row[0]]
                return winner
        if " " not in self.board:
            return "Ничья"
        return None

    def dermal_bag_move(self):
        """ Function of human turn """

        move = self.ask_player("Ваш ход. Введите число в диапазоне [0-8]:")
        human_move = self.validate_input(move)
        print("Ты проиграешь...")
        print(human_move)
        return human_move

    def computer_move(self, computer, dermal_bag):
        """Function of computer turn, computer makes the best moves and can prevent your winning turn"""

        board = self.board[:]
        random_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)

        for move in [i for i, v in enumerate(board) if v == ' ']:
            board[move] = computer
            if self.check_winner() == computer:
                print(move)
                return move
            board[move] = " "
        for move in [i for i, v in enumerate(board) if v == ' ']:
            board[move] = dermal_bag
            if self.check_winner() == dermal_bag:
                print(move)
                return move
            board[move] = " "
        for move in random_moves:
            if move in [i for i, v in enumerate(board) if v == ' ']:
                print(move)
                return move

    @staticmethod
    def next_turn(turn):
        """Function of changing mark"""
        if turn == "X":
            return "O"
        else:
            return "X"

    @staticmethod
    def game_result(result, computer):
        """Function which print result"""
        if result != "Ничья":
            if result == computer:
                print("Победил компьютер!")
            else:
                print("Вы победили!")
        else:
            print("Ничья\n")


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
