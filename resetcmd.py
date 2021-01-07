from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

yesbutton = InlineKeyboardButton('Yes',callback_data='YorN1:yes')
nobutton = InlineKeyboardButton('No',callback_data='YorN1:no')
YorN1kb = InlineKeyboardMarkup([[yesbutton, nobutton]])

def reset(update, context):
    update.message.reply_text('Are you sure you want to reset the game? WARNING: YOU WILL GAIN NOTHING, AND NOTHING WILL BE SAVED',reply_markup=YorN1kb)

def resetcallback(update, context):
    query = update.callback_query
    if query.data == 'YorN1:yes':
        uid = str(query.from_user.id)
        msg = 'Your game has been reset.'
        inventory.reset(uid)
    else:
        msg = 'No? OK.'
    query.edit_message_text(msg)

def add_resetcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('reset', reset)) 
    dp.add_handler(CallbackQueryHandler(resetcallback,pattern="^YorN1:[A-Za-z0-9_:]*"))
    