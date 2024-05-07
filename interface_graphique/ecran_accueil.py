# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecran_accueil.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.perso = QtWidgets.QLabel(self.centralwidget)
        self.perso.setGeometry(QtCore.QRect(500, 100, 281, 461))
        self.perso.setText("")
        self.perso.setPixmap(QtGui.QPixmap("images/perso_entier.png"))
        self.perso.setScaledContents(True)
        self.perso.setObjectName("perso")
        self.titre_pokemon = QtWidgets.QLabel(self.centralwidget)
        self.titre_pokemon.setGeometry(QtCore.QRect(60, 20, 381, 321))
        self.titre_pokemon.setText("")
        self.titre_pokemon.setPixmap(QtGui.QPixmap("images/titre_pokemon.png"))
        self.titre_pokemon.setScaledContents(True)
        self.titre_pokemon.setObjectName("titre_pokemon")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(100, 290, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(67)
        self.play.setFont(font)
        self.play.setAutoFillBackground(False)
        self.play.setObjectName("play")
        self.aquali = QtWidgets.QLabel(self.centralwidget)
        self.aquali.setGeometry(QtCore.QRect(80, 420, 91, 91))
        self.aquali.setAutoFillBackground(False)
        self.aquali.setText("")
        self.aquali.setPixmap(QtGui.QPixmap("images/images_pokemon/Aquali-RFVF-removebg-preview.png"))
        self.aquali.setScaledContents(True)
        self.aquali.setObjectName("aquali")
        self.jigglypuff = QtWidgets.QLabel(self.centralwidget)
        self.jigglypuff.setGeometry(QtCore.QRect(210, 420, 101, 91))
        self.jigglypuff.setText("")
        self.jigglypuff.setPixmap(QtGui.QPixmap("images/images_pokemon/jigglypuff.png"))
        self.jigglypuff.setScaledContents(True)
        self.jigglypuff.setObjectName("jigglypuff")
        self.oddish = QtWidgets.QLabel(self.centralwidget)
        self.oddish.setGeometry(QtCore.QRect(340, 410, 101, 101))
        self.oddish.setText("")
        self.oddish.setPixmap(QtGui.QPixmap("images/images_pokemon/oddish.png"))
        self.oddish.setScaledContents(True)
        self.oddish.setObjectName("oddish")
        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.fond.setText("")
        self.fond.setPixmap(QtGui.QPixmap("images/prairie_et_ciel.png"))
        self.fond.setScaledContents(True)
        self.fond.setObjectName("fond")
        self.fond.raise_()
        self.perso.raise_()
        self.titre_pokemon.raise_()
        self.play.raise_()
        self.aquali.raise_()
        self.jigglypuff.raise_()
        self.oddish.raise_()
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play.setText(_translate("MainWindow", "Play"))