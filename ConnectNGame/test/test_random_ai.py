import unittest
from unittest.mock import patch
from ConnectNGame.src.board import Board
from ConnectNGame.src.players.player import Player
from .print_capturer import PrintCapturer
from ConnectNGame.src.players.random_ai import RandomAi


class TestRandomAi(unittest.TestCase):

    def test_random_ai_add_char(self):
        board = Board(2, 2, '-', 2)
        capture = PrintCapturer()
        Player('RandomAi 1', '?')
        self.name = 'RandomAi 1'
        self.char = '?'
        board.game_board = [['B', '-'],
                            ['?', '-']]

        with patch('ConnectNGame.src.board.print', side_effect=capture):
            RandomAi.take_turn(self, board=board, other_char='B')
            board.generic_print()
            output = ['  0 1\n0 B -\n1 ? ?\n']
            self.assertEqual(output, capture.output)


if __name__ == '__main__':
    unittest.main()
