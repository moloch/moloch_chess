class Player:
    def __init__(self, color, game):
        self.color = color
        self.game = game

    def move(self, move):
        return self.game.add_move(move)

    def pgn_move(self, move):
        return self.game.add_pgn_move(move)
