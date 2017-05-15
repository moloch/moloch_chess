from src.square import Square
from src.pieces import PieceFactory


class Board:

    def __init__(self):
        self.squares = [[Square(x, y) for x in range(0, 8)] for y in range(0, 8)]
        self.pieces = [2, 3, 4, 5, 6, 4, 3, 2]
        self.pawns = 8 * [1]
        self.dispose_pieces()

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

    def find_src_pawn_position(self, dest_pawn_position, color):
        square = self.get_square(dest_pawn_position)
        increments = [1, 2]
        if color == 'B':
            increments = [-1, -2]
        return self.__check_pawn_position(square, increments)

    def __check_pawn_position(self, square, increments):
        for increment in increments:
            src_square = self.squares[square.y + increment][square.x]
            if src_square.piece is not None and src_square.piece.name == 'p':
                return src_square

    def print_board(self):
        for line in self.squares:
            print('\n')
            for square in line:
                print(square)
