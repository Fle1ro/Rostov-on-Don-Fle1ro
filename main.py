from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter, QPen
import random



class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__(self)
        uic.loadUi('UI.ui', self)

        self.pushButton.connect(self.draw())

    def draw(self):
        qp = QPainter()
        qp.begin(self)
        size = random.randint(20, 100)
        w = self.geometry().width()
        h = self.geometry().height()
        r, g, b = 255, 255, 0
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(random.randint(0, w) - size // 2, random.randint(0, h) - size // 2)