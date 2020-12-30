import pokemons
import random

rarityrates = ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','s','s','s','s','l']

pokemonchosen = []

pokemonchosenstr = ''

def choosenewpokemon():   
    global pokemonchosen
    global pokemonchosenstr
    
    raritychosen = random.choice(rarityrates)
    if raritychosen == 'c':
        pokemonchosen = random.choice(pokemons.commonpokemons)
    elif raritychosen == 'u': 
        pokemonchosen = random.choice(pokemons.uncommonpokemons)
    elif raritychosen == 'r': 
        pokemonchosen = random.choice(pokemons.rarepokemons)
    elif raritychosen == 's': 
        pokemonchosen = random.choice(pokemons.superrarepokemons)
    elif raritychosen == ';': 
        pokemonchosen = random.choice(pokemons.legendarypokemons)
    
    pokemonchosenstr = pokemonchosen.name   

msg = ''

choosenewpokemon()
print(pokemonchosen)
print(pokemonchosenstr)