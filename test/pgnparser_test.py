import unittest
from src.pgnparser import PGNParser
from src.game import Game
from src.board import Board


class TestMove(unittest.TestCase):

    def setUp(self):
        self.parser = PGNParser()

    def pawn_move_test(self):
        parser = self.parser
        move = parser.parse('e4')
        self.assertEqual('p', move.piece)
        self.assertEqual('e4', move.destination)

    def pawn_takes_pawn_test(self):
        parser = self.parser
        parser.parse('exd4')
        self.assertEqual('p', parser.move.piece)
        self.assertEqual('d4', parser.move.destination)
        self.assertEqual(True, parser.move.is_take)

    def piece_move_test(self):
        parser = self.parser
        move = parser.parse('Qh8')
        self.assertEqual('Q', move.piece)
        self.assertEqual('h8', move.destination)

    def piece_takes_test(self):
        parser = self.parser
        move1 = parser.parse('Nxa3')
        self.assertEqual('N', move1.piece)
        self.assertEqual('a3', move1.destination)
        self.assertEqual(True, move1.is_take)

        move2 = parser.parse('Raxa3')
        self.assertEqual('R', move2.piece)
        self.assertEqual('a', move2.source)
        self.assertEqual('a3', move2.destination)
        self.assertEqual(True, move2.is_take)

    def pawn_check_test(self):
        parser = self.parser
        move = parser.parse('e4+')
        self.assertEqual('p', move.piece)
        self.assertEqual('e4', move.destination)
        self.assertEqual(True, move.is_check)

    def pawn_takes_with_check_test(self):
        parser = self.parser
        move = parser.parse('exd4+')
        self.assertEqual('p', move.piece)
        self.assertEqual('d4',move.destination)
        self.assertEqual(True, move.is_take)
        self.assertEqual(True, move.is_check)

    def piece_check_test(self):
        parser = self.parser
        move = parser.parse('Qh8+')
        self.assertEqual('Q', move.piece)
        self.assertEqual('h8', move.destination)
        self.assertEqual(True, move.is_check)


    def piece_takes_with_check_test(self):
        parser = self.parser
        move1 = parser.parse('Nxa3+')
        self.assertEqual('N', move1.piece)
        self.assertEqual('a3', move1.destination)
        self.assertEqual(True, move1.is_take)
        self.assertEqual(True, move1.is_check)

        move2 = parser.parse('Raxa3+')
        self.assertEqual('R', move2.piece)
        self.assertEqual('a', move2.source)
        self.assertEqual('a3', move2.destination)
        self.assertEqual(True, move2.is_take)
        self.assertEqual(True, move2.is_check)

    def kingside_castle_test(self):
        parser = self.parser
        move = parser.parse('O-O')
        self.assertEqual(True, move.is_kingside_castle)

    def queenside_castle_test(self):
        parser = self.parser
        move = parser.parse('O-O-O')
        self.assertEqual(True, move.is_queenside_castle)
