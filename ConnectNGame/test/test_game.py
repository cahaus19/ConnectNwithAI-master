import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board
from ConnectNGame.src.check_col_win import check_col_win
from ConnectNGame.src.check_row_win import check_row_win
from ConnectNGame.src.check_left_diag_win import check_left_diag_win
from ConnectNGame.src.check_right_diag_win import check_right_diag_win
from ConnectNGame.src.check_tie import check_tie
from ConnectNGame.src.players.human_player import HumanPlayer


class TestGame(unittest.TestCase):

    def test_game_over(self):
        b = Board(3, 3, '-', 3)

        self.board = b

        b.game_board = [['r', '-', '-'],
                        ['r', '-', '-'],
                        ['r', 's', 's']]

        p1 = HumanPlayer('Kim', 's')
        p2 = HumanPlayer('Kanye', 'r')

        self.assertTrue(Game(b, p1, p2))






    def test_row_win(self):
        b = Board(3, 3, '-', 3)
        b.game_board = [['r', '-', '-'],
                       ['r', '-', '-'],
                       ['s', 's', 's']]
        self.assertTrue(check_row_win(b))

    def test_col_win(self):
        b = Board(3, 3, '-', 3)
        b.game_board = [['r', '-', '-'],
                       ['r', '-', '-'],
                       ['r', 's', 's']]
        self.assertTrue(check_col_win(b))

    def test_left_diag_win(self):
        b = Board(3, 3, '-', 3)
        b.game_board = [['-', '-', 'r'],
                        ['s', 'r', 's'],
                        ['r', 's', 's']]
        self.assertTrue(check_left_diag_win(b))

    def test_right_diag_win(self):
        b = Board(3, 3, '-', 3)
        b.game_board = [['s', '-', '-'],
                        ['r', 's', '-'],
                        ['r', 'r', 's']]
        self.assertTrue(check_right_diag_win(b))

    def test_tie(self):
        b = Board(3, 3, '-', 3)
        b.game_board = [['s', 's', 'r'],
                        ['r', 'r', 's'],
                        ['s', 'r', 's']]
        self.assertTrue(check_tie(b))








if __name__ == '__main__':
    unittest.main()
