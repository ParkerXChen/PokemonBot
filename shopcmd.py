from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

buy10pokeballsbutton = InlineKeyboardButton('10 Pokeballs (50 Pokedollars)',callback_data='buy:tenpokeballs')
buy50pokeballsbutton = InlineKeyboardButton('50 Pokeballs (200 Pokedollars)',callback_data='buy:fiftypokeballs')

buykb = InlineKeyboardMarkup([[buy10pokeballsbutton,buy50pokeballsbutton]])

def shop(update, context):
    update.message.reply_text("Hi! Welcome to the PokeShop! Here, you can buy things for your adventure! Click on an item to buy it.",reply_markup=buykb)

def shopcallback(update, context):
    query = update.callback_query
    print (query.data)
    uid = str(query.from_user.id)
    if query.data == 'buy:tenpokeballs':
        if inventory.userinventory[uid]['pokedollars'] < 50:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-50)
            inventory.add_balls(uid,'pokeballs',10)
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['pokeballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buy:fiftypokeballs':
        if inventory.userinventory[uid]['pokedollars'] < 200:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-200)
            inventory.add_balls(uid,'pokeballs',50)            
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['pokeballs'],inventory.userinventory[uid]['pokedollars']))

def add_shopcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('shop', shop)) 
    dp.add_handler(CallbackQueryHandler(shopcallback,pattern="^buy:[A-Za-z0-9_:]*"))