import random
from typing import Tuple


def get_player_info_sai(X, blank, other=':) ') -> Tuple[str, str]:
    if X == 1:
        name = 'SimpleAi 1'
    elif X == 2:
        name = 'SimpleAi 2'
    char_list = [chr(i) for i in range(ord('!'), ord('~') + 1)]

    while True:
        char = random.choice(char_list)
        if char != blank and char != other:
            return name, char
