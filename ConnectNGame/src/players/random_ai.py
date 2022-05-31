import random
from ConnectNGame.src.players.player import Player


class RandomAi(Player):

    def take_turn(self, board, other_char: str) -> None:
        total = board.num_col
        board = board
        options = range(total)
        top_row = 0
        possible_choice = []

        for col in options:
            if board.game_board[top_row][col] == board.blank_char:
                possible_choice.append(col)

        choice = random.choice(possible_choice)
        board.add_new_char(choice, board.blank_char, self.char)
