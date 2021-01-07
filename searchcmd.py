from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand,InputMediaAnimation
import random
import inventory, pokemons
import time

pokeballbutton = InlineKeyboardButton('Pokeball',callback_data='ballchoice:pokeball')
greatballbutton = InlineKeyboardButton('Greatball',callback_data='ballchoice:greatball')
ultraballbutton = InlineKeyboardButton('Ultraball',callback_data='ballchoice:ultraball')
masterballbutton = InlineKeyboardButton('Masterball',callback_data='ballchoice:masterball')
ballchoicekb = InlineKeyboardMarkup([])

pokemonchosenrarity = '' 
pokemonchosenstr = ''
raritypercent = 0

def choosenewpokemon():   
    global pokemonchosen
    global pokemonchosenstr
    global pokemonchosenrarity
    global raritypercent
    global pokedollarsreward
    global XPreward 
    
    raritynum = random.randint(1,100)

    if raritynum <= 65:
        pokemonchosenrarity = 'Common'
        pokemonchosen = random.choice(pokemons.commonpokemons)
        raritypercent = 54.76
        pokedollarsreward = random.randint(100,200)
        XPreward = random.randint(150,250)
    elif raritynum <= 80: 
        pokemonchosenrarity = 'Uncommon'
        pokemonchosen = random.choice(pokemons.uncommonpokemons)
        raritypercent = 14.47
        pokedollarsreward = random.randint(250,500)
        XPreward = random.randint(250,500)
    elif raritynum <= 90: 
        pokemonchosenrarity = 'Rare'
        pokemonchosen = random.choice(pokemons.rarepokemons)
        raritypercent = 9.59
        pokedollarsreward = random.randint(500,1000)
        XPreward = random.randint(500,1000)
    elif raritynum == 95: 
        pokemonchosenrarity = 'Super Rare'
        pokemonchosen = random.choice(pokemons.superrarepokemons)
        raritypercent = 4.94
        pokedollarsreward = random.randint(1000,3000)
        XPreward = random.randint(1000,3000)
    elif raritynum == 100: 
        pokemonchosenrarity = 'Legendary'
        pokemonchosen = random.choice(pokemons.legendarypokemons)
        raritypercent = 0.733
        pokedollarsreward = random.randint(5000,10000)
        XPreward = random.randint(3000,5000)
    else:
        pokemonchosen = random.choice(pokemons.pokemons)
    
    pokemonchosenstr = pokemonchosen.name   

def search(update, context):
    global pokemonchosen
    global ballchoicekb

    choosenewpokemon()
    balls = []
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid)
    realinventory = inventory.userinventory[uid]
    
    if not realinventory['balls']['pokeballs'] <= 0:
        balls.append(pokeballbutton)
    if not realinventory['balls']['greatballs'] == 0:
        balls.append(greatballbutton)
    if not realinventory['balls']['ultraballs'] == 0:
        balls.append(ultraballbutton)
    if not realinventory['balls']['masterballs'] == 0:
        balls.append(masterballbutton)

    ballchoicekb = InlineKeyboardMarkup([balls])
    update.message.reply_animation(pokemonchosen.giflink,caption='A wild %s appeared! \n\nRarity: %s (%s%%). \nBase catchrate: %s\n\nWhat ball do you want to use on it?'%(pokemonchosenstr,pokemonchosenrarity,raritypercent,pokemonchosen.catchRate),reply_markup=ballchoicekb)


def searchcallback(update, context):
        global pokemonchosen
        global pokemonchosenstr
        query = update.callback_query     
        uid = str(query.from_user.id)
        inventory.check_uid(uid)    
        number = random.randint(1,100)    
        catchrate = pokemonchosen.catchRate
        ballused = ''
        # print(query.data)
        # print(number)
        
        if query.data == 'ballchoice:pokeball':
            ballused = 'pokeballs'
        elif query.data == 'ballchoice:greatball':
            catchrate *= 1.5
            ballused = 'greatballs'
        elif query.data == 'ballchoice:ultraball':
            catchrate *= 2
            ballused = 'ultraballs'
        elif query.data == 'ballchoice:masterball':
            catchrate = 100
            ballused = 'masterballs'
        else:
            catchrate = pokemonchosen.catchRate
        
        print(catchrate)
        
        if number <= catchrate:
            a = InputMediaAnimation(media='https://i.gifer.com/MfJw.gif')
            query.edit_message_media(a)

            inventory.add_pokemon(uid,pokemonchosenstr)
            inventory.add_balls(uid,ballused,1)
            number = random.randint(1,3)    
            choosenewpokemon()
            number = random.randint(1,100)    
            inventory.add_XP(uid,XPreward)
            inventory.add_pokedollars(uid,pokedollarsreward)
            
            query.edit_message_caption('Nice job! You captured the %s!\n\nYour catchrate: %s%%.\n\nBalls left:\n\nPokeballs: %s\nGreatballs: %s\nUltraballs: %s\nMasterballs: %s\n\nYou earned %s XP and %s Pokedollars!'%(
            pokemonchosenstr,
            catchrate,
            inventory.userinventory[uid]['balls']['pokeballs'],
            inventory.userinventory[uid]['balls']['greatballs'],
            inventory.userinventory[uid]['balls']['ultraballs'],
            inventory.userinventory[uid]['balls']['masterballs'],
            XPreward,
            pokedollarsreward
            ))
        else:
            # b = InputMediaAnimation(media=open('/Users/Parker/work/PokemonBot/PokeballFail.gif'))
            b = InputMediaAnimation(media='https://media.tenor.com/images/37acc4234291468b6bb1884e3916a341/tenor.gif')
            query.edit_message_media(b)
            query.edit_message_caption('%s broke out of the %s'%(pokemonchosenstr,ballused))
            number = random.randint(1,3)
            inventory.add_balls(uid,ballused,1)
            choosenewpokemon()
            number = random.randint(1,100)    
                
def add_searchhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('search', search))
    dp.add_handler(CallbackQueryHandler(searchcallback,pattern='^ballchoice:[AZaz09_]*'))