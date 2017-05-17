import unittest
from src.board import Board
from src.pgnparser import get_coords


class TestBoard(unittest.TestCase):

    def empty_board_test(self):
        board = Board()
        self.assertIsNotNone(board)

    def get_square_test(self):
        board = Board()
        a1 = board.get_square((0, 7))
        self.assertEqual(0, a1.x)
        self.assertEqual(7, a1.y)
        self.assertTrue(a1.is_black())
        b1 = board.get_square((1, 7))
        self.assertEqual(1, b1.x)
        self.assertEqual(7, b1.y)
        a2 = board.get_square((0, 6))
        self.assertEqual(0, a2.x)
        self.assertEqual(6, a2.y)
        self.assertTrue(a2.is_white())
        e2 = board.get_square((4, 6))
        self.assertEqual(4, e2.x)
        self.assertEqual(6, e2.y)
        e4 = board.get_square((4, 4))
        self.assertEqual(4, e4.x)
        self.assertEqual(4, e4.y)
        h8 = board.get_square((7, 0))
        self.assertEqual(7, h8.x)
        self.assertEqual(0, h8.y)
        self.assertTrue(h8.is_black())

    def initial_position_test(self):
        board = Board()
        self.assertEqual('R', board.get_square(get_coords('a1')).piece.name)
        self.assertEqual('W', board.get_square(get_coords('a1')).piece.color)
        self.assertEqual('N', board.get_square(get_coords('b1')).piece.name)
        self.assertEqual('p', board.get_square(get_coords('e2')).piece.name)
        self.assertEqual('K', board.get_square(get_coords('e8')).piece.name)
        self.assertEqual('B', board.get_square(get_coords('e8')).piece.color)

    def custom_position_test(self):
        # white king in d6 black king in f3
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 6, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, -6, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual('K', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual('W', board.get_square(get_coords('d6')).piece.color)
        self.assertEqual('K', board.get_square(get_coords('f3')).piece.name)
        self.assertEqual('B', board.get_square(get_coords('f3')).piece.color)

    def find_first_piece_north_test(self):
        # white pawns in e2 and e6
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(get_coords('e6')[0], board.find_first_piece(get_coords('e2'), 'N').x)
        self.assertEqual(get_coords('e6')[1], board.find_first_piece(get_coords('e2'), 'N').y)

    def find_first_piece_south_test(self):
        # white pawns in e2 and e6
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(get_coords('e2')[0], board.find_first_piece(get_coords('e6'), 'S').x)
        self.assertEqual(get_coords('e2')[1], board.find_first_piece(get_coords('e6'), 'S').y)

    def find_first_piece_west_test(self):
        # white pawns in b6 and f6
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 1, 0, 0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(get_coords('b6')[0], board.find_first_piece(get_coords('f6'), 'W').x)
        self.assertEqual(get_coords('b6')[1], board.find_first_piece(get_coords('f6'), 'W').y)

    def find_first_piece_east_test(self):
        # white pawns in b6 and f6
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 1, 0, 0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(get_coords('f6')[0], board.find_first_piece(get_coords('b6'), 'E').x)
        self.assertEqual(get_coords('f6')[1], board.find_first_piece(get_coords('b6'), 'E').y)

    def find_first_piece_south_east_test(self):
        board = Board(init_matrix=[[4, 4, 4, 4, 4, 4, 4, 0],
                                   [0, 1, 0, 0, 0, 0, 0, 1],
                                   [0, 0, 0, 1, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 0, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(get_coords('b7')[0], board.find_first_piece(get_coords('a8'), 'SE').x)
        self.assertEqual(get_coords('b7')[1], board.find_first_piece(get_coords('a8'), 'SE').y)
        self.assertEqual(get_coords('d6')[0], board.find_first_piece(get_coords('b8'), 'SE').x)
        self.assertEqual(get_coords('d6')[1], board.find_first_piece(get_coords('b8'), 'SE').y)
        self.assertEqual(get_coords('f5')[0], board.find_first_piece(get_coords('c8'), 'SE').x)
        self.assertEqual(get_coords('f5')[1], board.find_first_piece(get_coords('c8'), 'SE').y)
        self.assertEqual(get_coords('g5')[0], board.find_first_piece(get_coords('d8'), 'SE').x)
        self.assertEqual(get_coords('g5')[1], board.find_first_piece(get_coords('d8'), 'SE').y)
        self.assertEqual(get_coords('h5')[0], board.find_first_piece(get_coords('e8'), 'SE').x)
        self.assertEqual(get_coords('h5')[1], board.find_first_piece(get_coords('e8'), 'SE').y)
        self.assertEqual(get_coords('h6')[0], board.find_first_piece(get_coords('f8'), 'SE').x)
        self.assertEqual(get_coords('h6')[1], board.find_first_piece(get_coords('f8'), 'SE').y)
        self.assertEqual(get_coords('h7')[0], board.find_first_piece(get_coords('g8'), 'SE').x)
        self.assertEqual(get_coords('h7')[1], board.find_first_piece(get_coords('g8'), 'SE').y)

    def find_first_piece_south_west_test(self):
        board = Board(init_matrix=[[0, 4, 4, 4, 4, 4, 4, 4],
                                   [1, 0, 0, 0, 0, 0, 1, 0],
                                   [1, 0, 0, 0, 1, 0, 0, 0],
                                   [1, 0, 1, 0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual((1,0), get_coords('b8'))
        self.assertEqual((0,1), get_coords('a7'))
        self.assertEqual(get_coords('a7')[0], board.find_first_piece(get_coords('b8'), 'SW').x)
        self.assertEqual(get_coords('a7')[1], board.find_first_piece(get_coords('b8'), 'SW').y)
        self.assertEqual(get_coords('a6')[0], board.find_first_piece(get_coords('c8'), 'SW').x)
        self.assertEqual(get_coords('a6')[1], board.find_first_piece(get_coords('c8'), 'SW').y)
        self.assertEqual(get_coords('a5')[0], board.find_first_piece(get_coords('d8'), 'SW').x)
        self.assertEqual(get_coords('a5')[1], board.find_first_piece(get_coords('d8'), 'SW').y)
        self.assertEqual(get_coords('a4')[0], board.find_first_piece(get_coords('e8'), 'SW').x)
        self.assertEqual(get_coords('a4')[1], board.find_first_piece(get_coords('e8'), 'SW').y)
        self.assertEqual(get_coords('c5')[0], board.find_first_piece(get_coords('f8'), 'SW').x)
        self.assertEqual(get_coords('c5')[1], board.find_first_piece(get_coords('f8'), 'SW').y)
        self.assertEqual(get_coords('e6')[0], board.find_first_piece(get_coords('g8'), 'SW').x)
        self.assertEqual(get_coords('e6')[1], board.find_first_piece(get_coords('g8'), 'SW').y)
        self.assertEqual(get_coords('g7')[0], board.find_first_piece(get_coords('h8'), 'SW').x)
        self.assertEqual(get_coords('g7')[1], board.find_first_piece(get_coords('h8'), 'SW').y)
