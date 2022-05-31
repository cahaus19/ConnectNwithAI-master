import random
from typing import Tuple


def get_player_info_rai(X, blank, other=':)') -> Tuple[str, str]:
    if X == 1:
        name = 'RandomAi 1'
    elif X == 2:
        name = 'RandomAi 2'
    char_list = [chr(i) for i in range(ord('!'), ord('~') + 1)]
    while True:
        char = random.choice(char_list)
        if char != blank and char != other:
            return name, char
