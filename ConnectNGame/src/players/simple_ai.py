import random
import copy
from ConnectNGame.src.players.player import Player
from ConnectNGame.src.check_col_win import check_col_win
from ConnectNGame.src.check_row_win import check_row_win
from ConnectNGame.src.check_left_diag_win import check_left_diag_win
from ConnectNGame.src.check_right_diag_win import check_right_diag_win


class SimpleAI(Player):

    def take_turn(self, board, other_char: str) -> None:
        total = board.num_col
        winning_ai_move: int = 'N'
        blocking_win_move = 'N'
        options = range(total)
        top_row = 0
        possible_choice = []
        # takes out full columns
        for col in options:
            if board.game_board[top_row][col] == board.blank_char:
                possible_choice.append(col)
        # finds if there's a winning move
        for i in possible_choice:
            copy_board = copy.deepcopy(board)
            copy_board.add_new_char(i, board.blank_char, self.char)
            row_win = check_row_win(copy_board)
            col_win = check_col_win(copy_board)
            left_diag_win = check_left_diag_win(copy_board)
            right_diag_win = check_right_diag_win(copy_board)
            if any([row_win, col_win, left_diag_win, right_diag_win]):
                winning_ai_move = i
                break
        # finds a move to block
        for j in possible_choice:
            copy_board = copy.deepcopy(board)
            copy_board.add_new_char(j, board.blank_char, other_char)
            row_win = check_row_win(copy_board)
            col_win = check_col_win(copy_board)
            left_diag_win = check_left_diag_win(copy_board)
            right_diag_win = check_right_diag_win(copy_board)
            if any([row_win, col_win, left_diag_win, right_diag_win]):
                blocking_win_move = j
                break

        # if no winning or blocking round, goes into random move
        # determines which move to play
        if winning_ai_move == 'N' and blocking_win_move == 'N':
            choice = random.choice(options)
        elif winning_ai_move == 'N' and blocking_win_move != 'N':
            choice = blocking_win_move
        elif winning_ai_move != 'N' and blocking_win_move == 'N':
            choice = winning_ai_move
        elif winning_ai_move != 'N' and blocking_win_move != 'N':
            choice = winning_ai_move

        board.add_new_char(choice, board.blank_char, self.char)
