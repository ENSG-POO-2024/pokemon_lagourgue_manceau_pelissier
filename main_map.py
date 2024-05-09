import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.QtGui import QPixmap
import gestion_des_pokemons.pokemons as  pok
from interface_graphique.map import Ui_map
from interface_graphique.ecran_accueil import Ui_ecran_accueil
from interface_graphique.pokedeck import Ui_pokedeck
from interface_graphique.rencontre_pokemon_sauvage import Ui_rencontre_pokemon_sauvage
from interface_graphique.choix_pokemon import Ui_choix_pokemon
from interface_graphique.choix_attaque import Ui_choix_attaque
from interface_graphique.fond_combat import Ui_fond_combat
from interface_graphique.ecran_triple import Ui_ecran_triple
import random as rand
import numpy as np
import pandas as pd


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # Utilisez la classe générée par Qt Designer
        self.ui = Ui_map()
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
        
        coord = [self.ui.tete_perso.pos().x(),self.ui.tete_perso.pos().y()]
        if self.detection(coord) != None:
            dialog = RencontreDlg()
            dialog.exec_()  # Affichez la boîte de dialogue de manière modale
            self.ui.tete_perso.setFocus()
                                 
    def calcul_distance_poke(self,coord,nom_poke):
        if pok.dico_poke[nom_poke].coordX == 'pokédeck':
            return 1000
        return np.sqrt((coord[0] - pok.dico_poke[nom_poke].coordX)**2 + (coord[1] - pok.dico_poke[nom_poke].coordY)**2)

    def detection(self,coord):
        distance_detection = 50
        for k in pok.liste_tous_poke:
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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_pokedeck()
        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.load_image)  # Connectez le signal de changement de sélection de la ComboBox
        
    def load_image(self):
        selected_item = self.ui.comboBox.currentText()
        for k in pok.liste_tous_poke:
            if selected_item == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap = QPixmap(image_path)
        self.ui.label_2.setPixmap(pixmap)
        self.ui.label_2.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
 
        
class RencontreDlg(QDialog):
    
    # corriger nom pokémon

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_rencontre_pokemon_sauvage()
        self.ui.setupUi(self)
        coord = [window.ui.tete_perso.pos().x(),window.ui.tete_perso.pos().y()]
        nom = window.detection(coord)
        for k in pok.liste_tous_poke:
            if nom == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap = QPixmap(image_path)
        self.ui.pokemon_sauvage.setPixmap(pixmap)
        self.ui.pokemon_sauvage.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
