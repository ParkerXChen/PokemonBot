from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand
import random
from datetime import datetime,timedelta
import inventory
import pokemons

yes1button = InlineKeyboardButton('Yes',callback_data='search1:yes')
no1button = InlineKeyboardButton('No',callback_data='search1:no')
searchquestion1kb = InlineKeyboardMarkup([[yes1button, no1button]])

yes2button = InlineKeyboardButton('Yes',callback_data='search2:yes')
no2button = InlineKeyboardButton('No',callback_data='search2:no')
searchquestion2kb = InlineKeyboardMarkup([[yes2button, no2button]])

def search(update, context):
    update.message.reply_text("Try to find a pokemon? You have %s pokeballs."%(inventory.userinventory['pokeballs']), reply_markup=searchquestion1kb)

def search1callback(update, context):
    global pokemonchosen
    query = update.callback_query 
    pokemonchosen = random.choice(pokemons.pokemons)
    if query.data == 'search1:yes':
        choice = random.choice(['Yes','Yes','Yes','No','No'])
        if choice == 'No':
            query.edit_message_text('You didn\'t find a pokemon.')
        elif choice == 'Yes':
            query.edit_message_text('You Found a %s! Do you want to try to capture it?'%(pokemonchosen),reply_markup=searchquestion2kb)
    else:
        query.edit_message_text('Search Cancelled')

def search2callback(update, context):
        global pokemonchosen
        
        query = update.callback_query     
        number = random.randint(1,3)    
        if query.data == 'search2:yes':
            if number == 1:
                inventory.userinventory['pokemons'].append(pokemonchosen)
                query.edit_message_text('You captured the %s!'%(pokemonchosen))
                inventory.userinventory['pokeballs'] -= 1
                pokemonchosen = random.choice(pokemons.pokemons)
                number = random.randint(1,3)    
            else:
                if number == 2:
                    query.edit_message_text('You missed the pokemon. At least you still have the pokeball!')
                    number = random.randint(1,3)    
                else:
                    query.edit_message_text('You missed the pokemon AND you lost the pokeball. Sad.')
                    inventory.userinventory['pokeballs'] -= 1
                    number = random.randint(1,3)    
                
def add_searchhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('search', search))
    dp.add_handler(CallbackQueryHandler(search1callback,pattern="^search1:[A-Za-z0-9_]*"))
    dp.add_handler(CallbackQueryHandler(search2callback,pattern="^search2:[A-Za-z0-9_]*"))