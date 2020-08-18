from PyQt5 import QtWidgets, QtGui
from pip._internal.exceptions import HashErrors
import design
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import pyperclip


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


class App(QtWidgets.QMainWindow, design.Ui_MainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.col_1 = QColor(0, 0, 0)
        self.col_2 = QColor(0, 0, 0)

        self.color_button_1 = QPushButton('Select first color', self)
        # self.color_button_1.move(20, 102)
        self.color_button_1.setGeometry(20, 110, 111, 31)
        self.color_button_1.clicked.connect(self.showDialog)
        self.color_button_1.setStyleSheet('QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \nQPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}')

        self.color_button_2 = QPushButton('Select second color', self)
        self.color_button_2.setGeometry(140, 110, 111, 31)
        self.color_button_2.setStyleSheet('QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \nQPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}')
        self.color_button_2.clicked.connect(self.showDialog2)

    def showDialog(self):
        self.col_1 = QColorDialog.getColor()
        if self.col_1.isValid():
            self.color_button_1.setStyleSheet("QPushButton { background-color: %s }"
                                              % self.col_1.name())

    def showDialog2(self):
        self.col_2 = QColorDialog.getColor()
        if self.col_2.isValid():
            self.color_button_2.setStyleSheet("QPushButton { background-color: %s }"
                                              % self.col_2.name())


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()


def solve():
    if window.input.text() != '':
        start_color = list(window.col_1.getRgb()[:-1])
        end_color = list(window.col_2.getRgb()[:-1])
        text = window.input.text()
        steps = [(end_color[i] - start_color[i]) // len(text) for i in range(3)]
        o = ''
        for i in range(len(text)):
            for c_index in range(3):
                start_color[c_index] += steps[c_index]
            if rgb_to_hex(tuple(start_color)).find('-') == -1:
                o += '[' + rgb_to_hex(tuple(start_color)) + ']' + text[i]
            else:
                o += text[i]
        window.output.setText(o)


def copy():
    pyperclip.copy(window.output.text())


# --- --- ---
# Window parameters
window.setWindowTitle('Mindustry gradient [by Vladislav117]')
window.setWindowIcon(QtGui.QIcon('icon.png'))
window.solve.clicked.connect(solve)
window.copy.clicked.connect(copy)
# So, let's start!
app.exec()
