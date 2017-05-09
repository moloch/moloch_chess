class Rook:
    def __init__(self, color):
        self.color = color
        self.name = 'R'

    def __str__(self):
        return self.name


class Knight:
    def __init__(self, color):
        self.color = color
        self.name = 'N'

    def __str__(self):
        return self.name


class Bishop:
    def __init__(self, color):
        self.color = color
        self.name = 'B'

    def __str__(self):
        return self.name


class Queen:
    def __init__(self, color):
        self.color = color
        self.name = 'Q'

    def __str__(self):
        return self.name


class King:
    def __init__(self, color):
        self.color = color
        self.name = 'K'

    def __str__(self):
        return self.name


class Pawn:
    def __init__(self, color):
        self.color = color
        self.name = 'p'

    def __str__(self):
        return self.name


class PieceFactory:

    @staticmethod
    def build(symbol, color):
        if symbol == 'R':
            return Rook(color)
        if symbol == 'B':
            return Bishop(color)
        if symbol == 'K':
            return Knight(color)
        if symbol == 'Q':
            return Queen(color)
        if symbol == 'K':
            return King(color)
        if symbol == 'p':
            return Pawn(color)