from src.player import Player


class Game:
    def __init__(self, board):
        self.board = board
        self.white_player = Player('W', self)
        self.black_player = Player('B', self)
        self.current_player = self.white_player
