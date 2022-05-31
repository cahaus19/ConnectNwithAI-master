def check_tie(b) -> bool:  # type: ignore
    col = b.num_col
    row = b.num_row
    blank = b.blank_char
    non_blank = 0
    total = col * row

    for j in range(col):
        for i in range(row):
            if b.game_board[i][j] != blank:
                non_blank += 1
                if non_blank >= total:
                    return True
    return False
