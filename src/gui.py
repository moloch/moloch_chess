#!/usr/bin/env python

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QMimeData, QByteArray, QDataStream, QPoint, QIODevice, QBuffer)
from PyQt5.QtGui import (QBrush, QColor, QPainter, QPixmap, QDrag)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGraphicsPixmapItem, QGraphicsRectItem)

from game import Game
from board import Board
from move import Move


class SquareGraphics(QGraphicsRectItem):
    def __init__(self, board_graphics, square):
        super(SquareGraphics, self).__init__()
        self.board_graphics = board_graphics
        self.square = square
        self.setAcceptDrops(True)

    def dropEvent(self, event):
        game = self.board_graphics.game
        move = self.board_graphics.current_move
        move.destination = self.square.get_coords()
        game.current_player.move(move)
        piece_pixmap = QPixmap("img/" + self.board_graphics.moving_piece.piece.color +
                               "_" + self.board_graphics.moving_piece.piece.name + ".png")
        piece_pixmap = piece_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
        piece_graphics = PieceGraphics(self.board_graphics, piece_pixmap, self.square.piece)
        x = self.rect().x()
        y = self.rect().y()
        piece_graphics.setOffset(x, y)
        self.board_graphics.scene.removeItem(self.board_graphics.moving_piece)
        self.board_graphics.scene.addItem(piece_graphics)


class BoardGraphics(QGraphicsRectItem):
    def __init__(self, scene, game):
        super(BoardGraphics, self).__init__()
        self.scene = scene
        self.game = game
        self.__generate_board()
        self.moving_piece = None
        self.current_move = None

    def __generate_board(self):
        board = self.game.board
        for line in board.squares:
            for square in line:
                square_graphic_item = SquareGraphics(self, square)
                x = square.x * 70
                y = square.y * 70
                square_graphic_item.setRect(QRectF(x, y, 70, 70))
                if square.is_black():
                    square_graphic_item.setBrush(QBrush(QColor("grey")))
                else:
                    square_graphic_item.setBrush(QBrush(QColor("white")))
                self.scene.addItem(square_graphic_item)
                self.__add_piece(square.piece, x, y)

    def __add_piece(self, piece, x, y):
        if piece is not None:
            piece_pixmap = QPixmap("img/" + piece.color + "_" + piece.name + ".png")
            piece_pixmap = piece_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
            piece_graphics = PieceGraphics(self, piece_pixmap, piece)
            piece_graphics.setOffset(x, y)
            self.scene.addItem(piece_graphics)


class PieceGraphics(QGraphicsPixmapItem):
    def __init__(self, board_graphics, pixmap, piece):
        super().__init__(pixmap)
        self.board_graphics = board_graphics
        self.piece = piece

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        self.board_graphics.moving_piece = self
        move = Move()
        move.piece = self.piece.name
        move.source = self.piece.square.get_coords()
        move.color = self.piece.color
        self.board_graphics.current_move = move
        print("Changing moving piece to: " + self.piece.name)
        print("Current move is: " + str(self.board_graphics.current_move))
        item_data = QByteArray()
        buffer = QBuffer(item_data)
        buffer.open(QIODevice.WriteOnly)
        self.pixmap().save(buffer)
        mime_data = QMimeData()
        mime_data.setData('application/x-dnditemdata', item_data)

        drag = QDrag(event.widget())
        drag.setMimeData(mime_data)
        drag.setPixmap(self.pixmap())
        x = self.pos().toPoint().x() + self.pixmap().width() / 2
        y = self.pos().toPoint().y() + self.pixmap().height() / 2
        drag.setHotSpot(QPoint(x, y))
        drag.exec_()


class MainWindow(QGraphicsView):
    def __init__(self, game):
        super(MainWindow, self).__init__()
        self.game = game
        scene = QGraphicsScene(self)
        rectangle = BoardGraphics(scene, game)
        rectangle.setRect(QRectF(0, 0, 560, 560))
        scene.addItem(rectangle)
        scene.setSceneRect(0, 0, 560, 560)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setWindowTitle("Moloch Chess")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Game(Board())
    mainWindow = MainWindow(game)
    mainWindow.show()
    sys.exit(app.exec_())