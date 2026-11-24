import sys
import random
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter


class YellowCircles(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        size = random.randint(20, 100)
        w = max(0, self.width() - size)
        h = max(0, self.height() - size)

        x = random.randint(0, w)
        y = random.randint(0, h)

        self.circles.append((x, y, size, size))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        qp = QPainter(self)

        qp.setBrush(QColor(255, 255, 0))

        for x, y, width, height in self.circles:
            qp.drawEllipse(x, y, width, height)

        qp.end()

        self.circles.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YellowCircles()
    window.show()
    sys.exit(app.exec())