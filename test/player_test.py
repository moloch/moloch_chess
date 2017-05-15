import unittest
from src.player import Player
from src.game import Game
from src.board import Board
from src.move import Move
from src.pgnparser import get_coords


class TestPlayer(unittest.TestCase):
    def move_test(self):
        game = Game(Board())
        self.assertEqual(0, len(game.moves))
        player = Player('W', game)
        player.move(Move(piece='p', destination=get_coords('e4')))
        self.assertEqual(1, len(game.moves))
