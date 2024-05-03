import pandas as pd

pokemons = pd.read_csv("../data/pokemon_first_gen.csv")
pokemons_coordinates = pd.read_csv("../data/pokemon_coordinates.csv")
l = list(pokemons['Name'])
l2 = list(pokemons_coordinates['pokemon'])

coord = list(pokemons_coordinates['coordinates'])
for k in range(len(coord)):
    




