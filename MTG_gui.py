# the module containing the necessary graphical design scripts

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, time


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 1000, 1000)  # xps, yps, width, height, (0,0) -- ( , )
        self.setWindowTitle('Magic Processing Unit')
        self.label = QtWidgets.QLabel(self)
        self.label.setText("""Let's walk the planes.""")
        self.update()  # adjusts label width view
        self.label.move(350, 500)  # xps, yps
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('TAP')
        self.b1.clicked.connect(self.swing)

    def swing(self):
        self.label.setText('You tapped your card.')
        self.update()

    def update(self):
        self.label.adjustSize()


def window():  # simply learning how to use the system to make a gui
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
