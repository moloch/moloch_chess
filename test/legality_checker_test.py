import unittest
from src.legalitychecker import LegalityChecker
from src.move import Move
from src.game import Game
from src.board import Board
from src.pgnparser import get_coords, get_x_coord


class TestGame(unittest.TestCase):
    def pawn_legal_move_check_test(self):
        checker = LegalityChecker(Game(Board()))
        move = Move(piece='p', destination=get_coords('e4'))
        self.assertNotEqual(False, checker.check(move))

    def pawn_legal_take_check_test(self):
        # e3 takes d4  -> exd4
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, -1, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        checker = LegalityChecker(Game(board=board))
        move = Move(piece='p', destination=get_coords('d4'), source=get_x_coord('e3'), is_take=True)
        self.assertNotEqual(False, checker.check(move))

    def pawn_illegal_move_check_test(self):
        checker = LegalityChecker(Game(Board()))
        move = Move(piece='p', destination=get_coords('e5'))
        self.assertEqual(False, checker.check(move))
        move = Move(piece='p', destination=get_coords('e2'))
        self.assertEqual(False, checker.check(move))
