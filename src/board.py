class Board:

    def __init__(self):
        self.squares = [[Square(x,y) for y in range(0, 8)] for x in range(0, 8)]

    def get_square(self, coordinates):
        x = ord(coordinates[0]) - 97
        y = int(8 - int(coordinates[1]))
        return self.squares[x][y]


class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
