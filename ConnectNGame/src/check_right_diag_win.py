def check_right_diag_win(b) -> bool:

    col = b.num_col
    row = b.num_row
    blank = b.blank_char
    num_win = b.num_win
    num_in_diag = 1
    diag_board = ([[1 for j in range(col)] for i in range(row)])    # type: ignore

    for i in range(1, row):
        for j in range(1, col):
            if b.game_board[i][j] != blank and b.game_board[i-1][j-1] == b.game_board[i][j]:  # type: ignore
                num_in_diag = 1 + diag_board[i-1][j-1]
                diag_board[i][j] = num_in_diag

                if num_in_diag >= num_win:
                    return True

    return False
