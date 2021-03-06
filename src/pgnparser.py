from move import Move

class PGNParser:
    def __init__(self):
        self.move = Move()

    def parse(self, pgn_move, color='W'):
        self.move.color = color
        if pgn_move[-1] == '#':
            self.move.is_checkmate = True
            pgn_move = pgn_move[:-1]
        if pgn_move[-1] == '+':
            self.move.is_check = True
            pgn_move = pgn_move[:-1]
        if pgn_move == 'O-O':
            self.__parse_kingside_castle()
        elif pgn_move == 'O-O-O':
            self.__parse_queenside_castle()
        elif pgn_move[0].isalpha() and pgn_move[0].islower():
            self.__parse_pawn_move(pgn_move)
        elif pgn_move[0].isalpha() and pgn_move[0].isupper():
            self.__parse_piece_move(pgn_move)
        return self.move

    def __parse_kingside_castle(self):
        self.move.is_kingside_castle = True

    def __parse_queenside_castle(self):
        self.move.is_queenside_castle = True

    def __parse_pawn_move(self, pgn_move):
        self.move.piece = 'p'
        if len(pgn_move) == 2:
            self.move.destination = get_coords(pgn_move)
        elif len(pgn_move) == 4 and pgn_move[1] == 'x':
            self.move.source = get_x_coord(pgn_move[0])
            self.move.destination = get_coords(pgn_move[2:])
            self.move.is_take = True

    def __parse_piece_move(self, pgn_move):
        self.move.piece = pgn_move[0]
        if len(pgn_move) == 3:
            self.move.destination = get_coords(pgn_move[1:])
        elif len(pgn_move) == 4 and pgn_move[1] == 'x':
            self.move.destination = get_coords(pgn_move[2:])
            self.move.is_take = True
        elif len(pgn_move) == 5 and pgn_move[2] == 'x':
            self.move.piece = pgn_move[:1]
            self.move.source = pgn_move[1:2]
            self.move.destination = get_coords(pgn_move[3:])


def get_coords(pgn_coordinates):
    return get_x_coord(pgn_coordinates), get_y_coord(pgn_coordinates)

def get_x_coord(pgn_coordinates):
    return ord(pgn_coordinates[0]) - 97

def get_y_coord(pgn_coordinates):
    return int(8 - int(pgn_coordinates[1]))
