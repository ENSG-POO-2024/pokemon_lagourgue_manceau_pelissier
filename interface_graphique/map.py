# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.herbe = QtWidgets.QLabel(self.centralwidget)
        self.herbe.setGeometry(QtCore.QRect(0, 0, 1031, 571))
        self.herbe.setText("")
        self.herbe.setPixmap(QtGui.QPixmap("../../../tests python/images_test/herbe_barriere.jpeg"))
        self.herbe.setScaledContents(True)
        self.herbe.setObjectName("herbe")
        self.tete_perso = QtWidgets.QLabel(self.centralwidget)
        self.tete_perso.setGeometry(QtCore.QRect(220, 180, 61, 51))
        self.tete_perso.setText("")
        self.tete_perso.setPixmap(QtGui.QPixmap("images/tete_perso.png"))
        self.tete_perso.setScaledContents(True)
        self.tete_perso.setObjectName("tete_perso")
        self.bouton_pokedeck = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_pokedeck.setGeometry(QtCore.QRect(930, 80, 71, 23))
        self.bouton_pokedeck.setObjectName("bouton_pokedeck")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(940, 10, 51, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/th-removebg-preview (2).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.herbe.raise_()
        self.bouton_pokedeck.raise_()
        self.label.raise_()
        self.tete_perso.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 21))
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
        self.bouton_pokedeck.setText(_translate("MainWindow", "Pokedeck"))
