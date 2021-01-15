from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand,InputMediaAnimation
import random
import inventory, pokemons


def me(update, context):
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid)
    update.message.reply_text(f'Trainer {update.message.from_user.first_name}\nJoined on {inventory.userinventory[uid]["datejoined"]}\n\nLevel: {inventory.userinventory[uid]["level"]}\n{inventory.userinventory[uid]["XP"]}/{(inventory.userinventory[uid]["level"]+1)*1000} XP to level up\nXP To next level: {(inventory.userinventory[uid]["level"]+1)*1000-inventory.userinventory[uid]["XP"]}')

def add_mecmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('me', me))