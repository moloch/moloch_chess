import unittest
from src.game import Game
from src.board import Board
from src.pgnparser import get_coords


class TestGame(unittest.TestCase):
    def game_initialization_test(self):
        game = Game(Board())
        self.assertIsNotNone(game.board)
        self.assertEqual('W', game.white_player.color)
        self.assertEqual('B', game.black_player.color)
        self.assertEqual('W', game.current_player.color)

    def game_pawn_move_test(self):
        board = Board()
        game = Game(board)
        self.assertEqual('p', board.get_square(get_coords('e2')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('e4')).piece)
        game.add_pgn_move('e4')
        self.assertEqual((get_coords('e2'))[0], game.moves[0].source.x)
        self.assertEqual((get_coords('e2'))[1], game.moves[0].source.y)
        self.assertEqual((get_coords('e4'))[0], game.moves[0].destination.x)
        self.assertEqual((get_coords('e4'))[1], game.moves[0].destination.y)
        self.assertEqual(None, board.get_square(get_coords('e2')).piece)
        self.assertEqual('p', board.get_square(get_coords('e4')).piece.name)

    def rook_move_test(self):
        #White rook in d6, black rook in f3
        board = Board(init_matrix=[[6, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 2, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, -2, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, -6, 0]])
        game = Game(board)
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('d1')).piece)
        game.add_pgn_move('Rd1')
        self.assertEqual((get_coords('d6'))[0], game.moves[0].source.x)
        self.assertEqual((get_coords('d6'))[1], game.moves[0].source.y)
        self.assertEqual((get_coords('d1'))[0], game.moves[0].destination.x)
        self.assertEqual((get_coords('d1'))[1], game.moves[0].destination.y)
        self.assertEqual(None, board.get_square(get_coords('d6')).piece)
        self.assertEqual('R', board.get_square(get_coords('d1')).piece.name)
