# Pokémon: projet informatique

* Lagourgue Eléonore
* Manceau Loéva
* Pelissier Maïlys

## Manuel d'utilisation du projet pokémon :

### Lancement du jeu :

* Ouvrir dans spyder le fichier main_map.py
* Lancer ce fichier 
* Le joueur commence le jeu avec trois pokémons dans son deck: Bulbasaur, Charmander et Squirtle

### Pokédeck :
* Le joueur peut accéder aux pokémons qu'il possède en cliquant sur le bouton Pokedeck. Il accèdera à un menu déroulant où il pourra voir tous les pokémons qu'il a et le nombre de pokémons possédés sur le nombre total de pokémons sur la carte.

### Déplacement :
* Pour se déplacer sur la carte, utiliser les flèches du clavier

### Rencontre du pokémon sauvage:
* Un écran s'affiche pour signaler la rencontre avec un pokémon sauvage
* Le joueur choisit de s'enfuir ou de combattre

### Combat :
* Dans le cas d'un combat, le joueur doit sélectionner un pokémon
* S'il est moins rapide, c'est le pokémon sauvage qui attaque. Sinon le joueur a le choix entre une attaque neutre et une attaque spéciale
* A chaque tour le joueur peut attaquer, changer de pokémon ou fuir.


## Modification du code :

### Organisation des fichiers  : 

#### Dans le répertoire "documents", on retrouve :
* La présentation du projet au format pdf
* L'explication des coefficents d'attaques au format pdf

#### Dans le répertoire "data", on retrouve :  
* Un fichier csv contenant les 151 pokemons de la première génération, ainsi que leurs attributs :
  1. `#` : indique le numéro du pokemon (peut être utilisé comme id)
  2. `name` : le nom (ici en anglais) du pokemon
  3. `Type 1` : le type du pokemon
  4. `Type 2` : le second type du pokemon (s'il en possède un deuxième)
  5. `Total` : le nombre total de points d'attributs (HP + Attack + Defense + Sp. Attack + Sp. Def + Speed)
  6. `HP` : le nombre de point de vie de départ
  7. `Attack` : le nombre de point d'attaque (coefficient pour les dégats infligés)
  8. `Defense` : le nombre de point de défense (coefficient pour les dégats reçus)
  9. `Sp. Atk` : le nombre de point d'attaque spéciale (coefficient pour les dégats infligés)
  10. `Sp. Def` : le nombre de point de défense contre une attaque spéciale (coefficient pour les dégats reçus)
  11. `Speed` : la vitesse du pokemon (détermine qui joue en premier)
  12. `Generation` : la génération du pokemon (ici la première)
  13. `Legendary` : rareté du pokemon, les légendaires sont normalement uniques

* Un fichier csv contenant une liste de pokemons avec des coordonnées géographiques.


#### Dans le répertoire "gestion_des_pokemons", on retrouve :
* Un fichier python contenant la classe Pokemon et Caracteristiques_Pokemons

#### Dans le répertoire "interface_graphique", on retrouve :
* ecran_accueil au format ui et py : il contient
* map au format ui et py : c'est la mainwindow
* pokedeckau au format ui et py
* rencontre_pokemon_sauvageau au format ui et py
* choix_attaqueau au format ui et py
* fond_combatau au format ui et py
* ecran_tripleau au format ui et py
* capture_pokemonau au format ui et py



1. Se créer un identifiant github

