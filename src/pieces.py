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

    def check_move(self, move, game):
        dest_square = game.board.get_square(move.destination)
        src_square = game.board.find_src_pawn_position(move.destination, game.current_player.color)
        if src_square is not None:
            if dest_square.piece is None:
                move.source = src_square
                move.destination = dest_square
                return True
        return False

    def __str__(self):
        return self.name


class PieceFactory:

    @staticmethod
    def build(symbol, color):
        if symbol == 'R':
            return Rook(color)
        if symbol == 'N':
            return Knight(color)
        if symbol == 'B':
            return Bishop(color)
        if symbol == 'Q':
            return Queen(color)
        if symbol == 'K':
            return King(color)
        if symbol == 'p':
            return Pawn(color)