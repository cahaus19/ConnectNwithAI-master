import unittest
from unittest.mock import patch
from ConnectNGame.src.players.simple_ai import SimpleAI
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board
from ConnectNGame.src.players.player import Player


class TestSimpleAi(unittest.TestCase):
    def test_simple_ai_add_char_to_win(self):
        board = Board(3, 3, '-', 3)
        capture = PrintCapturer()
        Player('SimpleAi 1', 'W')
        self.name = 'SimpleAi 1'
        self.char = 'W'
        board.game_board = [['-', '-', '-'],
                            ['-', 'W', '9'],
                            ['W', '9', '9']]
        with patch('ConnectNGame.src.board.print', side_effect=capture):
            SimpleAI.take_turn(self, board=board, other_char='9')
            board.generic_print()
            output = ['  0 1 2\n0 - - W\n1 - W 9\n2 W 9 9\n']
            self.assertEqual(output, capture.output)

    def test_simple_ai_to_block(self):
        board = Board(3, 3, '-', 3)
        capture = PrintCapturer()
        Player('SimpleAi 1', 'W')
        self.name = 'SimpleAi 1'
        self.char = 'W'
        board.game_board = [['-', '-', '-'],
                            ['-', 'W', '-'],
                            ['-', '9', '9']]
        with patch('ConnectNGame.src.board.print', side_effect=capture):
            SimpleAI.take_turn(self, board=board, other_char='9')
            board.generic_print()
            output = ['  0 1 2\n0 - - -\n1 - W -\n2 W 9 9\n']
            self.assertEqual(output, capture.output)


if __name__ == '__main__':
    unittest.main()
