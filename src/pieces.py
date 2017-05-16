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

    def perform_move(self, move, game):
        dest_square = game.board.get_square(move.destination)
        if move.is_take:
            src_square = game.board.find_taking_pawn_position(move.destination, move.source, game.current_player.color)
        else:
            src_square = game.board.find_src_pawn_position(move.destination, game.current_player.color)
        if src_square is not None:
            if dest_square.piece is None or dest_square.piece is not None and move.is_take:
                move.source = src_square
                move.destination = dest_square
                return move
        return False

    def __str__(self):
        return self.name


class PieceFactory:

    @staticmethod
    def build(value):
        color = 'W' if value > 0 else 'B'
        value = value if value > 0 else -1 * value
        if value == 1:
            return Pawn(color)
        elif value == 2:
            return Rook(color)
        elif value == 3:
            return Knight(color)
        elif value == 4:
            return Bishop(color)
        elif value == 5:
            return Queen(color)
        elif value == 6:
            return King(color)

    @staticmethod
    def build_from_pgn(value, color):
        if value == 'p':
            return Pawn(color)
        elif value == 'R':
            return Rook(color)
        elif value == 'N':
            return Knight(color)
        elif value == 'B':
            return Bishop(color)
        elif value == 'Q':
            return Queen(color)
        elif value == 'K':
            return King(color)
