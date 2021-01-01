from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand
import random
import inventory, pokemons
import time

yesbutton = InlineKeyboardButton('Yes',callback_data='search:yes')
nobutton = InlineKeyboardButton('No',callback_data='search:no')
searchquestionkb = InlineKeyboardMarkup([[yesbutton, nobutton]])

pokeballbutton = InlineKeyboardButton('Pokeball',callback_data='ballchoice:pokeball')
greatball = InlineKeyboardButton('Greatball',callback_data='ballchoice:greatball')

pokemonchosenrarity = '' 
pokemonchosenstr = ''
raritypercent = 0

def choosenewpokemon():   
    global pokemonchosen
    global pokemonchosenstr
    global pokemonchosenrarity
    global raritypercent
    raritynum = random.randint(1,100)

    if raritynum <= 65:
        pokemonchosenrarity = 'Common'
        pokemonchosen = random.choice(pokemons.commonpokemons)
        raritypercent = 54.76
    elif raritynum <= 80: 
        pokemonchosenrarity = 'Uncommon'
        pokemonchosen = random.choice(pokemons.uncommonpokemons)
        raritypercent = 14.47
    elif raritynum <= 90: 
        pokemonchosenrarity = 'Rare'
        pokemonchosen = random.choice(pokemons.rarepokemons)
        raritypercent = 9.59
    elif raritynum == 95: 
        pokemonchosenrarity = 'Super Rare'
        pokemonchosen = random.choice(pokemons.superrarepokemons)
        raritypercent = 4.94
    elif raritynum == 100: 
        pokemonchosenrarity = 'Legendary'
        pokemonchosen = random.choice(pokemons.legendarypokemons)
        raritypercent = 0.733
    
    pokemonchosenstr = pokemonchosen.name   

def search(update, context):
    global pokemonchosen
    choosenewpokemon()
    update.message.reply_animation(pokemonchosen.giflink,caption='You Found a wild %s! \n\nRarity: %s (%s%%). \nBase catchrate: %s\n\nDo you want to try to capture it?'%(pokemonchosenstr,pokemonchosenrarity,raritypercent,pokemonchosen.catchRate),reply_markup=searchquestionkb)


def searchcallback(update, context):
        global pokemonchosen
        global pokemonchosenstr
        query = update.callback_query     
        uid = str(query.from_user.id)
        inventory.check_uid(uid)    
        number = random.randint(1,100)    
        if query.data == 'search:yes':
            if inventory.userinventory[uid]['balls']['pokeballs'] <= 0:
                query.edit_message_caption('You don\'t have any pokeballs!')
            else:
                if number <= pokemonchosen.catchRate:
                    query.edit_message_caption('Nice job! You captured the %s! \n\nYou earned 500 XP and 100 Pokecoins!'%(pokemonchosenstr))
                    inventory.add_pokemon(uid,pokemonchosenstr)
                    inventory.add_pokeballs(uid,-1)
                    number = random.randint(1,3)    
                    choosenewpokemon()
                    number = random.randint(1,100)    
                    inventory.add_XP(uid,500)
                    inventory.add_pokedollars(uid,100)
                else:
                        query.edit_message_caption('%s broke out of the pokeball!'%(pokemonchosenstr))
                        number = random.randint(1,3)
                        inventory.add_pokeballs(uid,-1)
                        choosenewpokemon()
                        number = random.randint(1,100)    
                
def add_searchhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('search', search))
    dp.add_handler(CallbackQueryHandler(searchcallback,pattern='^search:[A-Za-z0-9_]*'))