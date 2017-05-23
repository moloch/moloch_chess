#!/usr/bin/env python

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QMimeData, QByteArray, QDataStream, QPoint, QIODevice, QBuffer)
from PyQt5.QtGui import (QBrush, QColor, QPainter, QPixmap, QDrag)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGraphicsPixmapItem, QGraphicsRectItem)


class BoardGraphicsItem(QGraphicsRectItem):
    def __init__(self):
        super(BoardGraphicsItem, self).__init__()


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


    def dragEnterEvent(self, event):
        print("Enter Drag")

    def dragLeaveEvent(self, event):
        print("Leave Drag")

    def dropEvent(self, event):
        print("Drop")


class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene(self)
        scene.addItem(BoardGraphicsItem())
        queen_pixmap = QPixmap("img/w_Q.png")
        queen_pixmap = queen_pixmap.scaledToHeight(64, Qt.SmoothTransformation)
        queen = PieceGraphicsPixmapItem(queen_pixmap)
        queen.setOffset(100,100)
        scene.addItem(queen)
        #Usare QGraphicsPixmapItem per i vari pezzi, la scacchiera sara' lo sfondo QgraphicsView
        scene.setSceneRect(0, 0, 300, 300)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setWindowTitle("Moloch Chess")

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_R:
            self.tic_tac_toe.reset()
        super(MainWindow, self).keyPressEvent(event)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())