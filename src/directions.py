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


class SouthWest(ComplexDirection):
    def get_range(self, source):
        return source[0] - 1, -1, -1

    def get_y(self, source, x):
        return source[0] + source[1] - x


class NorthEast(ComplexDirection):
    def get_range(self, source):
        return source[0] + 1, 8

    def get_y(self, source, x):
        return source[0] + source[1] - x


class NorthWest (Direction):
    def get_range(self, source):
        return source[0] - 1, -1, -1

    def get_y(self, source, x):
        return source[1] - source[0] + x


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
