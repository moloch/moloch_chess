from square import Square
from pieces import PieceFactory
from directions import DirectionFactory

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
        move.destination.piece.assign_to_square(move.destination)

    def find_first_piece(self, source, direction):
        return DirectionFactory.build(direction).find_first_piece(self, source)

    def find_first_knight(self, source, direction):
        return DirectionFactory.build(direction).find_first_knight(self, source)

    def print_board(self):
        for line in self.squares:
            line_str = ""
            for square in line:
                if square.piece == None:
                    line_str += '0'
                else:
                    line_str += square.piece.name
            print(line_str)
