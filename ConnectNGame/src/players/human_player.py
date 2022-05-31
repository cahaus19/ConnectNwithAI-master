from ConnectNGame.src.players.player import Player


class HumanPlayer(Player):

    def take_turn(self, board: object, other_char: str) -> None:  # type: ignore
        total_col = int(board.num_col)
        name = self.name
        board = board
        # print(name)
        while True:
            col_input = input('{}, please enter the column you want to play in: '.format(self.name))

            if not col_input.isdigit() and '-' not in col_input:
                print('{}, column needs to be an integer. {} is not an integer. '.format(self.name, col_input))
                continue

            elif int(col_input) > total_col - 1 or int(col_input)<0:
                print('Your column needs to be between 0 and {} but is actually {}.'.format(str(total_col - 1),
                                                                                            str(col_input)))
                continue

            elif board.game_board[0][int(col_input)] != board.blank_char:
                print('You cannot play in {} because it is full.'.format(col_input))
                continue
            else:
                board.add_new_char(col_input, board.blank_char, self.char)
                break
