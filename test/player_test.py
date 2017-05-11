import unittest
from src.player import Player
from src.game import Game
from src.board import Board


class TestPlayer(unittest.TestCase):
    def move_test(self):
        player = Player('W', Game(Board()))
