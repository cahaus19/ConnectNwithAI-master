
def check_row_win(b) -> bool:  # type: ignore

    col = b.num_col
    row = b.num_row
    blank = b.blank_char
    num_win = b.num_win
    num_in_row = 1

    for i in range(1, row):
        for j in range(1, col):
            if b.game_board[i][j] != blank and b.game_board[i][j-1] == b.game_board[i][j]:   # type: ignore
                num_in_row += 1
                if num_in_row >= num_win:
                    return True
            else:
                num_in_row = 1
    return False
