class Move:
    def __init__(self, piece=None, color='W', source=None, destination=None,
                 is_take=False, is_kingside_castle=False,
                 is_queenside_castle=False, is_checkmate=False):
        self.piece = piece
        self.color = color
        self.source = source
        self.destination = destination
        self.is_take = is_take
        self.is_kingside_castle = is_kingside_castle
        self.is_queenside_castle = is_queenside_castle
        self.is_checkmate = is_checkmate

    def __repr__(self):
        return str(self.piece) + " " + str(self.color)+ " " + str(self.source) + " " +str(self.destination)
