import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.circles = []
        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        x, y, r = random.randint(0, self.geometry().width()), random.randint(0, self.geometry().height()), \
                  random.randint(0, 50)
        self.circles.append((x, y, r))
        self.update()
    
    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))

        for x, y, r in self.circles:
            painter.drawEllipse(x - r, y - r, x + r, y + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
