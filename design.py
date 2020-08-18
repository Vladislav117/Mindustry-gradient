# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 309)
        MainWindow.setStyleSheet("background-color:#1C1C1B")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 150, 321, 41))
        self.input.setStyleSheet("QLineEdit {color: #429F42 ; background-color: #2D2D2D; border: none;}\\nQTextBrowser:hover {color: #5BD75B ; background-color: #3A3A39; border: none;}")
        self.input.setObjectName("input")
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 210, 321, 41))
        self.output.setStyleSheet("QLineEdit {color: #429F42 ; background-color: #2D2D2D; border: none;}\\nQTextBrowser:hover {color: #5BD75B ; background-color: #3A3A39; border: none;}")
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.solve = QtWidgets.QPushButton(self.centralwidget)
        self.solve.setGeometry(QtCore.QRect(350, 150, 111, 41))
        self.solve.setStyleSheet("QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
" QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \n"
"QPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}")
        self.solve.setObjectName("solve")
        self.GameName = QtWidgets.QLabel(self.centralwidget)
        self.GameName.setGeometry(QtCore.QRect(20, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.GameName.setFont(font)
        self.GameName.setStyleSheet("QLabel {color: #D1D152}")
        self.GameName.setObjectName("GameName")
        self.Author = QtWidgets.QLabel(self.centralwidget)
        self.Author.setGeometry(QtCore.QRect(20, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Author.setFont(font)
        self.Author.setStyleSheet("QLabel {color: #D1D152}")
        self.Author.setObjectName("Author")
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(350, 210, 111, 41))
        self.copy.setStyleSheet("QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
" QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \n"
"QPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}")
        self.copy.setObjectName("copy")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.solve.setText(_translate("MainWindow", "Solve"))
        self.GameName.setText(_translate("MainWindow", "Mindustry gradient"))
        self.Author.setText(_translate("MainWindow", "by Vladislav117"))
        self.copy.setText(_translate("MainWindow", "Copy"))
