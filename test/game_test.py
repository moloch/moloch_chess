import unittest
from src.game import Game
from src.board import Board


class TestGame(unittest.TestCase):

    def game_initialization_test(self):
        game = Game(Board())
        self.assertIsNotNone(game.board)