from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand,InputMediaAnimation
import inventory

def despawn(update, context):
    uid = str(update.message.from_user.id)
    inventory.userinventory[uid]['Spawnedpokemon'] = False
    update.message.reply_text('You have despawned all pokemon.')

def add_despawncmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('despawn',despawn ))