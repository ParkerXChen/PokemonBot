from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand
import inventory

squritlebutton = InlineKeyboardButton('Squirtle',callback_data='choose:Squirtle')
bulbasourbutton = InlineKeyboardButton('Bulbasour',callback_data='choose:Bulbasour')
charmanderbutton = InlineKeyboardButton('Charmander',callback_data='choose:Charmander')
choosestarterkb = InlineKeyboardMarkup([[squritlebutton, bulbasourbutton, charmanderbutton]])

def start(update, context):
    msg = "Hello %s! I\'m pokemon professor @ParkerChen. \n\nHmmm. You look like you would make a pretty good trainer. Why don't you pick a starter pokemon? Pick one from the following:"%(update.message.from_user.first_name,)
    update.message.reply_text(msg,reply_markup= choosestarterkb)

def startcallback(update, context):
    query = update.callback_query
    if query.data == 'choose:Squirtle':
        inventory.userinventory['pokemons'].append('Squirtle')
        query.edit_message_text('Squirtle? Nice choice! He will be with you for the rest of your journey. Oh, and, you can use the /inventory to see your items. Good luck!')
    elif query.data == 'choose:Bulbasour':
        inventory.userinventory['pokemons'].append('Bulbasour')
        query.edit_message_text('Bulbasour? Nice choice! He will be with you for the rest of your journey. Oh, and, you can use the /inventory to see your items. Good luck!')
    elif query.data == 'choose:Charmander':
        inventory.userinventory['pokemons'].append('Charmander')
        query.edit_message_text('Charmander? Nice choice! He will be with you for the rest of your journey. Oh, and, you can use the /inventory to see your items. Good luck!')

def add_startcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('start', start)) 
    dp.add_handler(CallbackQueryHandler(startcallback,pattern="^choose:[A-Za-z0-9_]*"))