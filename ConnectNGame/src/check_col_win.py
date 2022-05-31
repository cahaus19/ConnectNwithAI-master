def check_col_win(b) -> bool:  # type: ignore
    col = b.num_col
    row = b.num_row
    blank = b.blank_char
    num_win = b.num_win
    num_in_col = 0

    for j in range(1, col):
        for i in range(row):
            if b.game_board[i][j] != blank and (b.game_board[i - 1][j] == b.game_board[i][j]):  # type: ignore
                num_in_col += 1
                if num_in_col == num_win:
                    return True
            else:
                num_in_col = 1
    return False
