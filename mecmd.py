from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand,InputMediaAnimation
import random
import inventory, pokemons


def me(update, context):
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid)
    update.message.reply_text('Trainer %s\nJoined %s\n\nLevel: %s\nXP:%s'%(
        update.message.from_user.first_name,
        inventory.userinventory[uid]['datejoined'],
        inventory.userinventory[uid]['pokedollars'],
        inventory.userinventory[uid]['XP']
    ))

def add_mecmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('me', me))