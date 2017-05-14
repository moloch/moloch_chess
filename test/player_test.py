import unittest
from src.player import Player
from src.game import Game
from src.board import Board
from src.move import Move
from src.pgnparser import get_coords


class TestPlayer(unittest.TestCase):
    def move_test(self):
        player = Player('W', Game(Board()))
        player.move(Move(piece='p', destination=get_coords('e4')))
