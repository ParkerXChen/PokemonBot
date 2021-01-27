from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
import inventory

def leaderboard(update, context):
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    mostXPperson = ""
    mostXPusername = "" 
    mostXP = -1
    for i in inventory.userinventory.keys():
        if inventory.userinventory[i]['XP'] > mostXP:
            mostXP = inventory.userinventory[i]['XP']
            mostXPperson = inventory.userinventory[i]['name']
            mostXPusername = inventory.userinventory[i]['username']
    update.message.reply_text(f'Most XP:\n{mostXPperson} (@{mostXPusername}): {mostXP}')

def add_leaderboardhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('leaderboard', leaderboard))