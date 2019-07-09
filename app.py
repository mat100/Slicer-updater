import sys
import os

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from updater_ui import Ui_Updater
from updaters.kisslicer163 import KISSlicer163

UPDATE_URL_DELTIQ = "https://github.com/trilab3d/Slicer-profiles/archive/deltiq.zip"
UPDATE_URL_DELTIQ2 = "https://github.com/trilab3d/Slicer-profiles/archive/deltiq2.zip"

class MainWindow(QMainWindow, Ui_Updater):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()

    def assignWidgets(self):
        self.btnUpdate.clicked.connect(self.performUpdate)

    def performUpdate(self):
        url = None
        slicer = None

        if self.selPrinter.currentText() == "TriLAB DeltiQ":
            url = UPDATE_URL_DELTIQ
        else:
            QMessageBox.warning(None, "Unsupported printer", "{} printer is currently not supported".format(self.selPrinter.currentText()))
            return

        if self.selSlicer.currentText() == "KISSlicer 1.6.3":
            slicer = KISSlicer163(os.path.dirname(os.path.realpath(__file__)))
        else:
            QMessageBox.warning(None, "Unsupported slicer", "{} slicer is currently not supported".format(self.selSlicer.currentText()))
            return

        if url and slicer:
            if slicer.perform_update(url):
                QMessageBox.information(None, "Update successful", "Slicer profiles updated successfully")
            else:
                QMessageBox.critical(None, "Error", "Slicer profiles updated failed")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )