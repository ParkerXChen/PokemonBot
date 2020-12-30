from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

buypokeballbutton = InlineKeyboardButton('10 Pokeballs (50 Pokedollars)',callback_data='buy:tenpokeballs')

buykb = InlineKeyboardMarkup([[buypokeballbutton]])

def shop(update, context):
    update.message.reply_text("Hi! Welcome to the PokeShop! Here, you can buy things for your adventure! Click on an item to buy it.",reply_markup=buykb)

def shopcallback(update, context):
    query = update.callback_query
    print (query.data)

    if query.data == 'buy:tenpokeballs':
        if inventory.userinventory['pokedollars'] < 50:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokedollars!'%(inventory.userinventory['balls']['pokeballs'],inventory.userinventory['pokedollars']))
            inventory.add_pokedollars(-50)
            inventory.add_pokeballs(10)

def add_shopcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('shop', shop)) 
    dp.add_handler(CallbackQueryHandler(shopcallback,pattern="^buy:[A-Za-z0-9_:]*"))