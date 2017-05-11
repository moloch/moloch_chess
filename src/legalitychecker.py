from src.pieces import PieceFactory


class LegalityChecker:
    def __init__(self, game):
        self.game = game

    def check(self, move, color):
        piece = PieceFactory.build(move.piece, self.game.current_player.color)
        return piece.check_move(move, self.game)