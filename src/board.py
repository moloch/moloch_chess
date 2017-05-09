class Board:

    def __init__(self):
        self.squares = [[Square(x,y) for y in range(0, 8)] for x in range(0, 8)]
        print(self.squares)

    def get_square(self, coordinates):
        x = self.translate_x(coordinates[0])
        y = self.translate_y(coordinates[1])
        return self.squares[x][y]

    def translate_x(self, x):
        return ord(x) - 97

    def translate_y(self, y):
        return int(8 - int(y))


class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
