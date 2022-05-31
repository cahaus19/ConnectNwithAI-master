import sys
from ConnectNGame.src.check_col_win import check_col_win
from ConnectNGame.src.check_row_win import check_row_win
from ConnectNGame.src.check_left_diag_win import check_left_diag_win
from ConnectNGame.src.check_right_diag_win import check_right_diag_win
from ConnectNGame.src.check_tie import check_tie


class Game(object):
    game_over = False

    def __init__(self, board: object, p1: object,  p2: object) -> None:  # type: ignore
        self.game_over = False
        self.active_player_index = 0
        self.player_list = [p1, p2]
        self.board = board

    def check_if_game_over(self) -> bool:

        row_win = check_row_win(self.board)
        col_win = check_col_win(self.board)
        left_diag_win = check_left_diag_win(self.board)
        right_diag_win = check_right_diag_win(self.board)
        tie = check_tie(self.board)

        if any([row_win, col_win, left_diag_win, right_diag_win]):
            self.game_over = True
            print(self.board)
            return self.game_over

        elif tie:
            self.game_over = True
            print(self.board)
            print('Tie Game.')
            sys.exit()

        return self.game_over
