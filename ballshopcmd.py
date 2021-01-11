from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

buy10pokeballsbutton = InlineKeyboardButton('25 Pokeballs (x1 Capture Rate) (1250 Pokedollars)',callback_data='buyballs:tfpokeballs')
buy25pokeballsbutton = InlineKeyboardButton('50 Pokeballs (x1 Capture Rate) (2000 Pokedollars)',callback_data='buyballs:ftypokeballs')
buy10greatballsbutton = InlineKeyboardButton('10 Greatballs (x1.5 Capture Rate) (1250 Pokedollars)',callback_data='buyballs:tgreatballs')
buy25greatballsbutton = InlineKeyboardButton('25 Greatballs (x1.5 Capture Rate) (3000 Pokedollars)',callback_data='buyballs:tfgreatballs')
buy10ultraballsbutton = InlineKeyboardButton('5 Ultraballs (x2 Capture Rate) (2000 Pokedollars)',callback_data='buyballs:fultraballs')
buy25ultraballsbutton = InlineKeyboardButton('15 Ultraballs (x2 Capture Rate) (1000 Pokedollars)',callback_data='buyballs:fteultraballs')
buy10masterballsbutton = InlineKeyboardButton('1 Masterball (x255 Capture Rate) (10000 Pokedollars)',callback_data='buyballs:omasterballs')
buy25masterballsbutton = InlineKeyboardButton('5 Masterballs (x255 Capture Rate) (45000 Pokedollars)',callback_data='buyballs:fmasterballs')

buyballskb = InlineKeyboardMarkup([[buy10pokeballsbutton],[buy25pokeballsbutton],[buy10greatballsbutton],[buy25greatballsbutton],[buy10ultraballsbutton],[buy25ultraballsbutton],[buy10masterballsbutton],[buy25masterballsbutton]])

def ballshop(update, context):
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid)
    update.message.reply_text(f"Hello {update.message.from_user.first_name}! Welcome to the BallShop! Here, you can buy Balls for your adventure!  \n\nYou have {inventory.userinventory[uid]['pokedollars']} pokedollars.\n\nClick on an item to buy it.",reply_markup=buyballskb)

def ballshopcallback(update, context):
    query = update.callback_query
    uid = str(query.from_user.id)
    if query.data == 'buyballs:tfpokeballs':
        if inventory.userinventory[uid]['pokedollars'] < 1250:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-1250)
            inventory.add_balls(uid,'pokeballs',25)
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['pokeballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:ftypokeballs':
        if inventory.userinventory[uid]['pokedollars'] < 2000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-2000)
            inventory.add_balls(uid,'pokeballs',50)            
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['pokeballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:tgreatballs':
        if inventory.userinventory[uid]['pokedollars'] < 1250:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-1250)
            inventory.add_balls(uid,'greatballs',10)            
            query.edit_message_text('Purchase sucsessful! You now have %s greatballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['greatballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:tfgreatballs':
        if inventory.userinventory[uid]['pokedollars'] < 3000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-3000)
            inventory.add_balls(uid,'greatballs',25)            
            query.edit_message_text('Purchase sucsessful! You now have %s greatballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['greatballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:fultraballs':
        if inventory.userinventory[uid]['pokedollars'] < 2000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-2000)
            inventory.add_balls(uid,'ultraballs',5)            
            query.edit_message_text('Purchase sucsessful! You now have %s ultraballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['ultraballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:fteultraballs':
        if inventory.userinventory[uid]['pokedollars'] < 5000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-5000)
            inventory.add_balls(uid,'ultraballs',15)            
            query.edit_message_text('Purchase sucsessful! You now have %s ultraballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['ultraballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:omasterballs':
        if inventory.userinventory[uid]['pokedollars'] < 10000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-10000)
            inventory.add_balls(uid,'masterballs',1)            
            query.edit_message_text('Purchase sucsessful! You now have %s masterballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['masterballs'],inventory.userinventory[uid]['pokedollars']))
    elif query.data == 'buyballs:fmasterballs':
        if inventory.userinventory[uid]['pokedollars'] < 45000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokedollars(uid,-45000)
            inventory.add_balls(uid,'masterballs',5)            
            query.edit_message_text('Purchase sucsessful! You now have %s masterballs and %s pokedollars!'%(inventory.userinventory[uid]['balls']['masterballs'],inventory.userinventory[uid]['pokedollars']))

def add_ballshopcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('ballshop', ballshop)) 
    dp.add_handler(CallbackQueryHandler(ballshopcallback,pattern="^buyballs:[A-Za-z0-9_:]*"))