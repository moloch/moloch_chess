class Player:
    def __init__(self, color, game):
        self.color = color
        self.game = game

    def move(self, move):
        return move.parse(self.game)
