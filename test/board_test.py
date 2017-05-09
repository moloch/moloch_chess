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
        h8 = board.get_square('h8')
        self.assertEqual(7, h8.x)
        self.assertEqual(0, h8.y)
