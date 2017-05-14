class Move:
    def __init__(self, piece=None, source=None, destination=None,
                 is_take=False, is_kingside_castle=False,
                 is_queenside_castle=False, is_checkmate=False):
        self.piece = piece
        self.source = source
        self.destination = destination
        self.is_take = is_take
        self.is_kingside_castle = is_kingside_castle
        self.is_queenside_castle = is_queenside_castle
        self.is_checkmate = is_checkmate
