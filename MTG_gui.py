# the module containing the necessary graphical design scripts

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from tkinter import *

# still deciding which interface to use

class Root(Tk)



def window(): # simply learning how to use the system to make a gui
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 1000, 1000)  # xps, yps, width, heigth, (0,0) -- ( , )
    win.setWindowTitle('Magic Processing Unit')

    label = QtWidgets.QLabel(win) # sets where the label goes
    label.setText('EYHOA!')
    label.move(50, 50) # xps, yps from top left corner of window

    win.show()
    sys.exit(app.exec_())


window()
