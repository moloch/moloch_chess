class Board:

    def __init__(self):
        self.squares = [[Square() for i in range(0, 8)] for j in range(0, 8)]

    def get_square(self, coordinates):
        x = self.translate_x(coordinates[0])
        y = self.translate_y(coordinates[1])
        return self.squares[x][7]

    def translate_x(self, x):
        return ord(x) - 97

    def translate_y(self, y):
        return int(8 - int(y))


class Square:
    def get_x(self):
        return 0

    def get_y(self):
        return 7
