
from typing import List, TypeVar, Any

T = TypeVar('T')


class Board(object):

    board_gen: List[Any]
    game_board: List[List[int]]

    def __init__(self, num_row: int, num_col: int, blank_char: str, num_win: int) -> None: # type ignore
        self.num_row = num_row
        self.num_col = num_col
        self.blank_char = blank_char
        self.game_board = []
        self.num_win = num_win
        self.board_gen = []

    def create_board(self) -> List[List[int]]:
        int_row = int(self.num_row)
        int_col = int(self.num_col)
        n = int_row
        m = int_col
        self.game_board = ([[i + j for j in range(m)] for i in range(n)])  # type: ignore
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):  # type: ignore
                self.game_board[i][j] = self.blank_char  # type: ignore

        return self.game_board

    def add_new_char(self, col_input: int, blank_char: str, player_char: str) -> None:
        blank_char = self.blank_char
        self.col_input = int(col_input)
        row_pos = int(self.num_row) - 1
        new_pos = self.game_board[row_pos][self.col_input]
        while new_pos != blank_char:
            row_pos = row_pos - 1
            new_pos = self.game_board[row_pos][self.col_input]
        self.game_board[row_pos][self.col_input] = player_char

    def erase_char(self, col_input: int) -> None:
        blank_char = self.blank_char
        self.col_input = int(col_input)
        row_pos = self.num_row - 1
        i = 0
        while i < row_pos:
            i += 1
            if self.game_board[i][self.col_input] != blank_char:
                break
            else:
                continue
        self.game_board[i][self.col_input] = blank_char

    def __str__(self) -> str:
        int_row = int(self.num_row)
        int_col = int(self.num_col)
        n = int_row + 1
        m = int_col + 1
        self.board_gen = ([[i + j for j in range(m)] for i in range(n)])   # type: ignore
        for i in range(len(self.board_gen)):
            for j in range(len(self.board_gen[i])):  # type: ignore
                if i * j != 0:
                    self.board_gen[i][j] = self.game_board[i-1][j-1]  # type: ignore
                else:
                    if self.board_gen[i][j] == 0:
                        self.board_gen[i][j] = ' '  # type: ignore
                    else:
                        self.board_gen[i][j] = self.board_gen[i][j] - 1

        stringy_boi = ''
        for i in range(len(self.board_gen)):
            for j in range(len(self.board_gen[i])):
                if j + 1 < len(self.board_gen[i]):
                   stringy_boi += str(self.board_gen[i][j]) + ' '
                elif j + 1 <= len(self.board_gen[i]):
                    stringy_boi += str(self.board_gen[i][j])
            if i + 1 < len(self.board_gen):
                stringy_boi += '\n'
        return stringy_boi

    def generic_print(self) -> None:
        print(self)


