import unittest
from src.game import Game
from src.board import Board
from src.pgnparser import get_coords


class TestGame(unittest.TestCase):
    def game_initialization_test(self):
        game = Game(Board())
        self.assertIsNotNone(game.board)
        self.assertEqual('W', game.white_player.color)
        self.assertEqual('B', game.black_player.color)
        self.assertEqual('W', game.current_player.color)

    def game_pawn_move_test(self):
        board = Board()
        game = Game(board)
        self.assertEqual('p', board.get_square(get_coords('e2')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('e4')).piece)
        game.add_pgn_move('e4')
        self.assertEqual((get_coords('e2'))[0], game.moves[0].source.x)
        self.assertEqual((get_coords('e2'))[1], game.moves[0].source.y)
        self.assertEqual((get_coords('e4'))[0], game.moves[0].destination.x)
        self.assertEqual((get_coords('e4'))[1], game.moves[0].destination.y)
        self.assertEqual(None, board.get_square(get_coords('e2')).piece)
        self.assertEqual('p', board.get_square(get_coords('e4')).piece.name)

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
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('d1')).piece)
        game.add_pgn_move('Rd1')
        self.assertEqual((get_coords('d6'))[0], game.moves[0].source.x)
        self.assertEqual((get_coords('d6'))[1], game.moves[0].source.y)
        self.assertEqual((get_coords('d1'))[0], game.moves[0].destination.x)
        self.assertEqual((get_coords('d1'))[1], game.moves[0].destination.y)
        self.assertEqual(None, board.get_square(get_coords('d6')).piece)
        self.assertEqual('R', board.get_square(get_coords('d1')).piece.name)

    def black_rook_move_test(self):
        #White rook in d6, black rook in f3
        board = Board(init_matrix=[[6, 0, 0, 0, 0, 0, 0, -2],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 2, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, -2, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, -6, 0]])
        game = Game(board)
        game.current_player = game.black_player
        self.assertEqual('R', board.get_square(get_coords('h8')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('h1')).piece)
        game.add_pgn_move('Rh1')
        self.assertEqual((get_coords('h8'))[0], game.moves[0].source.x)
        self.assertEqual((get_coords('h8'))[1], game.moves[0].source.y)
        self.assertEqual((get_coords('h1'))[0], game.moves[0].destination.x)
        self.assertEqual((get_coords('h1'))[1], game.moves[0].destination.y)
        self.assertEqual(None, board.get_square(get_coords('h8')).piece)
        self.assertEqual('R', board.get_square(get_coords('h1')).piece.name)

    def rook_should_not_jump_over_pieces_while_moving_south_test(self):
        #White rook in d6, black rook in f3
        board = Board(init_matrix=[[6, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 2, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 0, -2, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, -6, 0]])
        game = Game(board)
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('d1')).piece)
        game.add_pgn_move('Rd1')
        self.assertEqual(0, len(game.moves))
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('d1')).piece)

    def rook_should_not_jump_over_pieces_while_moving_east_test(self):
        #White rook in d6, black rook in f3
        board = Board(init_matrix=[[6, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 2, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 0, -2, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, -6, 0]])
        game = Game(board)
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('h6')).piece)
        game.add_pgn_move('Rh6')
        self.assertEqual(0, len(game.moves))
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('h6')).piece)

    def rook_takes_test(self):
        #White rook in d6, black pawn in d3
        board = Board(init_matrix=[[6, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 2, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, -1, 0, 0, 0, -6],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        game = Game(board)
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual('p', board.get_square(get_coords('d3')).piece.name)
        game.add_pgn_move('Rxd3')
        self.assertEqual(1, len(game.moves))
        self.assertEqual(True, game.moves[0].is_take)
        self.assertEqual('R', board.get_square(get_coords('d3')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('d6')).piece)

    def rook_takes_near_piece_test(self):
        #White rook in d6, black pawn in c6
        board = Board(init_matrix=[[6, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, -1, 2, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, -6],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]])
        game = Game(board)
        self.assertEqual('R', board.get_square(get_coords('d6')).piece.name)
        self.assertEqual('p', board.get_square(get_coords('c6')).piece.name)
        game.add_pgn_move('Rxc6')
        self.assertEqual(1, len(game.moves))
        self.assertEqual(True, game.moves[0].is_take)
        self.assertEqual(None, board.get_square(get_coords('d6')).piece)
        self.assertEqual('R', board.get_square(get_coords('c6')).piece.name)

    def bishop_move_test(self):
        #White bishop in d6
        board = Board(init_matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 4]])
        game = Game(board)
        self.assertEqual('B', board.get_square(get_coords('h1')).piece.name)
        self.assertEqual(None, board.get_square(get_coords('a8')).piece)
        game.add_pgn_move('Ba8')
        self.assertEqual((get_coords('h1'))[0], game.moves[0].source.x)
        self.assertEqual((get_coords('h1'))[1], game.moves[0].source.y)
        self.assertEqual((get_coords('a8'))[0], game.moves[0].destination.x)
        self.assertEqual((get_coords('a8'))[1], game.moves[0].destination.y)
        self.assertEqual(None, board.get_square(get_coords('h1')).piece)
        self.assertEqual('B', board.get_square(get_coords('a8')).piece.name)
