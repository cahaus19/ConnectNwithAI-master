from typing import Tuple


def get_player_info_human(X: int, blank_char: str, used_char=0, used_name=0) -> Tuple[str, str]:  # type: ignore

    """
    has optional inputs for player 1's info, and will double check if name or piece is reused
    """

    while True:
        name = (input("HumanPlayer {} enter your name: ".format(X))).strip()
        lower = name.lower()
        if used_name != 0:
            used_lower = used_name.lower()

        if name.strip() == "":
            print("Your name cannot be the empty string or whitespace.")
            continue
        elif name == used_name or (used_name != 0 and lower == used_lower):
            print("You cannot use {} for your name as someone else is already using it.".format(name))
            continue

        char = (input('HumanPlayer {} enter your piece: '.format(X))).strip()
        if char.strip() == "":
            print("Your piece cannot be the empty string or whitespace.")
            continue
        elif len(char) != 1:
            print("{} is not a single character. Your piece can only be a single character.".format(char))
            continue
        elif char == blank_char:
            print("Your piece cannot be the same as the blank character.")
            continue
        elif char == used_char:
            print("You cannot use {} for your piece as {} is already using it.".format(char, used_name))
            continue
        else:
            break
        # print(used_char, 'used_char')

    return name, char
