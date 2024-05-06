import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Récupération des data
tableau_caracteristiques_pokemons = pd.read_csv("../data/pokemon_first_gen.csv").to_numpy()
pokemons_coordinates = pd.read_csv("../data/pokemon_coordinates.csv",engine='python')

# Pokémons choisis
liste_starter = ['Bulbasaur','Charmander','Squirtle']
liste_poke_choisis = ['Caterpie','Clefairy','Diglett','Eevee',"Farfetch'd",'Geodude','Growlithe','Jigglypuff',
                  'Machop','Meowth','Nidoran♂','Nidoran♀','Oddish','Pikachu','Ponyta','Psyduck','Rattata',
                  'Sandshrew','Venonat','Vulpix','Zubat']

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
    x = round(float(coord[k][1:8])*10,6)
    liste_x.append(x)
    i = 0
    while coord[k][i] != ' ':
        i += 1
    y = round(float(coord[k][i+1:i+8])*10,6)
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
    
    def joueur_commence(self,autre):
        if self.speed >= autre.speed:
            return True
        return False
        
    def calcul_pts_attaque(self,autre):
        # prendre défense en compte
        points_atk_neutre = self.attack
        ligne = Caracteristiques_Pokemon.liste_types.index(self.type1)
        colonne1 = Caracteristiques_Pokemon.liste_types.index(autre.type1)
        coeff = Caracteristiques_Pokemon.tableau_affinites[ligne][colonne1]
        if autre.type2 in Caracteristiques_Pokemon.liste_types:
            colonne2 = Caracteristiques_Pokemon.liste_types.index(autre.type2)
            coeff *= Caracteristiques_Pokemon.tableau_affinites[ligne][colonne2]
        points_atk_spe = self.sp_atk * coeff
        return points_atk_neutre, points_atk_spe
            
    def tour_joueur(self,autre):
        Attaquer = True
        Fuir = False
        Changer_poke = False
        
    def changement_poke(self):
        pass
              
    def combat(self,autre):
        joueur_HP = self.HP
        sauvage_HP = autre.HP
        Attaquer = True
        while Attaquer:
            while joueur_HP > 0 and sauvage_HP > 0:
                pass



class Pokemon(Caracteristiques_Pokemon):
    
    distance_detection = 1
    
    def __init__(self,ligne_coord):
        ligne_pokemon = dico_array[ligne_coord[0]]
        super().__init__(ligne_pokemon)
        self.coordX = ligne_coord[2]
        self.coordY = ligne_coord[3]
        
    def __str__(self):
        txt2 = f'\nCoordonnées : [{self.coordX}, {self.coordY}]'
        return super().__str__() + txt2
        
        
        
dico_array = {}       
dico_objet = {}
for k in range(len(tableau_caracteristiques_pokemons)):
    ligne_pokemon = tableau_caracteristiques_pokemons[k]
    dico_array[ligne_pokemon[1]] = ligne_pokemon
    dico_objet[ligne_pokemon[1]] = Caracteristiques_Pokemon(ligne_pokemon)


dico_poke = {}
for k in range(len(tableau_pokemons)):
    ligne_coord = tableau_pokemons[k]
    cle = (ligne_coord[0],ligne_coord[2],ligne_coord[3])
    dico_poke[cle] = Pokemon(ligne_coord)
    
    
   

print(dico_objet['Ivysaur'])
print(dico_objet['Bulbasaur'])
dico_objet['Ivysaur'].calcul_pts_attaque(dico_objet['Bulbasaur'])

print(dico_poke[('Caterpie', 213, 227.632)])



