from square import Square
from pieces import PieceFactory


class Board:

    def __init__(self, init_matrix = None):
        self.squares = [[Square(x, y) for x in range(0, 8)] for y in range(0, 8)]
        if(init_matrix == None):
            self.pieces = [2, 3, 4, 5, 6, 4, 3, 2]
            self.pawns = 8 * [1]
            self.dispose_pieces()
        else:
            for i, row in enumerate(init_matrix):
                for j, piece_value in enumerate(row):
                    if piece_value != 0:
                        self.squares[i][j].put(PieceFactory.build(piece_value))

    def dispose_pieces(self):
        self.__dispose_pieces(self.pieces, 7)
        self.__dispose_pieces(self.pawns, 6)
        self.__dispose_pieces([-x for x in self.pawns], 1)
        self.__dispose_pieces([-x for x in self.pieces], 0)

    def __dispose_pieces(self, pieces, row):
        for i, square in enumerate(self.squares[row]):
            square.put(PieceFactory.build(pieces[i]))

    def get_square(self, coordinates):
        return self.squares[coordinates[1]][coordinates[0]]

    def update(self, move):
        move.source.clear()
        move.destination.piece = PieceFactory.build_from_pgn(move.piece, move.color)

    def find_src_pawn_position(self, dest_pawn_position, color):
        square = self.get_square(dest_pawn_position)
        increments = [1, 2]
        if color == 'B':
            increments = [-1, -2]
        return self.__check_pawn_position(square, increments)

    def find_taking_pawn_position(self, dest_pawn_position, source_pawn_column, color):
        direction = 1 if color=='W' else -1
        dest_square = self.get_square(dest_pawn_position)
        src_square = self.get_square((source_pawn_column, dest_square.y + direction))
        if src_square.piece is not None and src_square.piece.name == 'p':
            return src_square

    def __check_pawn_position(self, square, increments):
        for increment in increments:
            src_square = self.squares[square.y + increment][square.x]
            if src_square.piece is not None and src_square.piece.name == 'p':
                return src_square

    def find_src_rook_position(self, dest_rook_position, color):
        dest_square = self.get_square(dest_rook_position)
        for x in range(8):
            src_square = self.get_square((x, dest_square.y))
            if src_square.piece is not None and src_square.piece.name == 'R':
                return src_square
        for y in range(8):
            src_square = self.get_square((dest_square.x, y))
            if src_square.piece is not None and src_square.piece.name == 'R':
                return src_square
        return False


    def find_taking_rook_position(self, dest_pawn_position, source_pawn_column, color):
        pass


    def print_board(self):
        for line in self.squares:
            line_str = ""
            for square in line:
                if square.piece == None:
                    line_str += '0'
                else:
                    line_str += square.piece.name
            print(line_str)
