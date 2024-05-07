# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:44:26 2024

@author: elago
"""
import pandas as pd
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from gestion_des_pokemons.pokemons import  *
from interface_graphique.choix_attaque import Ui_Dialog as Choix_attaques_diag
from interface_graphique.ecran_triple import Ui_Dialog as Ecran_triple_diag
from interface_graphique.main_map import MainWindow, XXXXDlg
import random as rand


        
class Joueur(): #Ui_MainWindow
    #liste représente l'ensemble des pokémons du deck du joueur
    def __init__(self, pokedeck, nom):
        
        self.nom = nom
        self.pokedeck = pokedeck
    
   

class Dialogue_choix_poke(QDialog):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.ui = Ui_Boite_Dialogue
    pass            
        
class Dialogue_attaque(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Choix_attaques_diag
        self.bouton_att_neutre.clicked.connect(self.att_neutre)
        self.bouton_att_spe.clicked.connect(self.att_spe)
        
        def att_neutre(self,pokemon):
            
            pass
        def att_spe(self):
            pass

class Dlg_choix_action(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ecran_triple_diag
        self.bouton_fuir.clicked.connect(self.close)
        self.bouton_attaque.clicked.connect(self.attaquer)
        self.bouton_changer_pokemon.clicked.connect(self.changer)
        
        
        def changer(self):
            #on change mais on attaque pas
            pass
        def attaquer(self):
            """
            renvoie à la boite de dialogue du choix d'attaque
            entre neutre et spéciale

            Returns
            -------
            None.

            """
            dlg = Dialogue_attaque(QDialog)
            dlg.exec()

class Dlg_choix_combat(Qdialog):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    
class Carte(QMainWindow): #dans main_map, à récupérer
    #représente le fond qu'il y a en permanence
    #a la méthode bouger pour le déplacement du Joueur
    def Detection_pokemon(self):
        if revelation(self.ui.tete_perso.pos()) != None:
            self.Combattre(dico_poke[revelation(self.ui.tete_perso.pos())])
        pass
    def Combattre(self,sauvage):
        """
        modélise les choix du joueur face à un pokémon sauvage

        Parameters
        ----------
        pokemon : TYPE class Pokemon
            DESCRIPTION.

        Returns
        -------
        None.

        """
        choisi = dico_poke[self.choix_pokemon.currentText()] #à récupérer avant
        
        hp_sauvage = sauvage.HP
        hp_choisi= choisi.HP
        
        #bouton
        if choisi.joueur_commence(sauvage): #condiditon de vitesse
            points = choisi.calcul_pts_attaque(sauvage)
            dlg_attaque = Dialogue_attaque(self)
            nbr_degat_att_spe.setText(str(points[1]))
            nbr_degat_att_neutre.setText(str(points[0]))
            
            hp_sauvage -= points # à modifier selon choix joueur
        else:
            
            if rand.random() < 0.5:
                point = sauvage.calcul_pts_attaque(pokemon_choisi)[0]
                
            else:
                point =sauvage.calcul_pts_attaque(pokemon_choisi)[1]
            pokemon_choisi.HP -=point
        while pokemon_choisi.HP > 0 :
            if pokemon_choisi.joueur_commence(sauvage):
                if rand.random() < 0.5:
                    point = sauvage.calcul_pts_attaque(pokemon_choisi)[0]
                    
                else:
                    point =sauvage.calcul_pts_attaque(pokemon_choisi)[1]
                pokemon_choisi.HP -= point
            else:
                dlg_choix = Dlg_choix_action(self)
                dlg_choix.exec()
                 
             
            
            if pokemon.hp < 0:
                self.pokedeck += pokemon
   
    def fuite(self):
        #retour map
        pass
    def attaque(self):
        degats = ...
        self.bouton_att_neutre.clicked.connect(self.att_neutre)
        self.bouton_att_spe.clicked.connect(self.att_spe)#à mettre dans le init
    
    def changer(self):
        pass
    
        

class Attaque():
    def __init__(self, nom, genre, nbpoints):
        self.nom = nom
        self.genre = genre
        self.nbpoints = nbpoints
        
#faire une liste des attaques possibles

if __name__ == "__main__":
    print(dico_poke['Caterpie'])