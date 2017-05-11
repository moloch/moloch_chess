import unittest
from src.board import Board


class TestBoard(unittest.TestCase):

    def empty_board_test(self):
        board = Board()
        self.assertIsNotNone(board)

    def coordinates_translation_test(self):
        board = Board()
        a1 = board.get_square('a1')
        self.assertEqual(0, a1.x)
        self.assertEqual(7, a1.y)
        self.assertTrue(a1.is_black())
        b1 = board.get_square('b1')
        self.assertEqual(1, b1.x)
        self.assertEqual(7, b1.y)
        a2 = board.get_square('a2')
        self.assertEqual(0, a2.x)
        self.assertEqual(6, a2.y)
        self.assertTrue(a2.is_white())
        e2 = board.get_square('e2')
        self.assertEqual(4, e2.x)
        self.assertEqual(6, e2.y)
        self.assertEqual(4, board.squares[e2.y][e2.x].x)
        self.assertEqual(6, board.squares[e2.y][e2.x].y)
        e4 = board.get_square('e4')
        self.assertEqual(4, e4.x)
        self.assertEqual(4, e4.y)
        h8 = board.get_square('h8')
        self.assertEqual(7, h8.x)
        self.assertEqual(0, h8.y)
        self.assertTrue(h8.is_black())

    def initial_position_test(self):
        board = Board()
        self.assertEqual('R', board.get_square('a1').piece.name)
        self.assertEqual('N', board.get_square('b1').piece.name)
        self.assertEqual('p', board.get_square('e2').piece.name)

    def find_pawn_src_square_test(self):
        board = Board()
        self.assertEqual(4, board.find_src_pawn_position('e4', 'W').x)
        self.assertEqual(6, board.find_src_pawn_position('e4', 'W').y)
        self.assertEqual(4, board.find_src_pawn_position('e5', 'B').x)
        self.assertEqual(1, board.find_src_pawn_position('e5', 'B').y)

