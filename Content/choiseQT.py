# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choise.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoiceWindow(object):
    def setupUi(self, ChoiceWindow):
        ChoiceWindow.setObjectName("ChoiceWindow")
        ChoiceWindow.resize(343, 139)
        ChoiceWindow.setMinimumSize(QtCore.QSize(343, 139))
        ChoiceWindow.setMaximumSize(QtCore.QSize(343, 139))
        ChoiceWindow.setStyleSheet("QMainWindow{\n"
                "background-color: rgb(80, 80, 80);\n"
                "}\n"
                "QLabel{\n"
                "color:white;\n"
                "}\n"
                "\n"
                "QPushButton{\n"
                "background-color: rgb(100, 100,100);\n"
                "color: white;\n"
                "}\n"
                "\n"
                "QComboBox{\n"
                "background-color: rgb(100, 100,100);\n"
                "color:white;\n"
                "}\n"
                "\n"
                "QComboBox::Item{\n"
                "background-color: rgb(100, 100,100);\n"
                "color:white;\n"
                "}")
        self.centralwidget = QtWidgets.QWidget(ChoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(250, 110, 81, 23))
        self.button_play.setObjectName("button_play")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 321, 22))
        self.comboBox.setMinimumSize(QtCore.QSize(321, 22))
        self.comboBox.setMaximumSize(QtCore.QSize(321, 22))
        self.comboBox.setObjectName("comboBox")
        from sys import platform
        if platform == "linux" or platform == "linux2":
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
        if platform == 'win32':
            self.comboBox.addItem("")
            self.comboBox.addItem("")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(10, 110, 81, 23))
        self.button_close.setObjectName("button_close")
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(10, 10, 141, 23))
        self.label_message.setObjectName("label_message")
        self.label_warning = QtWidgets.QLabel(self.centralwidget)
        self.label_warning.setGeometry(QtCore.QRect(10, 80, 261, 23))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_warning.setFont(font)
        self.label_warning.setObjectName("label_warning")
        ChoiceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoiceWindow)

    def retranslateUi(self, ChoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "Выбор драйвера"))
        self.button_play.setText(_translate("ChoiceWindow", "Играть"))
        from sys import platform
        if platform == "linux" or platform == "linux2":
            self.comboBox.setItemText(0, _translate("ChoiceWindow", "X11"))
            self.comboBox.setItemText(1, _translate("ChoiceWindow", "Dga"))
            self.comboBox.setItemText(2, _translate("ChoiceWindow", "Fbcon"))
            self.comboBox.setItemText(3, _translate("ChoiceWindow", "Directfb"))
            self.comboBox.setItemText(4, _translate("ChoiceWindow", "Ggi"))
            self.comboBox.setItemText(5, _translate("ChoiceWindow", "Vgl"))
            self.comboBox.setItemText(6, _translate("ChoiceWindow", "Svgalib"))
            self.comboBox.setItemText(7, _translate("ChoiceWindow", "Aalib"))
        if platform == 'win32':
            self.comboBox.setItemText(0, _translate("ChoiceWindow", "DirectX"))
            self.comboBox.setItemText(1, _translate("ChoiceWindow", "Windib"))
        self.button_close.setText(_translate("ChoiceWindow", "Закрыть"))
        self.label_message.setText(_translate("ChoiceWindow", "Выберите драйвер:"))
        self.label_warning.setText(_translate("ChoiceWindow", ""))

