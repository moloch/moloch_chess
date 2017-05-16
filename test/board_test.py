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

    def find_pawn_src_square_test(self):
        board = Board()
        self.assertEqual(4, board.find_src_pawn_position(get_coords('e4'), 'W').x)
        self.assertEqual(6, board.find_src_pawn_position(get_coords('e4'), 'W').y)
        self.assertEqual(4, board.find_src_pawn_position(get_coords('e5'), 'B').x)
        self.assertEqual(1, board.find_src_pawn_position(get_coords('e5'), 'B').y)

