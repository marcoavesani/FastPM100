# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastpm100/assets/strip_layout.ui'
#
# Created: Thu Jan  7 10:44:56 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 420)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameGraph = QtGui.QFrame(self.centralwidget)
        self.frameGraph.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameGraph.setFrameShadow(QtGui.QFrame.Raised)
        self.frameGraph.setObjectName("frameGraph")
        self.horizontalLayout.addWidget(self.frameGraph)
        self.frameRight = QtGui.QFrame(self.centralwidget)
        self.frameRight.setMinimumSize(QtCore.QSize(200, 400))
        self.frameRight.setMaximumSize(QtCore.QSize(200, 400))
        self.frameRight.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QtGui.QFrame.Raised)
        self.frameRight.setObjectName("frameRight")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frameRight)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(self.frameRight)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.labelCurrent = QtGui.QLabel(self.frameRight)
        self.labelCurrent.setObjectName("labelCurrent")
        self.verticalLayout_3.addWidget(self.labelCurrent)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.frameRight)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.labelMinimum = QtGui.QLabel(self.frameRight)
        self.labelMinimum.setObjectName("labelMinimum")
        self.verticalLayout.addWidget(self.labelMinimum)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtGui.QLabel(self.frameRight)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.labelMaximum = QtGui.QLabel(self.frameRight)
        self.labelMaximum.setObjectName("labelMaximum")
        self.verticalLayout_2.addWidget(self.labelMaximum)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtGui.QLabel(self.frameRight)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.labelSpeed = QtGui.QLabel(self.frameRight)
        self.labelSpeed.setObjectName("labelSpeed")
        self.verticalLayout_4.addWidget(self.labelSpeed)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.frameRight)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCurrent.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMinimum.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMaximum.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSpeed.setText(QtGui.QApplication.translate("MainWindow", "DFPS 0.0, RFPS 0.0", None, QtGui.QApplication.UnicodeUTF8))

