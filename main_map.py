import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.QtGui import QPixmap
import gestion_des_pokemons.pokemons as pok
from interface_graphique.map import Ui_map
from interface_graphique.ecran_accueil import Ui_ecran_accueil
from interface_graphique.pokedeck import Ui_pokedeck
from interface_graphique.rencontre_pokemon_sauvage import Ui_rencontre_pokemon_sauvage
from interface_graphique.choix_pokemon import Ui_choix_pokemon
from interface_graphique.choix_attaque import Ui_choix_attaque
from interface_graphique.fond_combat import Ui_arene_de_combat
from interface_graphique.ecran_triple import Ui_ecran_triple
from interface_graphique.capture_pokemon import Ui_capture
import random as rd
import numpy as np
import pandas as pd
import time


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
        
        debut = time.time()
        if time.time()-debut < 1:
            classe_ecran_accueil = EcranAccueilDlg()
            classe_ecran_accueil.exec_()  # Affichez la boîte de dialogue de manière modale
            self.ui.tete_perso.setFocus()
        
    def eventFilter(self, source, event):
        """
        Repère quand on appuie sur les touches du clavier

        Parameters
        ----------
        source : TYPE
            DESCRIPTION.
        event : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE: boolean
            DESCRIPTION.

        """
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
        """
        Affiche le déplacement du personnage dans les limites de l'image

        Parameters
        ----------
        dx : TYPE
            DESCRIPTION.
        dy : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
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
        """
        Calcule la distance entre chaque pokemon présents et le personnage

        Parameters
        ----------
        coord : TYPE liste
            DESCRIPTION. contient l'ordonnée et l'abscisse du personnage
        nom_poke : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if pok.dico_poke[nom_poke].coordX == 'pokédeck':
            return 1000
        return np.sqrt((coord[0] - pok.dico_poke[nom_poke].coordX)**2 + (coord[1] - pok.dico_poke[nom_poke].coordY)**2)

    def detection(self,coord):
        """
        Cherche si le personnage est dans la zone de détection

        Parameters
        ----------
        coord : TYPE liste
            DESCRIPTION.

        Returns
        -------
        k : TYPE 
            DESCRIPTION. nom du pokémon

        """
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
        
        
class EcranAccueilDlg(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ecran_accueil()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.open_carte)
        
    def open_carte(self):
        self.close()
        

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
        self.sauvageHP = pok.dico_poke[self.pokemon_sauvage].HP
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
        classe_choix_pokemon = ChoixPokemonDlg(pokemon_sauvage=self.pokemon_sauvage, sauvageHP=self.sauvageHP,
                                               ini_sauv_HP=self.sauvageHP, debut=True)
        classe_choix_pokemon.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
   
        
class ChoixPokemonDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_sauvage='défaut', sauvageHP='défaut', ini_sauv_HP='défaut', debut='défaut'):
        super().__init__(parent)
        self.ui = Ui_choix_pokemon()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_sauvage = pokemon_sauvage
        self.sauvageHP = sauvageHP
        self.ini_sauv_HP = ini_sauv_HP
        self.debut = debut
        self.ui.pokemon_choisi = 'Bulbasaur'
        self.ui.choisiHP = pok.dico_poke[self.ui.pokemon_choisi].HP
        self.ui.ComboBox_choix_pokemon.currentIndexChanged.connect(self.load_image_change_poke_choisi) # Connectez le signal de changement de sélection de la ComboBox
        self.ui.ok.clicked.connect(self.open_next_dialog)
    
    def load_image_change_poke_choisi(self):
        selected_item = self.ui.ComboBox_choix_pokemon.currentText()
        for k in pok.liste_tous_poke:
            if selected_item == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap = QPixmap(image_path)
        self.ui.image_pokemon.setPixmap(pixmap)
        self.ui.image_pokemon.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
        self.ui.pokemon_choisi = self.ui.ComboBox_choix_pokemon.currentText()
        self.ui.choisiHP = pok.dico_poke[self.ui.pokemon_choisi].HP
            
    def open_next_dialog(self):
        if self.debut:
            vitesse_poke_choisi = pok.dico_poke[self.ui.pokemon_choisi].speed 
            vitesse_poke_sauvage = pok.dico_poke[self.pokemon_sauvage].speed
            if vitesse_poke_choisi >= vitesse_poke_sauvage:
                classe_choix_attaque = ChoixAttaqueDlg(pokemon_choisi=self.ui.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                                       choisiHP=self.ui.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ui.choisiHP,
                                                       ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi')
                classe_choix_attaque.exec_()  # Affichez la boîte de dialogue de manière modale
                self.close()
                window.ui.tete_perso.setFocus()
            else:
                classe_fond_combat = FondCombatDlg(pokemon_choisi=self.ui.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                                   choisiHP=self.ui.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ui.choisiHP,
                                                   ini_sauv_HP=self.ini_sauv_HP,debut=False, tour='sauvage', nb_degats='reçus')
                classe_fond_combat.exec_()  # Affichez la boîte de dialogue de manière modale
                self.close()
                window.ui.tete_perso.setFocus()
        else:
            classe_fond_combat = FondCombatDlg(pokemon_choisi=self.ui.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                               choisiHP=self.ui.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ui.choisiHP,
                                               ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='sauvage', nb_degats='reçus')
            classe_fond_combat.exec_()  # Affichez la boîte de dialogue de manière modale
            self.close()
            window.ui.tete_perso.setFocus()
            
                
class ChoixAttaqueDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut', pokemon_sauvage='défaut', choisiHP='défaut', sauvageHP='défaut',
                 ini_choi_HP='défaut', ini_sauv_HP='défaut', debut='défaut', tour='défaut'):
        super().__init__(parent)
        self.ui = Ui_choix_attaque()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.choisiHP = choisiHP
        self.sauvageHP = sauvageHP
        self.ini_choi_HP = ini_choi_HP
        self.ini_sauv_HP = ini_sauv_HP
        obj_pokemon_choisi = pok.dico_poke[self.pokemon_choisi]
        obj_pokemon_sauvage = pok.dico_poke[self.pokemon_sauvage]
        self.attaque_neutre = pok.Caracteristiques_Pokemon.pts_attaque_neutre(obj_pokemon_choisi,obj_pokemon_sauvage)
        self.attaque_spe = pok.Caracteristiques_Pokemon.pts_attaque_spe(obj_pokemon_choisi,obj_pokemon_sauvage)
        self.ui.nbr_degat_att_neutre.setText(f"{self.attaque_neutre}")
        self.ui.nbr_degat_att_spe.setText(f"{self.attaque_spe}")
        self.ui.bouton_att_neutre.clicked.connect(self.open_dialog_atk_neutre)
        self.ui.bouton_att_spe.clicked.connect(self.open_dialog_atk_spe)
        
    def open_dialog_atk_neutre(self):
        classe_fond_combat = FondCombatDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi', nb_degats=self.attaque_neutre)
        classe_fond_combat.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
        
    def open_dialog_atk_spe(self):
        classe_fond_combat = FondCombatDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi', nb_degats=self.attaque_spe)
        classe_fond_combat.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
        
        
class FondCombatDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut', pokemon_sauvage='défaut', choisiHP='défaut', sauvageHP='défaut',
                 ini_choi_HP='défaut', ini_sauv_HP='défaut', debut='défaut', tour='défaut', nb_degats= 'défaut'):
        super().__init__(parent)
        self.ui = Ui_arene_de_combat()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.choisiHP = choisiHP
        self.sauvageHP = sauvageHP
        self.ini_choi_HP = ini_choi_HP
        self.ini_sauv_HP = ini_sauv_HP
        self.nb_degats = nb_degats
        obj_pokemon_choisi = pok.dico_poke[self.pokemon_choisi]
        obj_pokemon_sauvage = pok.dico_poke[self.pokemon_sauvage]
        self.ui.nom_mon_pokemon.setText(f"{self.pokemon_choisi}")
        self.ui.nom_pokemon_sauvage.setText(f"{self.pokemon_sauvage}")
        for k in pok.liste_tous_poke:
            if self.pokemon_choisi == k:
                image_path_choisi = f"interface_graphique/images/images_pokemon/pokemons_finaux/dos/{k}.png" # Chemin vers l'image
            if self.pokemon_sauvage == k:
                image_path_sauvage = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap_choisi = QPixmap(image_path_choisi)
        pixmap_sauvage = QPixmap(image_path_sauvage)
        self.ui.img_mon_pokemon.setPixmap(pixmap_choisi)
        self.ui.img_mon_pokemon.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
        self.ui.img_pokemon_sauvage.setPixmap(pixmap_sauvage)
        self.ui.img_pokemon_sauvage.setScaledContents(True)# Ajustez la taille de l'image au QLabel
        self.ui.barre_vie_mon_pokemon.setMaximum(self.ini_choi_HP)
        self.ui.barre_vie_pokemon_sauvage.setMaximum(self.ini_sauv_HP)
        self.ui.barre_vie_mon_pokemon.setProperty("value",f"{self.choisiHP}")
        self.ui.barre_vie_pokemon_sauvage.setProperty("value",f"{self.sauvageHP}")
        
        # Cas où c'est à notre tour de jouer
        if tour == 'choisi':
            self.sauvageHP -= self.nb_degats
            # Cas où le pokémon sauvage a encore des PV : le combat continue
            if self.sauvageHP > 0:
                self.ui.txt_descriptif.setText(f"{self.pokemon_choisi} attaque ! {self.pokemon_sauvage} perd {self.nb_degats} HP !")
                self.ui.barre_vie_pokemon_sauvage.setProperty("value",f"{self.sauvageHP}")
                self.ui.continuer.clicked.connect(self.open_dialog_fond_combat)
            # Cas où le pokémon sauvage n'a plus de PV : combat gagné
            if self.sauvageHP <= 0:
                self.ui.txt_descriptif.setText(f"{self.pokemon_sauvage} est KO ! Le combat est gagné !")
                self.ui.barre_vie_pokemon_sauvage.setProperty("value",0)
                self.ui.continuer.clicked.connect(self.open_dialog_capture_pokemon)
                
        # Cas où c'est au tour du pokémon sauvage de jouer
        if tour == 'sauvage':
            if rd.random() < 0.5:
                self.nb_degats = pok.Caracteristiques_Pokemon.pts_attaque_neutre(obj_pokemon_sauvage,obj_pokemon_choisi)
            else:
                self.nb_degats = pok.Caracteristiques_Pokemon.pts_attaque_spe(obj_pokemon_sauvage,obj_pokemon_choisi)
            self.choisiHP -= self.nb_degats
            # Cas où notre pokemon a encore des PV : le combat continue
            if self.choisiHP > 0:
                self.ui.txt_descriptif.setText(f"{self.pokemon_sauvage} attaque ! {self.pokemon_choisi} perd {self.nb_degats} HP !")
                self.ui.barre_vie_mon_pokemon.setProperty("value",f"{self.choisiHP}")
                self.ui.continuer.clicked.connect(self.open_dialog_ecran_triple)
            # Cas où notre pokémon n'a plus de PV : combat perdu
            if self.choisiHP <= 0:
                self.ui.txt_descriptif.setText(f"{self.pokemon_choisi} est KO ! Le combat est perdu !")
                self.ui.barre_vie_mon_pokemon.setProperty("value",0)
                self.ui.continuer.clicked.connect(self.retour_carte)
                
    def open_dialog_fond_combat(self):
        classe_fond_combat = FondCombatDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='sauvage', nb_degats='reçus')
        classe_fond_combat.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
    
    def open_dialog_ecran_triple(self):
        classe_ecran_triple = EcranTripleDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi')
        classe_ecran_triple.exec_()
        self.close()
        window.ui.tete_perso.setFocus()
        
    def open_dialog_capture_pokemon(self):
        classe_capture_pokemon = CapturePokemonDlg(pokemon_sauvage=self.pokemon_sauvage)
        classe_capture_pokemon.exec_()
        self.close()
        window.ui.tete_perso.setFocus()
    
    def retour_carte(self):
        self.close()
    

class EcranTripleDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut', pokemon_sauvage='défaut', choisiHP='défaut', sauvageHP='défaut',
                 ini_choi_HP='défaut', ini_sauv_HP='défaut', debut='défaut', tour='défaut'):
        super().__init__(parent)
        self.ui = Ui_ecran_triple()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.choisiHP= choisiHP
        self.sauvageHP = sauvageHP
        self.ini_choi_HP = ini_choi_HP
        self.ini_sauv_HP = ini_sauv_HP
        self.ui.bouton_fuir.clicked.connect(self.fuir)
        self.ui.bouton_attaque.clicked.connect(self.open_dialog_choix_attaque)
        self.ui.bouton_changer_pokemon.clicked.connect(self.open_dialog_choix_pokemon)

    def open_dialog_choix_attaque(self):
        classe_choix_attaque = ChoixAttaqueDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                               choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                               ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi')
        classe_choix_attaque.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
        
    def open_dialog_choix_pokemon(self):
        classe_choix_pokemon = ChoixPokemonDlg(pokemon_sauvage=self.pokemon_sauvage, sauvageHP=self.sauvageHP,
                                               ini_sauv_HP=self.sauvageHP, debut=False)
        classe_choix_pokemon.exec_()  # Affichez la boîte de dialogue de manière modale
        self.close()
        window.ui.tete_perso.setFocus()
        
    def fuir(self):
        self.close()


class CapturePokemonDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_sauvage='défaut'):
        super().__init__(parent)
        self.ui = Ui_capture()
        self.ui.setupUi(self) #l'argument self est utilisé comme widget parent
        self.pokemon_sauvage = pokemon_sauvage
        self.ui.titre.setText(f"{pokemon_sauvage} est capturé !")
        for k in pok.liste_tous_poke:
            if pokemon_sauvage == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png" # Chemin vers l'image
        pixmap = QPixmap(image_path)
        self.ui.pokemon_capture.setPixmap(pixmap)
        self.ui.pokemon_capture.setScaledContents(True)  # Ajustez la taille de l'image au QLabel
        pok.liste_pokedeck.append(pokemon_sauvage)
        ligne_coord = np.array([pokemon_sauvage,'pokédeck','pokédeck','pokédeck','pokédeck'])
        pok.dico_poke[ligne_coord[0]] = pok.Pokemon(ligne_coord)
        self.ui.ok.clicked.connect(self.retour_carte)
    
    def retour_carte(self):
        self.close()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
"""
voir points attaque
separer classes
remettre au propre
documenter code
voir rapport
"""
