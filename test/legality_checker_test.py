import unittest
from src.legalitychecker import LegalityChecker
from src.move import Move
from src.game import Game
from src.board import Board
from src.pgnparser import get_coords


class TestGame(unittest.TestCase):
    def pawn_legal_move_check_test(self):
        checker = LegalityChecker(Game(Board()))
        move = Move()
        move.piece = 'p'
        move.destination = get_coords('e4')
        self.assertEqual(True, checker.check(move, 'W'))

    def pawn_illegal_move_check_test(self):
        checker = LegalityChecker(Game(Board()))
        move = Move()
        move.piece = 'p'
        move.destination = get_coords('e5')
        self.assertEqual(False, checker.check(move, 'W'))
