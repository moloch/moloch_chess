import unittest
from src.pgnparser import PGNParser, get_coords, get_x_coord
from src.board import Board


class TestMove(unittest.TestCase):

    def setUp(self):
        self.parser = PGNParser()

    def pawn_move_test(self):
        parser = self.parser
        move = parser.parse('e4')
        self.assertEqual('p', move.piece)
        self.assertEqual(get_coords('e4'), move.destination)

    def pawn_takes_pawn_test(self):
        parser = self.parser
        parser.parse('exd4')
        self.assertEqual('p', parser.move.piece)
        self.assertEqual(get_coords('d4'), parser.move.destination)
        self.assertEqual(get_x_coord('e3'), parser.move.source)
        self.assertEqual(True, parser.move.is_take)

    def piece_move_test(self):
        parser = self.parser
        move = parser.parse('Qh8')
        self.assertEqual('Q', move.piece)
        self.assertEqual(get_coords('h8'), move.destination)

    def piece_takes_test(self):
        parser = self.parser
        move1 = parser.parse('Nxa3')
        self.assertEqual('N', move1.piece)
        self.assertEqual(get_coords('a3'), move1.destination)
        self.assertEqual(True, move1.is_take)

        move2 = parser.parse('Raxa3')
        self.assertEqual('R', move2.piece)
        self.assertEqual('a', move2.source)
        self.assertEqual(get_coords('a3'), move2.destination)
        self.assertEqual(True, move2.is_take)

    def pawn_check_test(self):
        parser = self.parser
        move = parser.parse('e4+')
        self.assertEqual('p', move.piece)
        self.assertEqual(get_coords('e4'), move.destination)
        self.assertEqual(True, move.is_check)

    def pawn_takes_with_check_test(self):
        parser = self.parser
        move = parser.parse('exd4+')
        self.assertEqual('p', move.piece)
        self.assertEqual(get_coords('d4'),move.destination)
        self.assertEqual(True, move.is_take)
        self.assertEqual(True, move.is_check)

    def piece_check_test(self):
        parser = self.parser
        move = parser.parse('Qh8+')
        self.assertEqual('Q', move.piece)
        self.assertEqual(get_coords('h8'), move.destination)
        self.assertEqual(True, move.is_check)


    def piece_takes_with_check_test(self):
        parser = self.parser
        move1 = parser.parse('Nxa3+')
        self.assertEqual('N', move1.piece)
        self.assertEqual(get_coords('a3'), move1.destination)
        self.assertEqual(True, move1.is_take)
        self.assertEqual(True, move1.is_check)

        move2 = parser.parse('Raxa3+')
        self.assertEqual('R', move2.piece)
        self.assertEqual('a', move2.source)
        self.assertEqual(get_coords('a3'), move2.destination)
        self.assertEqual(True, move2.is_take)
        self.assertEqual(True, move2.is_check)

    def pawn_takes_with_checkmate_test(self):
        parser = self.parser
        move = parser.parse('exd4#')
        self.assertEqual('p', move.piece)
        self.assertEqual(get_coords('d4'),move.destination)
        self.assertEqual(True, move.is_take)
        self.assertEqual(True, move.is_checkmate)

    def piece_checkmate_test(self):
        parser = self.parser
        move = parser.parse('Qh8#')
        self.assertEqual('Q', move.piece)
        self.assertEqual(get_coords('h8'), move.destination)
        self.assertEqual(True, move.is_checkmate)


    def piece_takes_with_checkmate_test(self):
        parser = self.parser
        move1 = parser.parse('Nxa3#')
        self.assertEqual('N', move1.piece)
        self.assertEqual(get_coords('a3'), move1.destination)
        self.assertEqual(True, move1.is_take)
        self.assertEqual(True, move1.is_checkmate)

        move2 = parser.parse('Raxa3#')
        self.assertEqual('R', move2.piece)
        self.assertEqual('a', move2.source)
        self.assertEqual(get_coords('a3'), move2.destination)
        self.assertEqual(True, move2.is_take)
        self.assertEqual(True, move2.is_checkmate)

    def kingside_castle_test(self):
        parser = self.parser
        move = parser.parse('O-O')
        self.assertEqual(True, move.is_kingside_castle)

    def queenside_castle_test(self):
        parser = self.parser
        move = parser.parse('O-O-O')
        self.assertEqual(True, move.is_queenside_castle)

    def coordinates_translation_test(self):
        board = Board()
        a1 = get_coords('a1')
        self.assertEqual((0, 7), a1)
        b1 = get_coords('b1')
        self.assertEqual((1, 7), b1)
        a2 = get_coords('a2')
        self.assertEqual((0, 6), a2)
        e2 = get_coords('e2')
        self.assertEqual((4, 6), e2)
        e4 = get_coords('e4')
        self.assertEqual((4, 4), e4)
        h8 = get_coords('h8')
        self.assertEqual((7,0), h8)
