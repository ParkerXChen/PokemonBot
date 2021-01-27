from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
import inventory

pokecoinsbutton = InlineKeyboardButton('Most pokecoins Leaderboard',callback_data='leaderchoice:pokecoins')
xpbutton = InlineKeyboardButton('Most XP Leaderboard',callback_data='leaderchoice:xp')

backbutton = InlineKeyboardButton('Back',callback_data='pokecoins')

leaderchoicekb = InlineKeyboardMarkup([[pokecoinsbutton],[xpbutton]])
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
    elif query.data == 'leaderchoice:pokecoins':
        uid = str(query.from_user.id)
        inventory.check_uid(uid,query.from_user.first_name,query.from_user.username)    
        mostpokecoins = -1
        for i in inventory.userinventory.keys():
            if inventory.userinventory[i]['pokecoins'] > mostpokecoins:
                mostpokecoins = inventory.userinventory[i]['pokecoins']
                mostpokecoinsperson = inventory.userinventory[i]['name']
                mostpokecoinsusername = inventory.userinventory[i]['username']
        query.edit_message_text(f'Most pokecoins: \n\n{mostpokecoinsperson} (@{mostpokecoinsusername}): {mostpokecoins}')

def add_leaderboardhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('leaderboard', leaderboard))
    dp.add_handler(CallbackQueryHandler(leaderchoicecallback,pattern='^leaderchoice:[AZaz_]*'))