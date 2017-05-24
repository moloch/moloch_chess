#!/usr/bin/env python

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QMimeData, QByteArray, QDataStream, QPoint, QIODevice, QBuffer)
from PyQt5.QtGui import (QBrush, QColor, QPainter, QPixmap, QDrag)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGraphicsPixmapItem, QGraphicsRectItem)

from game import Game
from board import Board


class SquareGraphics(QGraphicsRectItem):
    def __init__(self):
        super(SquareGraphics, self).__init__()
        self.setAcceptDrops(True)


class BoardGraphics(QGraphicsRectItem):
    def __init__(self, scene, game):
        super(BoardGraphics, self).__init__()
        self.setAcceptDrops(True)
        self.scene = scene
        self.game = game
        self.__generate_board()

    def __generate_board(self):
        board = self.game.board
        for line in board.squares:
            for square in line:
                square_graphic_item = SquareGraphics()
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
            queen_pixmap = QPixmap("img/" + piece.color + "_" + piece.name + ".png")
            queen_pixmap = queen_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
            queen = PieceGraphics(queen_pixmap)
            queen.setOffset(x, y)
            self.scene.addItem(queen)

    def dragEnterEvent(self, event):
        print("Enter Drag")

    def dragLeaveEvent(self, event):
        print("Leave Drag")

    def dropEvent(self, event):
        queen_pixmap = QPixmap("img/w_Q.png")
        queen_pixmap = queen_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
        queen = PieceGraphics(queen_pixmap)
        x = event.scenePos().toPoint().x() - queen_pixmap.width() / 2
        y = event.scenePos().toPoint().y() - queen_pixmap.height() / 2
        queen.setOffset(x, y)
        self.scene.addItem(queen)


class PieceGraphics(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)

    def mousePressEvent(self, event):
        print("Press")

    def mouseMoveEvent(self, event):
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
        #queen_pixmap = QPixmap("img/w_Q.png")
        #queen_pixmap = queen_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
        #queen = PieceGraphics(queen_pixmap)
        #scene.addItem(queen)
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