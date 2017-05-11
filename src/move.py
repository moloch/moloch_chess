class Move:
    def __init__(self):
        self.piece = None
        self.source = None
        self.destination = None
        self.is_take = False
        self.is_kingside_castle = False
        self.is_queenside_castle = False
        self.is_check = False
