import unittest
from src.board import Board


class TestBoard(unittest.TestCase):

    def empty_board_test(self):
        board = Board()
        self.assertIsNotNone(board)

    def get_square_test(self):
        board = Board()
        a1 = board.get_square('a1')
        self.assertEqual(0, a1.get_x());
        self.assertEqual(7, a1.get_y());