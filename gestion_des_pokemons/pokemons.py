import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

path = os.path.dirname(os.path.abspath(__file__))

# Récupération des data
path1 = os.path.join(path, "../data/pokemon_first_gen.csv")
tableau_caracteristiques_pokemons = pd.read_csv(path1).to_numpy()
path2 = os.path.join(path, "../data/pokemon_coordinates.csv")
pokemons_coordinates = pd.read_csv(path2,engine='python')

# Pokémons choisis
liste_starter = ['Bulbasaur','Charmander','Squirtle']
liste_poke_choisis = ['Caterpie','Clefairy','Diglett','Eevee','Ekans',"Farfetch'd",'Geodude','Growlithe',
                      'Jigglypuff','Machop','Meowth','Oddish','Paras','Pikachu','Ponyta','Psyduck',
                      'Rattata','Sandshrew','Venonat','Vulpix','Zubat']
liste_tous_poke = liste_starter + liste_poke_choisis

# Création du tableau contenant les 21 pokémons choisis et leurs coordonnées
pokemons_coordinates['id'] = np.arange(998)
liste_poke_coordinates = list(pokemons_coordinates['pokemon'])
liste_index = []
for k in range(len(liste_poke_coordinates)):
    if liste_poke_coordinates[k] in liste_poke_choisis:
        liste_index.append(k)
        liste_poke_choisis.remove(liste_poke_coordinates[k])
pokemons_coordinates_final = pokemons_coordinates[pokemons_coordinates['id'].isin(liste_index)]
coord = list(pokemons_coordinates_final['coordinates'])
liste_x = []
liste_y = []
for k in range(len(coord)):
    x = round(float(coord[k][1:8])*10*2.325+20,6)
    liste_x.append(x)
    i = 0
    while coord[k][i] != ' ':
        i += 1
    y = round(500-float(coord[k][i+1:i+8])*10*4.8,6)
    liste_y.append(y)
pokemons_coordinates_final['X'] = liste_x
pokemons_coordinates_final['Y'] = liste_y
tableau_pokemons = pokemons_coordinates_final.to_numpy()

# Affichage de la visualisation de la carte
plt.scatter(pokemons_coordinates_final.X,pokemons_coordinates_final.Y)
plt.show()



class Caracteristiques_Pokemon:
    
    tableau_affinites = np.array([[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.5,  0,  1,  1,0.5,  1],
                                  [  1,0.5,0.5,  2,  1,  2,  1,  1,  1,  1,  1,  2,0.5,  1,0.5,  1,  2,  1],
                                  [  1,  2,0.5,0.5,  1,  1,  1,  1,  2,  1,  1,  1,  2,  1,0.5,  1,  1,  1],
                                  [  1,0.5,  2,0.5,  1,  1,  1,0.5,  2,0.5,  1,0.5,  2,  1,0.5,  1,0.5,  1],
                                  [  1,  1,  2,0.5,0.5,  1,  1,  1,  0,  2,  1,  1,  1,  1,0.5,  1,  1,  1],
                                  [  1,0.5,0.5,  2,  1,0.5,  1,  1,  2,  2,  1,  1,  1,  1,  2,  1,0.5,  1],
                                  [  2,  1,  1,  1,  1,  2,  1,0.5,  1,0.5,0.5,0.5,  2,  0,  1,  2,  2,0.5],
                                  [  1,  1,  1,  2,  1,  1,  1,0.5,0.5,  1,  1,  1,0.5,0.5,  1,  1,  0,  2],
                                  [  1,  2,  1,0.5,  2,  1,  1,  2,  1,  0,  1,0.5,  2,  1,  1,  1,  2,  1],
                                  [  1,  1,  1,  2,0.5,  1,  2,  1,  1,  1,  1,  2,0.5,  1,  1,  1,0.5,  1],
                                  [  1,  1,  1,  1,  1,  1,  2,  2,  1,  1,0.5,  1,  1,  1,  1,  0,0.5,  1],
                                  [  1,0.5,  1,  2,  1,  1,0.5,0.5,  1,0.5,  2,  1,  1,0.5,  1,  2,0.5,0.5],
                                  [  1,  2,  1,  1,  1,  2,0.5,  1,0.5,  2,  1,  2,  1,  1,  1,  1,0.5,  1],
                                  [  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  2,  1,0.5,  1,  1],
                                  [  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,0.5,  0],
                                  [  1,  1,  1,  1,  1,  1,0.5,  1,  1,  1,  2,  1,  1,  2,  1,0.5,  1,0.5],
                                  [  1,0.5,0.5,  1,0.5,  2,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,0.5,  2],
                                  [  1,0.5,  1,  1,  1,  1,  2,0.5,  1,  1,  1,  1,  1,  1,  2,  2,0.5,  1]])

    liste_types = ['Normal','Fire','Water','Grass','Electric','Ice','Fighting','Poison','Ground','Flying',
                   'Psychic','Bug','Rock','Ghost','Dragon','Dark','Steel','Fairy']
    
    def __init__(self,ligne_pokemon):
        self.id = ligne_pokemon[0]
        self.name = ligne_pokemon[1]
        self.type1 = ligne_pokemon[2]
        self.type2 = ligne_pokemon[3]
        self.total = ligne_pokemon[4]
        self.HP = ligne_pokemon[5]
        self.attack = ligne_pokemon[6]
        self.defense = ligne_pokemon[7]
        self.sp_atk = ligne_pokemon[8]
        self.sp_def = ligne_pokemon[9]
        self.speed = ligne_pokemon[10]
        
    def __str__(self):
        txt = f'\n\nNuméro : {self.id}\nNom : {self.name}\n'
        txt += f'Type 1 : {self.type1}     Type 2 : {self.type2}\n'
        txt += f'Total : {self.total}\nHP : {self.HP}\n'
        txt += f'Attack : {self.attack}     Defense : {self.defense}\n'
        txt += f'Sp. Atk : {self.sp_atk}     Sp. Def : {self.sp_def}\n'
        txt += f'Speed : {self.speed}'
        return txt
    
    def pts_attaque_neutre(choisi,sauvage):
        points_atk_neutre = round(choisi.attack - sauvage.defense * (sauvage.defense/sauvage.total))
        return points_atk_neutre
    
    def pts_attaque_spe(choisi,sauvage):
        ligne = Caracteristiques_Pokemon.liste_types.index(choisi.type1)
        colonne1 = Caracteristiques_Pokemon.liste_types.index(sauvage.type1)
        coeff = Caracteristiques_Pokemon.tableau_affinites[ligne][colonne1]
        if sauvage.type2 in Caracteristiques_Pokemon.liste_types:
            colonne2 = Caracteristiques_Pokemon.liste_types.index(sauvage.type2)
            coeff *= Caracteristiques_Pokemon.tableau_affinites[ligne][colonne2]
        points_atk_spe = round((choisi.sp_atk - sauvage.sp_def * (sauvage.sp_def/sauvage.total))* coeff)
        return points_atk_spe
    

class Pokemon(Caracteristiques_Pokemon):
    
    def __init__(self,ligne_coord):
        ligne_pokemon = dico_array[ligne_coord[0]]
        super().__init__(ligne_pokemon)
        self.coordX = ligne_coord[3]
        self.coordY = ligne_coord[4]
        path3 = os.path.join(path, f"../interface_graphique/images/images_pokemon/pokemons_finaux/face/{ligne_coord[0]}.png")
        path4 = os.path.join(path, f"../interface_graphique/images/images_pokemon/pokemons_finaux/dos/{ligne_coord[0]}.png")
        self.img_face = mpimg.imread(path3)
        self.img_dos = mpimg.imread(path4)
        
    def __str__(self):
        txt2 = f'\nCoordonnées : [{self.coordX}, {self.coordY}]'
        return super().__str__() + txt2
    
    def plot_face(self):
        plt.imshow(self.img_face)
    
    def plot_dos(self):
        plt.imshow(self.img_dos)
        
        
        
dico_array = {}       
dico_objet = {}
for k in range(len(tableau_caracteristiques_pokemons)):
    ligne_pokemon = tableau_caracteristiques_pokemons[k]
    dico_array[ligne_pokemon[1]] = ligne_pokemon
    dico_objet[ligne_pokemon[1]] = Caracteristiques_Pokemon(ligne_pokemon)


dico_poke = {}
for k in range(len(tableau_pokemons)):
    ligne_coord = tableau_pokemons[k]
    dico_poke[ligne_coord[0]] = Pokemon(ligne_coord)
for k in range(len(liste_starter)):
    ligne_coord = np.array([liste_starter[k],'pokédeck','pokédeck','pokédeck','pokédeck'])
    dico_poke[ligne_coord[0]] = Pokemon(ligne_coord)
    
   
"""
print(dico_objet['Vulpix'])
print(dico_objet['Ivysaur'].calcul_pts_attaque(dico_objet['Bulbasaur']))
dico_poke['Caterpie'].plot_dos()
print(dico_poke['Caterpie'])
"""


