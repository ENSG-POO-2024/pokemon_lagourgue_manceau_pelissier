# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choix_attaque.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Choix_attaque(object):
    def setupUi(self, Choix_attaque):
        Choix_attaque.setObjectName("Choix_attaque")
        Choix_attaque.resize(741, 212)
        self.image_fond = QtWidgets.QLabel(Choix_attaque)
        self.image_fond.setGeometry(QtCore.QRect(-10, -30, 831, 591))
        self.image_fond.setText("")
        self.image_fond.setPixmap(QtGui.QPixmap("images/prairie_et_ciel.png"))
        self.image_fond.setScaledContents(True)
        self.image_fond.setObjectName("image_fond")
        self.bouton_att_spe = QtWidgets.QPushButton(Choix_attaque)
        self.bouton_att_spe.setGeometry(QtCore.QRect(40, 60, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(20)
        self.bouton_att_spe.setFont(font)
        self.bouton_att_spe.setObjectName("bouton_att_spe")
        self.bouton_att_neutre = QtWidgets.QPushButton(Choix_attaque)
        self.bouton_att_neutre.setGeometry(QtCore.QRect(380, 60, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(20)
        self.bouton_att_neutre.setFont(font)
        self.bouton_att_neutre.setObjectName("bouton_att_neutre")
        self.txt_degats_att_spe = QtWidgets.QLabel(Choix_attaque)
        self.txt_degats_att_spe.setGeometry(QtCore.QRect(50, 150, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_degats_att_spe.setFont(font)
        self.txt_degats_att_spe.setAutoFillBackground(False)
        self.txt_degats_att_spe.setObjectName("txt_degats_att_spe")
        self.nbr_degat_att_spe = QtWidgets.QLabel(Choix_attaque)
        self.nbr_degat_att_spe.setGeometry(QtCore.QRect(190, 150, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nbr_degat_att_spe.setFont(font)
        self.nbr_degat_att_spe.setObjectName("nbr_degat_att_spe")
        self.txt_degats_att_neutre = QtWidgets.QLabel(Choix_attaque)
        self.txt_degats_att_neutre.setGeometry(QtCore.QRect(380, 150, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_degats_att_neutre.setFont(font)
        self.txt_degats_att_neutre.setAutoFillBackground(False)
        self.txt_degats_att_neutre.setObjectName("txt_degats_att_neutre")
        self.nbr_degat_att_neutre = QtWidgets.QLabel(Choix_attaque)
        self.nbr_degat_att_neutre.setGeometry(QtCore.QRect(520, 150, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nbr_degat_att_neutre.setFont(font)
        self.nbr_degat_att_neutre.setObjectName("nbr_degat_att_neutre")
        self.image_fond.raise_()
        self.bouton_att_spe.raise_()
        self.bouton_att_neutre.raise_()
        self.txt_degats_att_spe.raise_()
        self.txt_degats_att_neutre.raise_()
        self.nbr_degat_att_spe.raise_()
        self.nbr_degat_att_neutre.raise_()

        self.retranslateUi(Choix_attaque)
        QtCore.QMetaObject.connectSlotsByName(Choix_attaque)

    def retranslateUi(self, Choix_attaque):
        _translate = QtCore.QCoreApplication.translate
        Choix_attaque.setWindowTitle(_translate("Choix_attaque", "Dialog"))
        self.bouton_att_spe.setText(_translate("Choix_attaque", "Attaque spéciale"))
        self.bouton_att_neutre.setText(_translate("Choix_attaque", "Attaque neutre"))
        self.txt_degats_att_spe.setText(_translate("Choix_attaque", "Dégats inffligés :              HP"))
        self.nbr_degat_att_spe.setText(_translate("Choix_attaque", "XX"))
        self.txt_degats_att_neutre.setText(_translate("Choix_attaque", "Dégats inffligés :              HP"))
        self.nbr_degat_att_neutre.setText(_translate("Choix_attaque", "YY"))
