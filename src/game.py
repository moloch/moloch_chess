from src.player import Player
from src.pgnparser import PGNParser
from src.legalitychecker import LegalityChecker


class Game:
    def __init__(self, board):
        self.board = board
        self.white_player = Player('W', self)
        self.black_player = Player('B', self)
        self.current_player = self.white_player
        self.parser = PGNParser()
        self.legalityChecker = LegalityChecker(self)
        self.moves = []

    def add_pgn_move(self, pgn_move):
        move = self.parser.parse(pgn_move, self.current_player.color)
        self.add_move(move)

    def add_move(self, move):
        if self.legalityChecker.check(move):
            self.moves.append(move)
