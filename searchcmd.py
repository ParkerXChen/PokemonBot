from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand
import random
import inventory, pokemons
import time

yes1button = InlineKeyboardButton('Yes',callback_data='search1:yes')
no1button = InlineKeyboardButton('No',callback_data='search1:no')
searchquestion1kb = InlineKeyboardMarkup([[yes1button, no1button]])

yes2button = InlineKeyboardButton('Yes',callback_data='search2:yes')
no2button = InlineKeyboardButton('No',callback_data='search2:no')
searchquestion2kb = InlineKeyboardMarkup([[yes2button, no2button]])

pokeballbutton = InlineKeyboardButton('Pokeball',callback_data='ballchoice:pokeball')
greatball = InlineKeyboardButton('Greatball',callback_data='ballchoice:greatball')

pokemonchosen = []
pokemonchosenstr = ''
def choosenewpokemon():   
    global pokemonchosen
    global pokemonchosenstr
    
    raritynum = random.randint(1,100)

    if raritynum <= 65:
        pokemonchosen = random.choice(pokemons.commonpokemons)
    elif raritynum <= 80: 
        pokemonchosen = random.choice(pokemons.uncommonpokemons)
    elif raritynum <= 90: 
        pokemonchosen = random.choice(pokemons.rarepokemons)
    elif raritynum == 95: 
        pokemonchosen = random.choice(pokemons.superrarepokemons)
    elif raritynum == 100: 
        pokemonchosen = random.choice(pokemons.legendarypokemons)
    
    pokemonchosenstr = pokemonchosen.name   



def search(update, context):
    update.message.reply_text('Try to find a pokemon?',reply_markup=searchquestion1kb)
    print(pokemonchosen)
    print(pokemonchosenstr)

def search1callback(update, context):
    global pokemonchosen
    choosenewpokemon()
    query = update.callback_query 
    if query.data == 'search1:yes':
        choice = random.choice(['Yes','Yes','Yes','No','No'])
        if choice == 'No':
            query.edit_message_text('You didn\'t find a pokemon.')
        elif choice == 'Yes':
            print(pokemonchosenstr)
            query.edit_message_text('You Found a %s! Do you want to try to capture it?'%(pokemonchosenstr),reply_markup=searchquestion2kb)
    else:
        query.edit_message_text('Search Cancelled')

def search2callback(update, context):
        global pokemonchosen
        global pokemonchosenstr
        query = update.callback_query     
        uid = str(query.from_user.id)
        inventory.check_uid(uid)    
        number = random.randint(1,100)    
        if query.data == 'search2:yes':
            if inventory.userinventory[uid]['balls']['pokeballs'] <= 0:
                query.edit_message_text('You don\'t have any pokeballs!')
            else:
                if number <= pokemonchosen.catchRate:
                    query.edit_message_text('Nice job! You captured the %s! \n\nYou earned 500 XP and 100 Pokecoins! \n\nCatchrate of %s: %s%%'%(pokemonchosenstr,pokemonchosenstr,pokemonchosen.catchRate))
                    print (pokemonchosenstr)
                    inventory.add_pokemon(uid,pokemonchosenstr)
                    inventory.add_pokeballs(uid,-1)
                    number = random.randint(1,3)    
                    choosenewpokemon()
                    number = random.randint(1,100)    
                    inventory.add_XP(uid,500)
                    inventory.add_pokedollars(uid,100)
                else:
                        query.edit_message_text('%s broke out of the pokeball! Catchrate of %s: %s%%'%(pokemonchosenstr,pokemonchosenstr,pokemonchosen.catchRate))
                        number = random.randint(1,3)
                        inventory.add_pokeballs(uid,-1)
                        choosenewpokemon()
                        number = random.randint(1,100)    
                
def add_searchhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('search', search))
    dp.add_handler(CallbackQueryHandler(search1callback,pattern='^search1:[A-Za-z0-9_]*'))
    dp.add_handler(CallbackQueryHandler(search2callback,pattern='^search2:[A-Za-z0-9_]*'))