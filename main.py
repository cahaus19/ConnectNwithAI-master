import random
from ConnectNGame.src.players.human_player import HumanPlayer
from ConnectNGame.src.players.random_ai import RandomAi
from ConnectNGame.src.players.simple_ai import SimpleAI
from ConnectNGame.src.board import Board
from ConnectNGame.src.game import Game
from ConnectNGame.src.get_board_info import get_board_info  # type: ignore
from determine_player_type import determine_player_type
from ConnectNGame.src.get_player_info_human import get_player_info_human
from ConnectNGame.src.get_player_info_rai import get_player_info_rai
from ConnectNGame.src.get_player_info_sai import get_player_info_sai


def main() -> None:
    info_output = get_board_info()
    num_row = int(info_output[0])
    num_col = int(info_output[1])
    num_win = int(info_output[2])
    blank_char = info_output[3]

    b = Board(num_row, num_col, blank_char, num_win)
    b.create_board()

    # portion for making players and getting player information
    p1_determine = determine_player_type(1)

    if p1_determine == 1:
        [p1_name, p1_char] = get_player_info_human(1, b.blank_char)
        p1 = HumanPlayer(p1_name, p1_char)
    elif p1_determine == 2:
        [p1_name, p1_char] = get_player_info_rai(1, b.blank_char)
        p1 = RandomAi(p1_name, p1_char)
    elif p1_determine == 3:
        [p1_name, p1_char] = get_player_info_sai(1, b.blank_char)
        p1 = SimpleAI(p1_name, p1_char)

    p2_determine = determine_player_type(2)
    if p2_determine == 1:
        [p2_name, p2_char] = get_player_info_human(2, b.blank_char, p1.char, p1.name)
        p2 = HumanPlayer(p2_name, p2_char)
    elif p2_determine == 2:
        [p2_name, p2_char] = get_player_info_rai(2, b.blank_char, p1.char)
        p2 = RandomAi(p2_name, p2_char)
    elif p2_determine == 3:
        [p2_name, p2_char] = get_player_info_sai(2, b.blank_char, p1.char)
        p2 = SimpleAI(p2_name, p2_char)

    # starts game
    g = Game(b, p1, p2)  # feeds the board and players to the game

    # for loop to get game
    while not g.game_over:
        b.generic_print()
        p1.take_turn(b, p2_char)
        p1.check_if_over(g)
        if g.game_over:
            break
        b.generic_print()
        p2.take_turn(b, p1_char)
        p2.check_if_over(g)


if __name__ == '__main__':
    main()
