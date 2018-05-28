
import os, sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, qApp, QSplashScreen, QPushButton
from PyQt5 import QtCore, QtGui
from time import sleep
from choiseQT import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ChoiceWindow()
        self.ui.setupUi(self)
        #self.ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.ui.button_close.clicked.connect(self.exitApp) # Действия выполняемые при нажатии на кнопку
        self.ui.button_play.clicked.connect(self.play) # Действия выполняемые при нажатии на кнопку
        self.ui.comboBox.activated.connect(self.pass_Net_Adap)
        #self.ui.button_play.clicked.connect()

        self.press = False
        self.lastPos = QtCore.QPoint(0, 0)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        if self.press:
            self.move(event.globalPos() - self.lastPos)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.press = True
        self.lastPos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.press = False

    def exitApp(self):
        sys.exit()

    def play(self):
        self.close()
        splash.show()
        Mwindow.load_data(splash)
        from sys import platform
        if platform == "linux" or platform == "linux2":
            drivers = ['x11', 'dga', 'fbcon', 'directfb', 'ggi', 'vgl', 'svgalib', 'aalib']
        elif platform == "win32":
            drivers = ['directx', 'windib']
        os.putenv('SDL_VIDEODRIVER', drivers[self.ui.comboBox.currentIndex()])
        import main
        sys.exit(app.exec_())

    def pass_Net_Adap(self):
        # print(str(self.ui.comboBox.currentText()))
        # print(str(self.ui.comboBox.currentIndex()))
        _translate = QtCore.QCoreApplication.translate
        self.ui.label_warning.setText(_translate("MainWindow", "Внимание! Убедитесь что у вас установлен " + self.ui.comboBox.currentText()))

# if not os.getenv('SDL_VIDEODRIVER'):
#     os.putenv('SDL_VIDEODRIVER', 'directx')



class MyWindow(QPushButton):
    def __init__(self):
        pass

    def load_data(self, sp):
        for i in range(1, 11):
            # print(i)
            sleep(0.1)
            sp.showMessage("Load... {0}%".format(i * 10 + i),
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
            qApp.processEvents()
            if i == 10:
                sp.close()
                #sys.exit()



if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    splash = QSplashScreen(QtGui.QPixmap("icon/rd.png"))
    Mwindow = MyWindow()
    qApp.processEvents()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    # app.exec_()
    #import main
