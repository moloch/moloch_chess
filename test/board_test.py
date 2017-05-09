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
        a2 = board.get_square('a2')
        self.assertEqual(0, a2.x)
        self.assertEqual(6, a2.y)
        self.assertTrue(a2.is_white())
        h8 = board.get_square('h8')
        self.assertEqual(7, h8.x)
        self.assertEqual(0, h8.y)
        self.assertTrue(h8.is_black())

    def initial_position_test(self):
        board = Board()
        print(board.squares)
        print(board.get_square('a1'))
        self.assertEqual('R', board.get_square('a1').piece.name)
