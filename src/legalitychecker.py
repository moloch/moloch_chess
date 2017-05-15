from src.pieces import PieceFactory


class LegalityChecker:
    def __init__(self, game):
        self.game = game

    def check(self, move):
        piece = PieceFactory.build_from_pgn(move.piece, move.color)
        return piece.check_move(move, self.game)