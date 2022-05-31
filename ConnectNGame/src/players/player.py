from abc import abstractmethod


class Player:

    def __init__(self, name: object, char: object) -> None:
        self.name = name
        self.char = char

    @abstractmethod
    def check_if_over(self, game) -> None:
        game.check_if_game_over()
        if game.game_over:
            print('{} won the game!'.format(self.name))
