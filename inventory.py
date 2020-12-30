import config

userinventory = config.CONFIG['userinventory']
nextlevel = 0
def save():
    config.CONFIG["userinventory"] = userinventory
    config.save_config()


def set_buddy(buddy):
    userinventory['buddy'] = buddy
    save()


def add_pokeballs(number):
    userinventory['balls']['pokeballs'] += number
    save()

def add_pokedollars(number):
    userinventory['pokedollars'] += number
    save()

def add_item(item):
    userinventory['otheritems'].append(item)
    save()

def add_pokemon(pokemon):
    userinventory['pokemons'].append(pokemon)
    save()

def add_XP(number):
    userinventory['XP'] += number
    save()

def subtract_XP(number):
    userinventory['XP'] -= number
    save()

def add_coderedeemed(code):
    userinventory['codesredeemed'].append(code)
    save()
    
def reset():
    userinventory['balls']['pokeballs'] = 0
    userinventory['balls']['greatballs'] = 0
    userinventory['balls']['ultraballs'] = 0
    userinventory['balls']['masterballs'] = 0
    userinventory['pokemons'] = []
    userinventory['buddy'] = ''
    userinventory['pokedollars'] = 0
    userinventory['otheritems'] = []
    userinventory['codesredeemed'] = [] 
    userinventory['level'] = 0
    userinventory['XP'] = 0
    userinventory['started'] = False
    save()
