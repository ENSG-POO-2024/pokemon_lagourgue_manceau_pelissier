         
        
class Dialogue_attaque(QDialog):
    def __init__(self,points, parent=None):
        super().__init__(parent)

        self.ui = Choix_attaques_diag
        self.bouton_att_neutre.clicked.connect(self.att_neutre)
        self.bouton_att_spe.clicked.connect(self.att_spe)
        self.nbr_degat_att_spe.setText(str(points[1]))
        self.nbr_degat_att_neutre.setText(str(points[0]))
        
        
    def att_neutre(self,points):
        return points[0]
            
    def att_spe(self, points):
        return points[1]
            

class Dlg_choix_action(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ecran_triple_diag
        
        self.bouton_fuir.clicked.connect(self.close)
        self.bouton_attaque.clicked.connect(self.attaquer)
        self.bouton_changer_pokemon.clicked.connect(self.changer)
        
        
    def changer(self):
        #on change mais on attaque pas
        dlg_choix = Dialogue_choix_poke(self)
        dlg.exec()
            
    def attaquer(self):
        """
            renvoie à la boite de dialogue du choix d'attaque
            entre neutre et spéciale

            Returns
            -------
            None.

            """
        dlg = Dialogue_attaque(self)
        dlg.exec()


    
    
class Main(QMainWindow): #dans main_map, à récupérer
    

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
            dlg_attaque = Dialogue_attaque(self, points)
            dlg_attaque.exec()
            
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
                dlg_choix = Dlg_choix_action(self)
                dlg_choix.exec()
                #à afficher dans la barre de vie
            else:
                dlg_choix = Dlg_choix_action(self)
                dlg_choix.exec()
                if rand.random() < 0.5:
                    point = sauvage.calcul_pts_attaque(pokemon_choisi)[0]
                    
                else:
                    point =sauvage.calcul_pts_attaque(pokemon_choisi)[1]
                pokemon_choisi.HP -= point
                 
             
            
            if pokemon.hp < 0:
                dico_poke[sauvage].coordX = 'pokédeck'
                dico_poke[sauvage].coordY = 'pokédeck'
                self.pokedeck.addItem( pokemon)
        # afficher vous avez perdu
                