import sys
from typing import List
import random


def get_board_info() -> List:
    # set up random seed
    if len(sys.argv) > 2:
        seed = sys.argv[2]
        random.seed(int(seed))

    path = sys.argv[1]
    with open(path, 'r') as file_input:
    # with open('config_files/3X3X3.txt', 'r') as file_input:

        data = file_input.read()
        data = data.strip()
        split_data = data.split('\n')
        info_output = []
        for i in range(0, len(split_data)):
            first_str = split_data[i]
            split_str = first_str.split(':')
            info = list(map(str.strip, split_str))
            if info[0] == 'blank_char':
                blank_char = info[1]
                temp_blank = blank_char
            elif info[0] == 'num_rows':
                rows = info[1]
                temp_row = rows
            elif info[0] == 'num_pieces_to_win':
                winning_num = info[1]
                temp_win = winning_num
            elif info[0] == 'num_cols':
                cols = info[1]
                temp_cols = cols
        info_output.append(temp_row)
        info_output.append(temp_cols)
        info_output.append(temp_win)
        info_output.append(temp_blank)
    file_input.close()
    return info_output
