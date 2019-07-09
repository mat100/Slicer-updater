# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/updater.ui',
# licensing of 'ui/updater.ui' applies.
#
# Created: Tue Jul  9 16:53:45 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Updater(object):
    def setupUi(self, Updater):
        Updater.setObjectName("Updater")
        Updater.resize(240, 320)
        Updater.setMinimumSize(QtCore.QSize(240, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/trilab.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Updater.setWindowIcon(icon)
        Updater.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Updater)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblUpdater = QtWidgets.QLabel(self.centralwidget)
        self.lblUpdater.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUpdater.setObjectName("lblUpdater")
        self.verticalLayout.addWidget(self.lblUpdater)
        self.lnUpdater = QtWidgets.QFrame(self.centralwidget)
        self.lnUpdater.setFrameShape(QtWidgets.QFrame.HLine)
        self.lnUpdater.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnUpdater.setObjectName("lnUpdater")
        self.verticalLayout.addWidget(self.lnUpdater)
        self.lblSlicer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSlicer.setFont(font)
        self.lblSlicer.setObjectName("lblSlicer")
        self.verticalLayout.addWidget(self.lblSlicer)
        self.selSlicer = QtWidgets.QComboBox(self.centralwidget)
        self.selSlicer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selSlicer.setObjectName("selSlicer")
        self.selSlicer.addItem("")
        self.selSlicer.setItemText(0, "KISSlicer 1.6.3")
        self.selSlicer.addItem("")
        self.selSlicer.setItemText(1, "PrusaSlicer 2.0")
        self.verticalLayout.addWidget(self.selSlicer)
        self.lblPrinter = QtWidgets.QLabel(self.centralwidget)
        self.lblPrinter.setObjectName("lblPrinter")
        self.verticalLayout.addWidget(self.lblPrinter)
        self.selPrinter = QtWidgets.QComboBox(self.centralwidget)
        self.selPrinter.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.selPrinter.setObjectName("selPrinter")
        self.selPrinter.addItem("")
        self.selPrinter.setItemText(0, "TriLAB DeltiQ")
        self.selPrinter.addItem("")
        self.selPrinter.setItemText(1, "TriLAB DeltiQ 2")
        self.verticalLayout.addWidget(self.selPrinter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnUpdate.setObjectName("btnUpdate")
        self.verticalLayout.addWidget(self.btnUpdate)
        self.horizontalLayout.addLayout(self.verticalLayout)
        Updater.setCentralWidget(self.centralwidget)

        self.retranslateUi(Updater)
        QtCore.QMetaObject.connectSlotsByName(Updater)

    def retranslateUi(self, Updater):
        Updater.setWindowTitle(QtWidgets.QApplication.translate("Updater", "Slicer updater", None, -1))
        self.lblUpdater.setText(QtWidgets.QApplication.translate("Updater", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Slicer updater</span></p></body></html>", None, -1))
        self.lblSlicer.setText(QtWidgets.QApplication.translate("Updater", "<html><head/><body><p><span style=\" color:#ffffff;\">Select slicer:</span></p></body></html>", None, -1))
        self.lblPrinter.setText(QtWidgets.QApplication.translate("Updater", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Select printer:</span></p></body></html>", None, -1))
        self.btnUpdate.setText(QtWidgets.QApplication.translate("Updater", "Update", None, -1))

import resources_rc
