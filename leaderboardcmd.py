from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
import inventory

pokedollarsbutton = InlineKeyboardButton('Most Pokedollars Leaderboard',callback_data='leaderchoice:pokedollars')
xpbutton = InlineKeyboardButton('Most XP Leaderboard',callback_data='leaderchoice:xp')

backbutton = InlineKeyboardButton('Back',callback_data='pokedollars')

leaderchoicekb = InlineKeyboardMarkup([[pokedollarsbutton],[xpbutton]])
backkb = InlineKeyboardMarkup([backbutton])

def leaderboard(update, context):
    update.message.reply_text(f'Welcome to the Leaderboards! Here, you can check who the top players in the game are. Click on a type of leaderboard to view it!',reply_markup=leaderchoicekb)

def leaderchoicecallback(update,context):
    query = update.callback_query
    if query.data == 'leaderchoice:xp':
        uid = str(query.from_user.id)
        inventory.check_uid(uid,query.from_user.first_name,query.from_user.username)    
        for i in inventory.userinventory.keys():
            if inventory.userinventory[i]['XP'] > mostXP:
                mostXP = inventory.userinventory[i]['XP']
                mostXPperson = inventory.userinventory[i]['name']
                mostXPusername = inventory.userinventory[i]['username']
        query.edit_message_text(f'Most XP: \n\n{mostXPperson} (@{mostXPusername}): {mostXP}')
    elif query.data == 'leaderchoice:pokedollars':
        uid = str(query.from_user.id)
        inventory.check_uid(uid,query.from_user.first_name,query.from_user.username)    
        mostpokedollars = -1
        for i in inventory.userinventory.keys():
            if inventory.userinventory[i]['pokedollars'] > mostpokedollars:
                mostpokedollars = inventory.userinventory[i]['pokedollars']
                mostpokedollarsperson = inventory.userinventory[i]['name']
                mostpokedollarsusername = inventory.userinventory[i]['username']
        query.edit_message_text(f'Most Pokedollars: \n\n{mostpokedollarsperson} (@{mostpokedollarsusername}): {mostpokedollars}')

def add_leaderboardhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('leaderboard', leaderboard))
    dp.add_handler(CallbackQueryHandler(leaderchoicecallback,pattern='^leaderchoice:[AZaz_]*'))