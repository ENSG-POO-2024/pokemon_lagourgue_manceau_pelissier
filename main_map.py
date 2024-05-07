# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:26:24 2024

@author: loeva
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi  # Importez la fonction loadUi pour charger le fichier UI
from gestion_des_pokemons.pokemons import  *
from interface_graphique.map import Ui_MainWindow
from interface_graphique.pokedeck import Ui_pokedeck
from interface_graphique.choix_attaque import Ui_Dialog as Choix_attaques_diag
from interface_graphique.ecran_triple import Ui_Dialog as Ecran_triple_diag

import random as rand


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Utilisez la classe générée par Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connectez les signaux et les slots pour gérer les événements de clavier
        self.ui.tete_perso.setFocus()  # Assurez-vous que le QLabel du perso a le focus pour recevoir les événements de clavier
        self.ui.tete_perso.installEventFilter(self)
        
        #loadUi("map.ui", self)  # Chargez le fichier UI de la fenêtre principale
        # Connectez le bouton pour ouvrir la boîte de dialogue
        self.ui.bouton_pokedeck.clicked.connect(self.open_dialog_Pokedeck)
        

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Left:
                self.move_square(-10, 0)
                return True
            elif key == Qt.Key_Right:
                self.move_square(10, 0)
                return True
            elif key == Qt.Key_Up:
                self.move_square(0, -10)
                return True
            elif key == Qt.Key_Down:
                self.move_square(0, 10)
                return True
        return super().eventFilter(source, event)

    def move_square(self, dx, dy):
        square_pos = self.ui.tete_perso.pos()
        new_pos = square_pos + QPoint(dx, dy)
    
        # Récupérer les dimensions de l'image
        image_width = self.ui.herbe.width()
        image_height = self.ui.herbe.height()
    
        # Récupérer les dimensions du carré
        square_width = self.ui.tete_perso.width()
        square_height = self.ui.tete_perso.height()
    
        # Limites de déplacement
        min_x = 0
        max_x = image_width - square_width
        min_y = 0
        max_y = image_height - square_height  # Prend en compte la hauteur du carré
    
        # Vérifier les limites de déplacement
        new_pos.setX(max(min(new_pos.x(), max_x), min_x))
        new_pos.setY(max(min(new_pos.y(), max_y), min_y))
    
        # Déplacer le carré
        self.ui.tete_perso.move(new_pos)
        
        #récuperer les coord du perso
        tete_perso_pos = self.ui.tete_perso.pos()
        #print("Coordonnées du carré : ", tete_perso_pos.x(), tete_perso_pos.y())
        
        if self.detection([tete_perso_pos.x(),tete_perso_pos.y()]) != None:
            print('detecté !!!!')
            
            
    def calcul_distance_poke(self,coord,nom_poke):
        if dico_poke[nom_poke].coordX == 'pokédeck':
            return 1000
        return np.sqrt((coord[0] - dico_poke[nom_poke].coordX)**2 + (coord[1] - dico_poke[nom_poke].coordY)**2)
        

    def detection(self,coord):
        distance_detection = 50
        for k in liste_tous_poke:
            dist = self.calcul_distance_poke(coord,k)
            if dist <= distance_detection:
                return k
        return None
        
    def open_dialog_Pokedeck(self):
        # Créez une instance de la boîte de dialogue
        dialog = PokedeckDlg()
        dialog.exec_()  # Affichez la boîte de dialogue de manière modale
        self.ui.tete_perso.setFocus()


class PokedeckDlg(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("interface_graphique/pokedeck.ui", self)  # Chargez le fichier UI de la boîte de dialogue
        self.comboBox.currentIndexChanged.connect(self.load_image)  # Connectez le signal de changement de sélection de la ComboBox

    def load_image(self, index):
        selected_item = self.comboBox.currentText()
        if selected_item == "Bulbasaur":
            image_path = "interface_graphique/images/images_pokemon/pokemons_finaux/face/Bulbasaur.png" # Chemin vers l'image 1
        elif selected_item == "Squirtle":
            image_path = "interface_graphique/images/images_pokemon/pokemons_finaux/face/Squirtle.png"  # Chemin vers l'image 2
            
        pixmap = QPixmap(image_path)
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)  # Ajustez la taille de l'image au QLabel




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
