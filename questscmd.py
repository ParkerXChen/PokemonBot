from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

def quests(update,context):
    uid = update.message.from_user.id
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    if len(inventory.userinventory[uid]['quests']) == 0:
        update.message.reply_text('You currently have no quests. Go to Pallet Town or the professor\'s house to get new quests.')
    else:
        update.message.reply_text(inventory.userinventory[uid]['quests'])

def add_questscmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('quests', quests)) 