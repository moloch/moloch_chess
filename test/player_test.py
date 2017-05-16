import unittest
from src.player import Player
from src.game import Game
from src.board import Board
from src.move import Move
from src.pgnparser import get_coords


class TestPlayer(unittest.TestCase):
    def pawn_move_test(self):
        game = Game(Board())
        self.assertEqual('W', game.current_player.color)
        self.assertEqual(0, len(game.moves))
        game.current_player.move(Move(piece='p', destination=get_coords('e4')))
        self.assertEqual(1, len(game.moves))
        self.assertEqual('B', game.current_player.color)

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
        game.current_player.move(Move(piece='R', destination=get_coords('d1')))
        self.assertEqual(1, len(game.moves))
        self.assertEqual('B', game.current_player.color)
