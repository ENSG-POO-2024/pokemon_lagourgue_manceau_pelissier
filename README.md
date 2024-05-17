# Pokémon: projet informatique

* Lagourgue Eléonore
* Manceau Loéva
* Pelissier Maïlys

* Version numpy utilisée : 1.24.3
* Version PyQT utilisée : 5.15.7

## Manuel d'utilisation du projet pokémon :

### Lancement du jeu :

* Ouvrir dans spyder le fichier main_map.py.
* Lancer ce fichier.
* Le joueur commence le jeu avec trois pokémons dans son deck : Bulbasaur, Charmander et Squirtle.

### Pokédeck :
* Le joueur peut accéder aux pokémons qu'il possède en cliquant sur le bouton Pokedeck. Il accèdera à un menu déroulant où il pourra voir tous les pokémons qu'il a et le nombre de pokémons possédés sur le nombre total de pokémons sur la carte (24).

### Déplacement :
* Pour se déplacer sur la carte, utiliser les flèches du clavier.

### Rencontre du pokémon sauvage:
* Un écran s'affiche pour signaler la rencontre avec un pokémon sauvage si on rentre dans sa zone de détection.
* Le joueur peut choisir de s'enfuir ou de combattre.

### Combat :
* Dans le cas d'un combat, le joueur doit sélectionner un pokémon.
* S'il est moins rapide, c'est le pokémon sauvage qui commence à attaquer.
* Sinon, c'est au pokémon choisi par le joueur de commencer.
* Le joueur et le pokémon jouent chacun leur tour.
* A son tour le joueur peut attaquer, changer de pokémon ou fuir.
* En cas d'attaque, le pokémon a le choix entre une attaque normale et une attaque spéciale (de son 1er type).
* Le pokémon sauvage choisit une de ces attaques aléatoirement.
* En cas de victoire, le pokémon sauvage est capturé et fait désormais partie du Pokédeck.


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

* Un fichier csv contenant une liste de pokemons avec des coordonnées géographiques


#### Dans le répertoire "gestion_des_pokemons", on retrouve :
* Un fichier python contenant la classe Pokemon et Caracteristiques_Pokemon qui permet de créer les attributs des pokémons présents sur la carte

#### Dans le répertoire "interface_graphique", on retrouve :

* Un dossier images contenant les images utilisées dans le jeu

* map au format ui et py : c'est la mainwindow. Elle représente la carte où le joueur se déplace.

* ecran_accueil au format ui et py : boîte de dialogue de l'écran d'accueil où le joueur clique sur "play".

* pokedeck au format ui et py :  boîte de dialogue du pokedeck où le joueur peut voir les pokémons capturés.

* rencontre_pokemon_sauvage au format ui et py : écran qui s'affiche lorsque le joueur croise un pokémon sauvage.

* choix_pokemon au format ui et py : écran où le joueur peut choisir son pokémon lors d'un combat.

* choix_attaque au format ui et py : écran où le joueur choisit entre une attaque neutre et une attaque spéciale.

* fond_combat  au format ui et py : écran représentant l'arène où s'affrontent les deux pokémons.

* ecran_triple au format ui et py : écran où le joueur choisit entre attaquer, changer de pokémon ou fuir.

* capture_pokemon au format ui et py : écran qui annonce au joueur la capture du pokémon sauvage.

* ecran_final au format ui et py : écran qui annonce la fin du jeu, lorsque les 24 pokémons sont capturés.

### Le main :
* main_map : contient la classe MapMainWindow. Permet de lancer le jeu.

