#!/usr/bin/env python

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QMimeData, QByteArray, QDataStream, QPoint, QIODevice, QBuffer)
from PyQt5.QtGui import (QBrush, QColor, QPainter, QPixmap, QDrag)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGraphicsPixmapItem, QGraphicsRectItem)


class BoardGraphicsItem(QGraphicsRectItem):
    def __init__(self, scene):
        super(BoardGraphicsItem, self).__init__()
        self.setAcceptDrops(True)
        self.scene = scene

    def dragEnterEvent(self, event):
        print("Enter Drag")

    def dragLeaveEvent(self, event):
        print("Leave Drag")

    def dropEvent(self, event):
        queen_pixmap = QPixmap("img/w_Q.png")
        queen_pixmap = queen_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
        queen = PieceGraphicsPixmapItem(queen_pixmap)
        x = event.scenePos().toPoint().x() - queen_pixmap.width() / 2
        y = event.scenePos().toPoint().y() - queen_pixmap.height() / 2
        queen.setOffset(x, y)
        self.scene.addItem(queen)


class PieceGraphicsPixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)

    def mousePressEvent(self, event):
        print("Press")

    def mouseMoveEvent(self, event):
        itemData = QByteArray()
        buffer = QBuffer(itemData)
        buffer.open(QIODevice.WriteOnly)
        self.pixmap().save(buffer)
        mimeData = QMimeData()
        mimeData.setData('application/x-dnditemdata', itemData)

        drag = QDrag(event.widget())
        drag.setMimeData(mimeData)
        drag.setPixmap(self.pixmap())
        x = self.pos().toPoint().x() + self.pixmap().width() / 2
        y = self.pos().toPoint().y() + self.pixmap().height() / 2
        drag.setHotSpot(QPoint(x, y))
        drag.exec_()


class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene(self)
        rectangle = BoardGraphicsItem(scene)
        rectangle.setRect(QRectF(0, 0, 300, 300))
        scene.addItem(rectangle)
        queen_pixmap = QPixmap("img/w_Q.png")
        queen_pixmap = queen_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
        queen = PieceGraphicsPixmapItem(queen_pixmap)
        queen.setOffset(100, 100)
        scene.addItem(queen)
        scene.setSceneRect(0, 0, 300, 300)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setWindowTitle("Moloch Chess")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())