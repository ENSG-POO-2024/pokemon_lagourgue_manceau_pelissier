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
from interface_graphique.fond_combat import Ui_arene_de_combat
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
            classe_rencontre = RencontreDlg()
            classe_rencontre.exec_()  # Affichez la boîte de dialogue de manière modale
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
        classe_pokedeck = PokedeckDlg()
        classe_pokedeck.exec_()  # Affichez la boîte de dialogue de manière modale
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
        self.ui.image_poke.setPixmap(pixmap)
        self.ui.image_poke.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
 
        
class RencontreDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_rencontre_pokemon_sauvage()
        self.ui.setupUi(self)
        coord = [window.ui.tete_perso.pos().x(),window.ui.tete_perso.pos().y()]
        pokemon_sauvage = window.detection(coord)
        self.pokemon_sauvage = pokemon_sauvage
        for k in pok.liste_tous_poke:
            if pokemon_sauvage == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap = QPixmap(image_path)
        self.ui.pokemon_sauvage.setPixmap(pixmap)
        self.ui.pokemon_sauvage.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
        self.ui.txt_poke_apparait.setText(f"Un {pokemon_sauvage} sauvage apparaît !")
        self.ui.bouton_fuir.clicked.connect(self.fuir) #relie l'action au bouton fuir
        self.ui.bouton_combattre.clicked.connect(self.open_dialog_choix_pokemon)  #relie l'action au bouton combattre
    
    def fuir(self):
        self.close() #retour à la mainWindow, la carte
        
    def open_dialog_choix_pokemon(self):
        classe_choix_pokemon = ChoixPokemonDlg(pokemon_sauvage=self.pokemon_sauvage)
        classe_choix_pokemon.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
   
        
class ChoixPokemonDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_sauvage='defaut'):
        super().__init__(parent)
        self.ui = Ui_choix_pokemon()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_sauvage = pokemon_sauvage
        self.ui.ComboBox_choix_pokemon.currentIndexChanged.connect(self.load_image) # Connectez le signal de changement de sélection de la ComboBox
        self.ui.ok.clicked.connect(self.open_next_dialog)
        
    def open_next_dialog(self):
        vitesse_poke_choisi = pok.dico_poke[self.ui.pokemon_choisi].speed 
        vitesse_poke_sauvage = pok.dico_poke[self.pokemon_sauvage].speed
        if vitesse_poke_choisi >= vitesse_poke_sauvage:
            print('attaque')
            classe_choix_attaque = ChoixAttaqueDlg(pokemon_choisi=self.ui.pokemon_choisi,pokemon_sauvage=self.pokemon_sauvage)
            classe_choix_attaque.exec_()  # Affichez la boîte de dialogue de manière modale
            self.close()
            window.ui.tete_perso.setFocus()
        else:
            print('fond combat')
            classe_fond_combat = FondCombatDlg(pokemon_choisi=self.ui.pokemon_choisi,pokemon_sauvage=self.pokemon_sauvage)
            classe_fond_combat.exec_()  # Affichez la boîte de dialogue de manière modale
            self.close()
            window.ui.tete_perso.setFocus()
        
    def load_image(self):
        selected_item = self.ui.ComboBox_choix_pokemon.currentText()
        for k in pok.liste_tous_poke:
            if selected_item == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap = QPixmap(image_path)
        self.ui.image_pokemon.setPixmap(pixmap)
        self.ui.image_pokemon.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
        self.ui.pokemon_choisi = self.ui.ComboBox_choix_pokemon.currentText()
        
        
        
class ChoixAttaqueDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut',pokemon_sauvage='défaut'):
        super().__init__(parent)
        self.ui = Ui_choix_attaque()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.ui.nbr_degat_att_neutre.setText(f"")
        self.ui.nbr_degat_att_spe.setText(f"")
        

class FondCombatDlg(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_fond_combat()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        


"""
        self.ui.bouton_fuir.clicked.connect(self.close)
        self.ui.bouton_attaque.clicked.connect(self.attaquer)
        self.ui.bouton_changer_pokemon.clicked.connect(self.changer)
        
        
    def changer(self):
        pass
            
    def attaquer(self):
        pass

"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
