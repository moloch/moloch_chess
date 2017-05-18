class Piece:
    def perform_move(self, move, game):
        dest_square = game.board.get_square(move.destination)
        if move.is_take:
            src_square = self.find_taking_position(game.board, move.destination, move.source, game.current_player.color)
        else:
            src_square = self.find_src_position(game.board, move.destination, game.current_player.color)
        if src_square is not None:
            if dest_square.piece is None or dest_square.piece is not None and move.is_take:
                move.source = src_square
                move.destination = dest_square
                return move
        return False


class Rook(Piece):
    def __init__(self, color):
        self.color = color
        self.name = 'R'

    def find_src_position(self, board, dest_rook_position, color):
        dest_square = board.get_square(dest_rook_position)
        src_square = False
        for direction in ['N', 'S', 'W', 'E']:
            src_square = board.find_first_piece((dest_square.x, dest_square.y), direction)
            if src_square != None and src_square.piece.name == 'R':
                return src_square

    def find_taking_position(self, board, dest, source, color):
        return self.find_src_position(board, dest, color)

    def __str__(self):
        return self.name


class Knight(Piece):
    def __init__(self, color):
        self.color = color
        self.name = 'N'

    def __str__(self):
        return self.name


class Bishop(Piece):
    def __init__(self, color):
        self.color = color
        self.name = 'B'

    def find_src_position(self, board, dest_rook_position, color):
        dest_square = board.get_square(dest_rook_position)
        src_square = False
        for direction in ['SE', 'SW', 'NE', 'NW']:
            src_square = board.find_first_piece((dest_square.x, dest_square.y), direction)
            if src_square is not None and src_square.piece.name == 'B':
                return src_square

    def find_taking_position(self, board, dest, source, color):
        return self.find_src_position(board, dest, color)

    def __str__(self):
        return self.name


class Queen(Piece):
    def __init__(self, color):
        self.color = color
        self.name = 'Q'

    def __str__(self):
        return self.name


class King(Piece):
    def __init__(self, color):
        self.color = color
        self.name = 'K'

    def __str__(self):
        return self.name


class Pawn(Piece):
    def __init__(self, color):
        self.color = color
        self.name = 'p'

    def find_src_position(self, board, dest_pawn_position, color):
        square = board.get_square(dest_pawn_position)
        increments = [1, 2]
        if color == 'B':
            increments = [-1, -2]
        return self.__check_pawn_position(board, square, increments)

    def find_taking_position(self, board, dest_pawn_position, source_pawn_column, color):
        direction = 1 if color=='W' else -1
        dest_square = board.get_square(dest_pawn_position)
        src_square = board.get_square((source_pawn_column, dest_square.y + direction))
        if src_square.piece is not None and src_square.piece.name == 'p':
            return src_square

    def __check_pawn_position(self, board, square, increments):
        for increment in increments:
            src_square = board.squares[square.y + increment][square.x]
            if src_square.piece is not None and src_square.piece.name == 'p':
                return src_square

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
