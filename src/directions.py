from abc import abstractmethod


class Direction:
    @abstractmethod
    def find_first_piece(self, board, source):
        pass


class SimpleDirection(Direction):
    def find_first_piece(self, board, source):
        for coord in range(*self.get_range(source)):
            current_square = board.get_square(self.find_coordinates(source, coord))
            if current_square.piece is not None:
                return current_square
        return None

    @abstractmethod
    def find_coordinates(self, source, coord):
        pass

    @abstractmethod
    def get_range(self, source):
        pass


class VerticalDirection(SimpleDirection):
    def find_coordinates(self, source, coord):
        return source[0], coord

    @abstractmethod
    def get_range(self, source):
        pass


class HorizontalDirection(SimpleDirection):
    def find_coordinates(self, source, coord):
        return coord, source[1]

    @abstractmethod
    def get_range(self, source):
        pass


class North(VerticalDirection):
    def get_range(self, source):
        return source[1] - 1, -1, -1


class South(VerticalDirection):
    def get_range(self, source):
        return source[1] + 1, 8


class West(HorizontalDirection):
    def get_range(self, source):
        return source[0] - 1, -1, -1


class East(HorizontalDirection):
    def get_range(self, source):
        return source[0] + 1, 8


class ComplexDirection(Direction):
    def find_first_piece(self, board, source):
        for x in range(*self.get_range(source)):
            y = self.get_y(source, x)
            if 0 <= y <= 7:
                current_square = board.get_square((x, y))
                if current_square.piece is not None:
                    return current_square
        return None

    def find_first_knight(self, board, source):
        coordinates = self.find_first_knight_coords(board, *source)
        if coordinates is None:
            return None
        for coords in coordinates:
            current_square = board.get_square(coords)
            if current_square.piece is not None and current_square.piece.name is 'N':
                return current_square

    @abstractmethod
    def find_knight_coords(self, board, source):
        pass

    @abstractmethod
    def get_range(self, source):
        pass

    @abstractmethod
    def get_y(self, source, x):
        pass


class SouthEast (ComplexDirection):
    def get_range(self, source):
        return source[0] + 1, 8

    def get_y(self, source, x):
        return source[1] - source[0] + x

    def find_first_knight_coords(self, board, x, y):
        return [(x + 2, y + 1), (x + 1, y + 2)]


class SouthWest(ComplexDirection):
    def get_range(self, source):
        return source[0] - 1, -1, -1

    def get_y(self, source, x):
        return source[0] + source[1] - x

    def find_first_knight_coords(self, board, x, y):
        return [(x - 2, y + 1), (x - 1, y + 2)]


class NorthEast(ComplexDirection):
    def get_range(self, source):
        return source[0] + 1, 8

    def get_y(self, source, x):
        return source[0] + source[1] - x

    def find_first_knight_coords(self, board, x, y):
        return [(x + 2, y - 1), (x + 1, y - 2)]


class NorthWest (ComplexDirection):
    def get_range(self, source):
        return source[0] - 1, -1, -1

    def get_y(self, source, x):
        return source[1] - source[0] + x

    def find_first_knight_coords(self, board, x, y):
        return [(x - 2, y - 1), (x - 1, y - 2)]


class DirectionFactory:
    def build(key):
        if key == 'N':
            return North()
        elif key == 'S':
            return South()
        elif key == 'W':
            return West()
        elif key == 'E':
            return East()
        elif key == 'SE':
            return SouthEast()
        elif key == 'SW':
            return SouthWest()
        elif key == 'NE':
            return NorthEast()
        elif key == 'NW':
            return NorthWest()
