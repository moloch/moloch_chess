class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.piece) + ')'

    def is_white(self):
        if self.x % 2 == 0:
            return True if self.y % 2 == 0 else False
        else:
            return False if self.y % 2 == 0 else True

    def is_black(self):
        return not self.is_white()

    def put(self, piece):
        self.piece = piece

    def clear(self):
        self.piece = None

    def get_coords(self):
        return self.x, self.y

