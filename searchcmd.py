from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand
import random
import inventory, pokemons
import time

yes2button = InlineKeyboardButton('Yes',callback_data='search2:yes')
no2button = InlineKeyboardButton('No',callback_data='search2:no')
searchquestion2kb = InlineKeyboardMarkup([[yes2button, no2button]])

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
    choice = random.choice(['Yes','Yes','Yes','No','No'])
    if choice == 'No':
        update.message.reply_text('You didn\'t find a pokemon.')
    elif choice == 'Yes':
        print(pokemonchosenstr)
        update.message.reply_animation(pokemonchosen.giflink,caption='You Found a %s! \n\nRarity: %s (%s%%). \nBase catchrate: %s\n\nDo you want to try to capture it?'%(pokemonchosenstr,pokemonchosenrarity,raritypercent,pokemonchosen.catchRate),reply_markup=searchquestion2kb)


def search2callback(update, context):
        global pokemonchosen
        global pokemonchosenstr
        query = update.callback_query     
        uid = str(query.from_user.id)
        inventory.check_uid(uid)    
        number = random.randint(1,100)    
        if query.data == 'search2:yes':
            if inventory.userinventory[uid]['balls']['pokeballs'] <= 0:
                query.edit_message_caption('You don\'t have any pokeballs!')
            else:
                if number <= pokemonchosen.catchRate:
                    query.edit_message_caption('Nice job! You captured the %s! \n\nYou earned 500 XP and 100 Pokecoins! \n\nCatchrate of %s: %s%%'%(pokemonchosenstr,pokemonchosenstr,pokemonchosen.catchRate))
                    print (pokemonchosenstr)
                    inventory.add_pokemon(uid,pokemonchosenstr)
                    inventory.add_pokeballs(uid,-1)
                    number = random.randint(1,3)    
                    choosenewpokemon()
                    number = random.randint(1,100)    
                    inventory.add_XP(uid,500)
                    inventory.add_pokedollars(uid,100)
                else:
                        query.edit_message_caption('%s broke out of the pokeball! Catchrate of %s: %s%%'%(pokemonchosenstr,pokemonchosenstr,pokemonchosen.catchRate))
                        number = random.randint(1,3)
                        inventory.add_pokeballs(uid,-1)
                        choosenewpokemon()
                        number = random.randint(1,100)    
                
def add_searchhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('search', search))
    dp.add_handler(CallbackQueryHandler(search2callback,pattern='^search2:[A-Za-z0-9_]*'))