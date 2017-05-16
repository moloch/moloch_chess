from game import Game
from board import Board

if __name__ == '__main__':
    game = Game(Board())
    while True:
        game.board.print_board()
        pgn = input("move:")
        game.current_player.pgn_move(pgn)
