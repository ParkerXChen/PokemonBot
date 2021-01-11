import config
import random

userinventory = config.CONFIG['userinventory']
nextlevel = 0
def save():
    config.CONFIG["userinventory"] = userinventory
    config.save_config()

def check_uid(uid):
    if not uid in userinventory:
        userinventory[uid] = {
            "level": 0,
            "XP": 0,
            "balls": {
                "pokeballs": 0,
                "greatballs": 0,
                "ultraballs": 0,
                "masterballs": 0
            },
            "buddy": "",
            "pokemons": [],
            "pokedollars": 0,
            "codesredeemed": [],
            "started": False,
            "Spawnedpokemon": False
        }
    save()


def set_buddy(uid,buddy):
    uid = str(uid)
    userinventory[uid]['buddy'] = buddy
    save()

def set_yesspawnedpokemon(uid):
    uid = str(uid)
    userinventory[uid]['Spawnedpokemon'] = True
    save()

def set_nospawnedpokemon(uid):
    uid = str(uid)
    userinventory[uid]['Spawnedpokemon'] = False
    save()

def add_balls(uid,balltype,number):
    uid = str(uid)
    userinventory[uid]['balls'][balltype] += number
    save()

def add_pokedollars(uid,number):
    uid = str(uid)
    userinventory[uid]['pokedollars'] += number
    save()

def add_pokemon(uid,pokemon):
    uid = str(uid)
    health = random.randint(pokemon.minhp,pokemon.maxhp)
    damage = random.randint(pokemon.mindp,pokemon.maxdp)
    power = round(health*damage/2)
    statsdict = {'name':pokemon.name,'health':health,'damage ':damage,'power':power}
    userinventory[uid]['pokemons'].append(statsdict)
    save()

def add_XP(uid,number):
    uid = str(uid)
    userinventory[uid]['XP'] += number
    save()

def subtract_XP(uid,number):
    uid = str(uid)
    userinventory[uid]['XP'] -= number
    save()

def add_coderedeemed(uid,code):
    uid = str(uid)
    userinventory[uid]['codesredeemed'].append(code)
    save()
    
def reset(uid):
    uid = str(uid)
    userinventory[uid]['balls']['pokeballs'] = 0
    userinventory[uid]['balls']['greatballs'] = 0
    userinventory[uid]['balls']['ultraballs'] = 0
    userinventory[uid]['balls']['masterballs'] = 0
    userinventory[uid]['pokemons'] = []
    userinventory[uid]['buddy'] = ''
    userinventory[uid]['pokedollars'] = 0
    userinventory[uid]['otheritems'] = []
    userinventory[uid]['codesredeemed'] = [] 
    userinventory[uid]['level'] = 0
    userinventory[uid]['XP'] = 0
    userinventory[uid]['started'] = False
    save()
