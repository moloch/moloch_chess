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
        self.assertEqual(get_coords('b6'), board.find_first_piece(get_coords('f6'), 'W').get_coords())

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
                                   [4, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [4, 0, 0, 0, 4, 0, 0, 0],
                                   [0, 0, 0, 1, 0, 1, 0, 0]])
        pairings = [('a8', 'b7'),
                    ('b8', 'd6'),
                    ('c8', 'f5'),
                    ('d8','g5'),
                    ('e8','h5'),
                    ('f8','h6'),
                    ('g8', 'h7'),
                    ('a4', 'd1'),
                    ('e2', 'f1')]
        self.check_all_pairings(board, pairings, 'SE')
        self.assertEqual(None, board.find_first_piece(get_coords('a2'), 'SE'))

    def find_first_piece_south_west_test(self):
        board = Board(init_matrix=[[0, 4, 4, 4, 4, 4, 4, 4],
                                   [1, 0, 0, 0, 0, 0, 1, 0],
                                   [1, 0, 0, 0, 1, 0, 0, 0],
                                   [1, 0, 1, 0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 4],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 0]])
        pairings = [('b8', 'a7'),
                    ('c8', 'a6'),
                    ('d8', 'a5'),
                    ('e8','a4'),
                    ('f8','c5'),
                    ('g8','e6'),
                    ('h8', 'g7'),
                    ('h4', 'e1')]
        self.check_all_pairings(board, pairings, 'SW')

    def find_first_piece_north_east_test(self):
        board = Board(init_matrix=[[0, 0, 0, 1, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [4, 0, 0, 0, 0, 0, 0, 0],
                                   [4, 0, 0, 0, 0, 0, 1, 0],
                                   [0, 0, 0, 1, 1, 0, 1, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 1],
                                   [4, 4, 4, 4, 4, 4, 4, 0]])
        pairings = [('a1', 'h8'),
                    ('b1', 'd3'),
                    ('c1', 'e3'),
                    ('d1', 'g4'),
                    ('e1', 'g3'),
                    ('f1', 'h3'),
                    ('g1', 'h2'),
                    ('a5', 'd8')]
        self.assertEqual(None, board.find_first_piece(get_coords('a4'), 'NE'))

    def find_first_piece_north_west_test(self):
        board = Board(init_matrix=[[1, 0, 0, 0, 1, 1, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 4],
                                   [1, 0, 0, 0, 0, 0, 0, 4],
                                   [1, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 4, 4, 4, 4, 4, 4, 4]])
        pairings = [('b1', 'a2'),
                    ('c1', 'a3'),
                    ('d1', 'a4'),
                    ('e1', 'a5'),
                    ('f1', 'a6'),
                    ('g1', 'a7'),
                    ('h1', 'a8'),
                    ('h5', 'e8'),
                    ('h6', 'f8')]
        self.assertEqual(None, board.find_first_piece(get_coords('a4'), 'NW'))

    def check_all_pairings(self, board, pairings, direction):
        for pair in pairings:
            expected = get_coords(pair[1])
            actual = board.find_first_piece(get_coords(pair[0]), direction).get_coords()
            self.assertEqual(expected, actual)
