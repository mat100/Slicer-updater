import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import QApplication, QMainWindow
from updater_ui import Ui_Updater

class MainWindow(QMainWindow, Ui_Updater):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()

    def assignWidgets(self):
        self.btnUpdate.clicked.connect(self.performUpdate)

    def performUpdate(self):
        print(self.selSlicer.currentText())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )