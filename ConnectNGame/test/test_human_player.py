import unittest
from unittest.mock import patch
from ConnectNGame.src.players.human_player import HumanPlayer
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board
from ConnectNGame.src.players.player import Player


class TestHumanPlayer(unittest.TestCase):

    def test_bad_inputs(self):
        board = Board(3, 3, '-', 3)
        capture = PrintCapturer()
        Player('Harry', 'X')
        board.game_board = [['-', '-', '-'],
                            ['-', '-', '-'],
                            ['-', '-', '-']]


        self.name = 'Harry'
        self.char = 'X'
        col_input = ['Hi', '2']
        with patch('ConnectNGame.src.players.human_player.input', side_effect=col_input):
            with patch('ConnectNGame.src.players.human_player.print', side_effect=capture):
                HumanPlayer.take_turn(self, board = board, other_char='G')
                outputs = ['Harry, column needs to be an integer. Hi is not an integer. \n']
                self.assertEqual(outputs, capture.output)

    def test_more_bad_inputs(self):
        board = Board(3, 3, '-', 3)
        capture = PrintCapturer()
        Player('Harry', 'X')
        board.game_board = [['G', '-', '-'],
                            ['G', '-', '-'],
                            ['X', '-', '-']]

        self.name = 'Harry'
        self.char = 'X'
        col_input = ['3', '0', '2']
        with patch('ConnectNGame.src.players.human_player.input', side_effect=col_input):
            with patch('ConnectNGame.src.players.human_player.print', side_effect=capture):
                HumanPlayer.take_turn(self, board=board, other_char='G')
                outputs = ['Your column needs to be between 0 and 2 but is actually 3.\n',
                           'You cannot play in 0 because it is full.\n']
                self.assertEqual(outputs, capture.output)

    def test_adding_char(self):
        board = Board(3, 3, '-', 3)
        capture = PrintCapturer()
        Player('Harry', 'X')
        board.game_board = [['G', '-', '-'],
                            ['G', '-', '-'],
                            ['X', '-', '-']]

        self.name = 'Harry'
        self.char = 'X'
        col_input = ['1']
        with patch('ConnectNGame.src.players.human_player.input', side_effect=col_input):
            with patch('ConnectNGame.src.board.print', side_effect=capture):
                HumanPlayer.take_turn(self, board=board, other_char='G')
                board.generic_print()
                outputs = ['  0 1 2\n0 G - -\n1 G - -\n2 X X -\n']
                self.assertEqual(outputs, capture.output)


if __name__ == '__main__':
    unittest.main()
