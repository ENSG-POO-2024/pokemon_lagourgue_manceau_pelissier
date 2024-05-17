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
from interface_graphique.ecran_final import Ui_ecran_final
import random as rd
import numpy as np
import time


class MapMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_map()
        self.ui.setupUi(self)

        # Mettre le focus sur le personnage pour recevoir les évènements de clavier
        self.ui.tete_perso.setFocus()
        
        # Détecter les évènements de clavier
        self.ui.tete_perso.installEventFilter(self)

        # Bouton pokédeck qui ouvre la boîte de dialogue Pokédeck
        self.ui.bouton_pokedeck.clicked.connect(self.open_dialog_Pokedeck)
        
        # Ouvrir la boîte de dialogue de l'écran d'accueil au début du jeu
        debut = time.time()
        if time.time()-debut < 1:
            classe_ecran_accueil = EcranAccueilDlg()
            classe_ecran_accueil.exec_()
            # Remettre le focus sur le personnage après avoir fermé la fenêtre de l'écran d'accueil
            self.ui.tete_perso.setFocus()
        
        
    def eventFilter(self, source, event):
        """
        Détecte quand on appuie sur les touches du clavier et lance la fonction de
        déplacement du personnage
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
        Affiche le déplacement du personnage (représenté par un carré) dans les 
        limites de l'image et change ses coordonnées
        """
        # Définir la nouvelle position du carré
        square_pos = self.ui.tete_perso.pos()
        new_pos = square_pos + QPoint(dx, dy)
    
        # Récupérer les dimensions de l'image
        image_width = self.ui.herbe.width()
        image_height = self.ui.herbe.height()
    
        # Récupérer les dimensions du carré
        square_width = self.ui.tete_perso.width()
        square_height = self.ui.tete_perso.height()
    
        # Limites de déplacement (en prenant en compte la hauteur du carré)
        min_x = 0
        max_x = image_width - square_width
        min_y = 0
        max_y = image_height - square_height
    
        # Vérifier les limites de déplacement
        new_pos.setX(max(min(new_pos.x(), max_x), min_x))
        new_pos.setY(max(min(new_pos.y(), max_y), min_y))
    
        # Déplacer le carré
        self.ui.tete_perso.move(new_pos)
        
        # Récuperer les coordonnées du perso
        coord = [self.ui.tete_perso.pos().x(),self.ui.tete_perso.pos().y()]
        
        # Ouvrir la boîte de dialogue de la rencontre d'un pokémon sauvage si un pokémon
        # sauvage est détecté
        if self.detection(coord) != None:
            classe_rencontre = RencontreDlg()
            classe_rencontre.exec_()
            # Remettre le focus sur le personnage après avoir fermé la fenêtre
            self.ui.tete_perso.setFocus()
                                 
    def calcul_distance_poke(self,coord,nom_poke):
        """
        Calcule la distance entre un pokemon et le personnage

        Parameters
        ----------
        coord : coordonnées du personnage
                type : list
        nom_poke : nom du pokémon
                type : str

        Returns
        -------
        dist : distance entre un pokemon et le personnage
                type : float
        1000 : retourne 1000 si le pokémon est dans le pokédeck
                (pour qu'il ne soit pas détecté)

        """
        if pok.dico_poke[nom_poke].coordX == 'pokédeck':
            return 1000
        dist = np.sqrt((coord[0] - pok.dico_poke[nom_poke].coordX)**2 + (coord[1] - pok.dico_poke[nom_poke].coordY)**2)
        return dist

    def detection(self,coord):
        """
        Cherche si le personnage est dans la zone de détection d'un pokémon

        Parameters
        ----------
        coord : coordonnées du personnage
                type : list

        Returns
        -------
        k : nom du pokémon détecté
                type : str
        None : retourne None si aucun pokémon n'est détecté

        """
        distance_detection = 50
        for k in pok.liste_tous_poke:
            dist = self.calcul_distance_poke(coord,k)
            if dist <= distance_detection:
                return k
        return None
    
    def open_dialog_Pokedeck(self):
        """
        Ouvre la boîte de dialogue Pokédeck
        """
        classe_pokedeck = PokedeckDlg()
        classe_pokedeck.exec_()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        self.ui.tete_perso.setFocus()
        
        
class EcranAccueilDlg(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_ecran_accueil()
        self.ui.setupUi(self)
        
        # Bouton Play qui renvoie à l'écran principal (la carte)
        self.ui.play.clicked.connect(self.open_carte)
        
    def open_carte(self):
        """
        Renvoie à la carte
        """
        self.close()
        

class PokedeckDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_pokedeck()
        self.ui.setupUi(self)
        
        # Changer l'image du pokémon affiché en fonction de celui sélectionné dans 
        # le menu déroulant
        self.ui.comboBox.currentIndexChanged.connect(self.load_image)
        
    def load_image(self):
        """
        Change l'image affichée pour correspondre au pokémon sélectionné
        """
        selected_item = self.ui.comboBox.currentText()
        for k in pok.liste_tous_poke:
            if selected_item == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png"
        pixmap = QPixmap(image_path)
        self.ui.image_poke.setPixmap(pixmap)
        self.ui.image_poke.setScaledContents(True)
     
        
class RencontreDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_rencontre_pokemon_sauvage()
        self.ui.setupUi(self)
        
        # Récupérer le nom du pokémon sauvage détecté et ses HP
        coord = [window.ui.tete_perso.pos().x(),window.ui.tete_perso.pos().y()]
        pokemon_sauvage = window.detection(coord)
        self.pokemon_sauvage = pokemon_sauvage
        self.sauvageHP = pok.dico_poke[self.pokemon_sauvage].HP
        
        # Afficher l'image correspondante
        for k in pok.liste_tous_poke:
            if pokemon_sauvage == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png"
        pixmap = QPixmap(image_path)
        self.ui.pokemon_sauvage.setPixmap(pixmap)
        self.ui.pokemon_sauvage.setScaledContents(True)
        
        # Afficher le texte "Un {pokemon_sauvage} sauvage apparaît !" avec le nom du pokémon
        self.ui.txt_poke_apparait.setText(f"Un {pokemon_sauvage} sauvage apparaît !")
        
        # Bouton Fuir qui permet de retourner sur la carte
        self.ui.bouton_fuir.clicked.connect(self.fuir)
        
        # Bouton COMBATTRE ! qui ouvre la boîte de dialogue Choix Pokémon
        self.ui.bouton_combattre.clicked.connect(self.open_dialog_choix_pokemon)
    
    def fuir(self):
        """
        Renvoie à la carte
        """
        self.close()
        
    def open_dialog_choix_pokemon(self):
        """
        Ouvre la boîte de dialogue Choix Pokémon
        """
        classe_choix_pokemon = ChoixPokemonDlg(pokemon_sauvage=self.pokemon_sauvage, sauvageHP=self.sauvageHP,
                                               ini_sauv_HP=self.sauvageHP, debut=True)
        classe_choix_pokemon.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
   
        
class ChoixPokemonDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_sauvage='défaut', sauvageHP='défaut', ini_sauv_HP='défaut', debut='défaut'):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_choix_pokemon()
        self.ui.setupUi(self)
        
        # Récupérer les paramètres de la fonction
        self.pokemon_sauvage = pokemon_sauvage
        self.sauvageHP = sauvageHP
        self.ini_sauv_HP = ini_sauv_HP
        self.debut = debut
        
        # Récupérer le nom du pokémon choisi et ses HP en fonction de celui choisi
        # dans le menu déroulant et afficher l'image correspondante
        self.ui.pokemon_choisi = 'Bulbasaur'
        self.ui.choisiHP = pok.dico_poke[self.ui.pokemon_choisi].HP
        self.ui.ComboBox_choix_pokemon.currentIndexChanged.connect(self.load_image_change_poke_choisi)
        
        # Bouton OK qui ouvre la boîte de dialogue suivante
        self.ui.ok.clicked.connect(self.open_next_dialog)
    
    def load_image_change_poke_choisi(self):
        """
        Change l'image affichée pour correspondre au pokémon sélectionné, et renvoie
        les HP du pokémon selectionné
        """
        selected_item = self.ui.ComboBox_choix_pokemon.currentText()
        for k in pok.liste_tous_poke:
            if selected_item == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png"
        pixmap = QPixmap(image_path)
        self.ui.image_pokemon.setPixmap(pixmap)
        self.ui.image_pokemon.setScaledContents(True)
        self.ui.pokemon_choisi = self.ui.ComboBox_choix_pokemon.currentText()
        self.ui.choisiHP = pok.dico_poke[self.ui.pokemon_choisi].HP
            
    def open_next_dialog(self):
        """
        Ouvre la boîte de dialogue de dialogue suivante, qui dépend de l'avancement du combat:
            Si le combat commence, on regarde quel pokémon est le plus rapide:
                Si notre pokémon est plus rapide, on ouvre la boîte de dialogue Choix Attaque
                Si le pokémon sauvage est plus rapide, on ouvre la boîte de dialogue Fond Combat
            Si le combat est déjà en cours, changer de pokémon prend un tour, donc on ouvre
            la boîte de dialogue Fond Combat
        """
        # Cas où le combat commence
        if self.debut:
            
            # Récupération des vitesses des deux pokémons
            vitesse_poke_choisi = pok.dico_poke[self.ui.pokemon_choisi].speed 
            vitesse_poke_sauvage = pok.dico_poke[self.pokemon_sauvage].speed
            
            # Cas où notre pokémon est plus rapide: on ouvre la boîte de dialogue Choix Attaque
            if vitesse_poke_choisi >= vitesse_poke_sauvage:
                classe_choix_attaque = ChoixAttaqueDlg(pokemon_choisi=self.ui.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                                       choisiHP=self.ui.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ui.choisiHP,
                                                       ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi')
                classe_choix_attaque.exec_()
                self.close()
                # Remettre le focus sur le personnage après avoir fermé la fenêtre
                window.ui.tete_perso.setFocus()
                
            # Cas où le pokémon sauvage est plus rapide: on ouvre la boîte de dialogue Fond Combat
            else:
                classe_fond_combat = FondCombatDlg(pokemon_choisi=self.ui.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                                   choisiHP=self.ui.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ui.choisiHP,
                                                   ini_sauv_HP=self.ini_sauv_HP,debut=False, tour='sauvage', nb_degats='reçus')
                classe_fond_combat.exec_()
                self.close()
                # Remettre le focus sur le personnage après avoir fermé la fenêtre
                window.ui.tete_perso.setFocus()
        
        # Cas où le combat est déjà en cours: on ouvre la boîte de dialogue Fond Combat
        else:
            classe_fond_combat = FondCombatDlg(pokemon_choisi=self.ui.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                               choisiHP=self.ui.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ui.choisiHP,
                                               ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='sauvage', nb_degats='reçus')
            classe_fond_combat.exec_()
            self.close()
            # Remettre le focus sur le personnage après avoir fermé la fenêtre
            window.ui.tete_perso.setFocus()
            
                
class ChoixAttaqueDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut', pokemon_sauvage='défaut', choisiHP='défaut', sauvageHP='défaut',
                 ini_choi_HP='défaut', ini_sauv_HP='défaut', debut='défaut', tour='défaut'):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_choix_attaque()
        self.ui.setupUi(self)
        
        # Récupérer les paramètres de la fonction
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.choisiHP = choisiHP
        self.sauvageHP = sauvageHP
        self.ini_choi_HP = ini_choi_HP
        self.ini_sauv_HP = ini_sauv_HP
        
        # Récupération des caractéristiques des deux pokémons à l'aide du dictionnaire dico_poke
        obj_pokemon_choisi = pok.dico_poke[self.pokemon_choisi]
        obj_pokemon_sauvage = pok.dico_poke[self.pokemon_sauvage]
        
        # Calcul des dégats infligés pour chaque attaque
        self.attaque_neutre = pok.Caracteristiques_Pokemon.pts_attaque_neutre(obj_pokemon_choisi,obj_pokemon_sauvage)
        self.attaque_spe = pok.Caracteristiques_Pokemon.pts_attaque_spe(obj_pokemon_choisi,obj_pokemon_sauvage)
        
        # Affichage des dégats de chaque attaque
        self.ui.nbr_degat_att_neutre.setText(f"{self.attaque_neutre}")
        self.ui.nbr_degat_att_spe.setText(f"{self.attaque_spe}")
        
        # Bouton attaque neutre qui ouvre la boîte de dialogue Fond Combat
        self.ui.bouton_att_neutre.clicked.connect(self.open_dialog_atk_neutre)
        
        # Bouton attaque spéciale qui ouvre la boîte de dialogue Fond Combat
        self.ui.bouton_att_spe.clicked.connect(self.open_dialog_atk_spe)
        
    def open_dialog_atk_neutre(self):
        """
        Ouvre la boîte de dialogue Fond Combat, en gardant en paramètre les dégats infligés par l'attaque neutre
        """
        classe_fond_combat = FondCombatDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi', nb_degats=self.attaque_neutre)
        classe_fond_combat.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
        
    def open_dialog_atk_spe(self):
        """
        Ouvre la boîte de dialogue Fond Combat, en gardant en paramètre les dégats infligés par l'attaque spéciale
        """
        classe_fond_combat = FondCombatDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi', nb_degats=self.attaque_spe)
        classe_fond_combat.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
        
        
class FondCombatDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut', pokemon_sauvage='défaut', choisiHP='défaut', sauvageHP='défaut',
                 ini_choi_HP='défaut', ini_sauv_HP='défaut', debut='défaut', tour='défaut', nb_degats= 'défaut'):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_arene_de_combat()
        self.ui.setupUi(self)
        
        # Récupérer les paramètres de la fonction
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.choisiHP = choisiHP
        self.sauvageHP = sauvageHP
        self.ini_choi_HP = ini_choi_HP
        self.ini_sauv_HP = ini_sauv_HP
        self.nb_degats = nb_degats
        
        # Récupération des caractéristiques des deux pokémons à l'aide du dictionnaire dico_poke
        obj_pokemon_choisi = pok.dico_poke[self.pokemon_choisi]
        obj_pokemon_sauvage = pok.dico_poke[self.pokemon_sauvage]
        
        # Afficher le nom des deux pokémons
        self.ui.nom_mon_pokemon.setText(f"{self.pokemon_choisi}")
        self.ui.nom_pokemon_sauvage.setText(f"{self.pokemon_sauvage}")
        
        # Afficher les images des deux pokémons
        for k in pok.liste_tous_poke:
            if self.pokemon_choisi == k:
                image_path_choisi = f"interface_graphique/images/images_pokemon/pokemons_finaux/dos/{k}.png"
            if self.pokemon_sauvage == k:
                image_path_sauvage = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png"
        pixmap_choisi = QPixmap(image_path_choisi)
        pixmap_sauvage = QPixmap(image_path_sauvage)
        self.ui.img_mon_pokemon.setPixmap(pixmap_choisi)
        self.ui.img_mon_pokemon.setScaledContents(True)
        self.ui.img_pokemon_sauvage.setPixmap(pixmap_sauvage)
        self.ui.img_pokemon_sauvage.setScaledContents(True)
        
        # Afficher les barres de vie des deux pokémons et leurs valeurs associées
        self.ui.barre_vie_mon_pokemon.setMaximum(self.ini_choi_HP)
        self.ui.barre_vie_pokemon_sauvage.setMaximum(self.ini_sauv_HP)
        self.ui.barre_vie_mon_pokemon.setProperty("value",f"{self.choisiHP}")
        self.ui.barre_vie_pokemon_sauvage.setProperty("value",f"{self.sauvageHP}")
        
        # Cas où c'est à notre tour de jouer
        if tour == 'choisi':
            
            # Le pokémon reçoit les dégats précédemment calculés dans Choix Attaque
            self.sauvageHP -= self.nb_degats
            
            # Cas où le pokémon sauvage a encore des PV : le combat continue
            if self.sauvageHP > 0:
                # Affichage du texte descriptif
                self.ui.txt_descriptif.setText(f"{self.pokemon_choisi} attaque ! {self.pokemon_sauvage} perd {self.nb_degats} HP !")
                # Mise à jour de la barre de vie
                self.ui.barre_vie_pokemon_sauvage.setProperty("value",f"{self.sauvageHP}")
                # Bouton Continuer qui ouvre la boîte de dialogue Fond Combat
                self.ui.continuer.clicked.connect(self.open_dialog_fond_combat)
                
            # Cas où le pokémon sauvage n'a plus de PV : combat gagné
            if self.sauvageHP <= 0:
                # Affichage du texte descriptif
                self.ui.txt_descriptif.setText(f"{self.pokemon_sauvage} est KO ! Le combat est gagné !")
                # Mise à jour de la barre de vie
                self.ui.barre_vie_pokemon_sauvage.setProperty("value",0)
                # Bouton Continuer qui ouvre la boîte de dialogue Capture Pokemon
                self.ui.continuer.clicked.connect(self.open_dialog_capture_pokemon)
                
        # Cas où c'est au tour du pokémon sauvage de jouer
        if tour == 'sauvage':
            
            # Le choix de l'attaque du pokémon sauvage est aléatoire:
            # 50% de chance de lancer une attaque normale, 50% de chance de lancer une attaque spéciale
            if rd.random() < 0.5:
                self.nb_degats = pok.Caracteristiques_Pokemon.pts_attaque_neutre(obj_pokemon_sauvage,obj_pokemon_choisi)
            else:
                self.nb_degats = pok.Caracteristiques_Pokemon.pts_attaque_spe(obj_pokemon_sauvage,obj_pokemon_choisi)
            
            # Le pokémon reçoit les dégats précédemment calculés
            self.choisiHP -= self.nb_degats
            
            # Cas où notre pokemon a encore des PV : le combat continue
            if self.choisiHP > 0:
                # Affichage du texte descriptif
                self.ui.txt_descriptif.setText(f"{self.pokemon_sauvage} attaque ! {self.pokemon_choisi} perd {self.nb_degats} HP !")
                # Mise à jour de la barre de vie
                self.ui.barre_vie_mon_pokemon.setProperty("value",f"{self.choisiHP}")
                # Bouton Continuer qui ouvre la boîte de dialogue Ecran Triple
                self.ui.continuer.clicked.connect(self.open_dialog_ecran_triple)
            
            # Cas où notre pokémon n'a plus de PV : combat perdu
            if self.choisiHP <= 0:
                # Affichage du texte descriptif
                self.ui.txt_descriptif.setText(f"{self.pokemon_choisi} est KO ! Le combat est perdu !")
                # Mise à jour de la barre de vie
                self.ui.barre_vie_mon_pokemon.setProperty("value",0)
                # Bouton Continuer qui renvoie à la carte
                self.ui.continuer.clicked.connect(self.retour_carte)
                
    def open_dialog_fond_combat(self):
        """
        Ouvre la boîte de dialogue Fond Combat en prenant en paramètre que le 
        prochain tour est celui du pokémon sauvage
        """
        classe_fond_combat = FondCombatDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='sauvage', nb_degats='reçus')
        classe_fond_combat.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
    
    def open_dialog_ecran_triple(self):
        """
        Ouvre la boîte de dialogue Ecran Triple en prenant en paramètre que le 
        prochain tour est celui de notre pokémon
        """
        classe_ecran_triple = EcranTripleDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                           choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                           ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi')
        classe_ecran_triple.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
        
    def open_dialog_capture_pokemon(self):
        """
        Ouvre la boîte de dialogue Capture Pokemon en gardant en paramètre le nom
        du pokémon sauvage pour pouvoir le capturer
        """
        classe_capture_pokemon = CapturePokemonDlg(pokemon_sauvage=self.pokemon_sauvage)
        classe_capture_pokemon.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
    
    def retour_carte(self):
        """
        Renvoie à la carte
        """
        self.close()
    

class EcranTripleDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_choisi='défaut', pokemon_sauvage='défaut', choisiHP='défaut', sauvageHP='défaut',
                 ini_choi_HP='défaut', ini_sauv_HP='défaut', debut='défaut', tour='défaut'):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_ecran_triple()
        self.ui.setupUi(self)
        
        # Récupérer les paramètres de la fonction
        self.pokemon_choisi = pokemon_choisi
        self.pokemon_sauvage = pokemon_sauvage
        self.choisiHP= choisiHP
        self.sauvageHP = sauvageHP
        self.ini_choi_HP = ini_choi_HP
        self.ini_sauv_HP = ini_sauv_HP
        
        # Bouton Fuir qui renvoie à la carte
        self.ui.bouton_fuir.clicked.connect(self.fuir)
        
        # Bouton Attaque qui ouvre la boîte de dialogue Choix Attaque
        self.ui.bouton_attaque.clicked.connect(self.open_dialog_choix_attaque)
        
        # Bouton Changer Pokémon qui ouvre la boîte de dialogue Choix Pokemon
        self.ui.bouton_changer_pokemon.clicked.connect(self.open_dialog_choix_pokemon)

    def open_dialog_choix_attaque(self):
        """
        Ouvre la boîte de dialogue Choix Attaque
        """
        classe_choix_attaque = ChoixAttaqueDlg(pokemon_choisi=self.pokemon_choisi, pokemon_sauvage=self.pokemon_sauvage,
                                               choisiHP=self.choisiHP, sauvageHP=self.sauvageHP, ini_choi_HP=self.ini_choi_HP,
                                               ini_sauv_HP=self.ini_sauv_HP, debut=False, tour='choisi')
        classe_choix_attaque.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
        
    def open_dialog_choix_pokemon(self):
        """
        Ouvre la boîte de dialogue Choix Pokémon
        """
        classe_choix_pokemon = ChoixPokemonDlg(pokemon_sauvage=self.pokemon_sauvage, sauvageHP=self.sauvageHP,
                                               ini_sauv_HP=self.ini_sauv_HP, debut=False)
        classe_choix_pokemon.exec_()
        self.close()
        # Remettre le focus sur le personnage après avoir fermé la fenêtre
        window.ui.tete_perso.setFocus()
        
    def fuir(self):
        """
        Renvoie à la carte
        """
        self.close()


class CapturePokemonDlg(QDialog):
    
    def __init__(self, parent=None, pokemon_sauvage='défaut'):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_capture()
        self.ui.setupUi(self)
        
        # Récupérer le nom du pokémon sauvage capturé 
        self.pokemon_sauvage = pokemon_sauvage
        
        # Afficher le texte "{pokemon_sauvage} est capturé !" avec le nom du pokémon
        self.ui.titre.setText(f"{pokemon_sauvage} est capturé !")
        
        # Afficher l'image du pokémon correspondant
        for k in pok.liste_tous_poke:
            if pokemon_sauvage == k:
                image_path = f"interface_graphique/images/images_pokemon/pokemons_finaux/face/{k}.png"
        pixmap = QPixmap(image_path)
        self.ui.pokemon_capture.setPixmap(pixmap)
        self.ui.pokemon_capture.setScaledContents(True)
        
        # Ajouter le pokémon à la liste des pokémons dans le pokédeck
        pok.liste_pokedeck.append(pokemon_sauvage)
        
        # Changer les coordonnées du pokémon en ['pokédeck','pokédeck'] pour qu'il 
        # n'apparaisse plus sur la carte
        ligne_coord = np.array([pokemon_sauvage,'pokédeck','pokédeck','pokédeck','pokédeck'])
        pok.dico_poke[ligne_coord[0]] = pok.Pokemon(ligne_coord)
        
        # Bouton OK qui renvoie sur la carte ou affiche l'écran de fin quand les 24 pokémons sont capturés
        self.ui.ok.clicked.connect(self.retour_carte_ou_ecran_fin)
    
    def retour_carte_ou_ecran_fin(self):
        """
        Ouvre la boîte de dialogue de l'écran de fin si les 24 pokémons sont capturés
        Renvoie à la carte sinon
        """
        if len(pok.liste_pokedeck) == 24:
            classe_ecran_final = EcranFinalDlg()
            classe_ecran_final.exec_()
            # Remettre le focus sur le personnage après avoir fermé la fenêtre de l'écran d'accueil
            window.ui.tete_perso.setFocus()
        self.close()
        
        
class EcranFinalDlg(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Utilisation de la classe générée par Qt Designer
        self.ui = Ui_ecran_final()
        self.ui.setupUi(self)
    
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MapMainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
"""
separer classes
voir rapport
"""
