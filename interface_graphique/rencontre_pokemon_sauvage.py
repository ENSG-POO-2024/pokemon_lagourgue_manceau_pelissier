# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rencontre_pokemon_sauvage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rencontre_pokemon_sauvage(object):
    def setupUi(self, rencontre_pokemon_sauvage):
        rencontre_pokemon_sauvage.setObjectName("rencontre_pokemon_sauvage")
        rencontre_pokemon_sauvage.resize(442, 297)
        self.fond_prairie = QtWidgets.QLabel(rencontre_pokemon_sauvage)
        self.fond_prairie.setGeometry(QtCore.QRect(-10, -20, 451, 321))
        self.fond_prairie.setText("")
        self.fond_prairie.setPixmap(QtGui.QPixmap("images/prairie_et_ciel.png"))
        self.fond_prairie.setObjectName("fond_prairie")
        self.pokemon_sauvage = QtWidgets.QLabel(rencontre_pokemon_sauvage)
        self.pokemon_sauvage.setGeometry(QtCore.QRect(60, 90, 161, 161))
        self.pokemon_sauvage.setText("")
        self.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/images_pokemon/pokemons_finaux/face/Diglett.png"))
        self.pokemon_sauvage.setScaledContents(True)
        self.pokemon_sauvage.setObjectName("pokemon_sauvage")
        self.perso_qui_court = QtWidgets.QLabel(rencontre_pokemon_sauvage)
        self.perso_qui_court.setGeometry(QtCore.QRect(260, -30, 181, 331))
        self.perso_qui_court.setText("")
        self.perso_qui_court.setPixmap(QtGui.QPixmap("images/perso_attaque.png"))
        self.perso_qui_court.setScaledContents(True)
        self.perso_qui_court.setObjectName("perso_qui_court")
        self.bouton_fuir = QtWidgets.QPushButton(rencontre_pokemon_sauvage)
        self.bouton_fuir.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.bouton_fuir.setObjectName("bouton_fuir")
        self.bouton_combattre = QtWidgets.QPushButton(rencontre_pokemon_sauvage)
        self.bouton_combattre.setGeometry(QtCore.QRect(120, 250, 91, 23))
        self.bouton_combattre.setObjectName("bouton_combattre")
        self.txt_poke_apparait = QtWidgets.QLabel(rencontre_pokemon_sauvage)
        self.txt_poke_apparait.setGeometry(QtCore.QRect(20, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.txt_poke_apparait.setFont(font)
        self.txt_poke_apparait.setAutoFillBackground(True)
        self.txt_poke_apparait.setObjectName("txt_poke_apparait")

        self.retranslateUi(rencontre_pokemon_sauvage)
        QtCore.QMetaObject.connectSlotsByName(rencontre_pokemon_sauvage)

    def retranslateUi(self, rencontre_pokemon_sauvage):
        _translate = QtCore.QCoreApplication.translate
        rencontre_pokemon_sauvage.setWindowTitle(_translate("rencontre_pokemon_sauvage", "Dialog"))
        self.bouton_fuir.setText(_translate("rencontre_pokemon_sauvage", "fuir"))
        self.bouton_combattre.setText(_translate("rencontre_pokemon_sauvage", "COMBATTRE !"))
        self.txt_poke_apparait.setText(_translate("rencontre_pokemon_sauvage", "Un nom_pokémon sauvage apparaît !"))
