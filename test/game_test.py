import unittest
from src.game import Game
from src.board import Board


class TestGame(unittest.TestCase):
    def game_initialization_test(self):
        game = Game(Board())
        self.assertIsNotNone(game.board)
        self.assertEqual('W', game.white_player.color)
        self.assertEqual('B', game.black_player.color)
        self.assertEqual('W', game.current_player.color)

    def game_move_test(self):
        game = Game(Board())
        game.add_pgn_move('e4')
        self.assertEqual(['e4'], game.moves)
