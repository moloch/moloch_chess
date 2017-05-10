from src.square import Square
from src.pieces import PieceFactory


class Board:

    def __init__(self):
        self.squares = [[Square(x, y) for x in range(0, 8)] for y in range(0, 8)]
        self.pieces = 'RNBQKBNR'
        self.pawns = 'pppppppp'
        self.dispose_pieces()

    def dispose_pieces(self):
        self.__dispose_pieces(self.pieces, 7, 'W')
        self.__dispose_pieces(self.pawns, 6, 'W')
        self.__dispose_pieces(self.pawns, 1, 'B')
        self.__dispose_pieces(self.pieces, 0, 'B')

    def __dispose_pieces(self, pieces, row, color):
        for i, square in enumerate(self.squares[row]):
            square.put(PieceFactory.build(pieces[i], color))

    def get_square(self, coordinates):
        y = ord(coordinates[0]) - 97
        x = int(8 - int(coordinates[1]))
        return self.squares[x][y]
