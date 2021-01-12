from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand,InputMediaAnimation
import random
import inventory, pokemons


def me(update, context):
    uid = str(update.message.from_user.id)

    update.message.reply_text('Trainer %s\n\nPokedollars: %s'%(
        update.message.from_user.first_name,
        inventory.userinventory[uid]['pokedollars']
    ))

def add_mecmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('me', me))