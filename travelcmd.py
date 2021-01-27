from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory, pokemons
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

squritlebutton = InlineKeyboardButton('Squirtle',callback_data='choose:Squirtle')
bulbasourbutton = InlineKeyboardButton('Bulbasaur',callback_data='choose:Bulbasaur')
charmanderbutton = InlineKeyboardButton('Charmander',callback_data='choose:Charmander')
choosestarterkb = InlineKeyboardMarkup([[squritlebutton, bulbasourbutton, charmanderbutton]])

professorshousebutton = InlineKeyboardButton('Professor Maple\'s House',callback_data='location:professorshouse')
ballshopbutton = InlineKeyboardButton('The Pokeball Shop',callback_data='location:ballshop')
chooselocationkb = InlineKeyboardMarkup([[professorshousebutton],[ballshopbutton]])

buy10pokeballsbutton = InlineKeyboardButton('25 Pokeballs (x1 Capture Rate) (1250 pokecoins)',callback_data='buyballs:tfpokeballs')
buy25pokeballsbutton = InlineKeyboardButton('50 Pokeballs (x1 Capture Rate) (2000 pokecoins)',callback_data='buyballs:ftypokeballs')
buy10greatballsbutton = InlineKeyboardButton('10 Greatballs (x1.5 Capture Rate) (1250 pokecoins)',callback_data='buyballs:tgreatballs')
buy25greatballsbutton = InlineKeyboardButton('25 Greatballs (x1.5 Capture Rate) (3000 pokecoins)',callback_data='buyballs:tfgreatballs')
buy10ultraballsbutton = InlineKeyboardButton('5 Ultraballs (x2 Capture Rate) (2000 pokecoins)',callback_data='buyballs:fultraballs')
buy25ultraballsbutton = InlineKeyboardButton('15 Ultraballs (x2 Capture Rate) (10000 pokecoins)',callback_data='buyballs:fteultraballs')
buy10masterballsbutton = InlineKeyboardButton('1 Masterball (x255 Capture Rate) (10000 pokecoins)',callback_data='buyballs:omasterballs')
buy25masterballsbutton = InlineKeyboardButton('5 Masterballs (x255 Capture Rate) (45000 pokecoins)',callback_data='buyballs:fmasterballs')

buyballskb = InlineKeyboardMarkup([[buy10pokeballsbutton],[buy25pokeballsbutton],[buy10greatballsbutton],[buy25greatballsbutton],[buy10ultraballsbutton],[buy25ultraballsbutton],[buy10masterballsbutton],[buy25masterballsbutton]])

def travel(update, context):
    update.message.reply_text("Use the /travel command to travel to different locations! Click on a location to travel there!",reply_markup=chooselocationkb)

def travelcallback(update, context):
    query = update.callback_query
    uid = str(query.from_user.id)
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    if query.data == 'location:professorshouse':
        if inventory.userinventory[uid]['started'] == False:
            inventory.check_uid
            query.edit_message_text("Hello %s! I\'m Pokemon professor Maple! heard you wanted to become a pokèmon trainer, so I\'m here to help you! Here is are 6 pokeballs and 500 pokecoins. Also, you can choose your starter pokemon:"%(query.from_user.first_name),reply_markup=choosestarterkb)
            inventory.add_pokecoins(uid,500)
            inventory.add_balls(uid,'pokeballs',6)
            inventory.userinventory[uid]['started'] = True
            inventory.save()
        else: 
            query.edit_message_text('Hello again! Are you making good progress on your journey?')
    elif query.data == 'location:ballshop':
        query.edit_message_text(f"Hello {query.from_user.first_name}! Welcome to the BallShop! Here, you can buy Balls for your adventure!  \n\nYou have {inventory.userinventory[uid]['pokecoins']} pokecoins.\n\nClick on an item to buy it.",reply_markup=buyballskb)

def choosestartercallback(update, context):
    user = update.effective_user
    query = update.callback_query
    if query.data == 'choose:Squirtle':
        inventory.add_pokemon(user.id,pokemons.squirtle)
        query.edit_message_text('Squirtle? Nice choice! He will be with you for the rest of your journey. Good luck!')
    elif query.data == 'choose:Bulbasaur':
        inventory.add_pokemon(user.id,pokemons.bulbasaur)
        query.edit_message_text('Bulbasaur? Nice choice! He will be with you for the rest of your journey. Good luck!')
    elif query.data == 'choose:Charmander':
        inventory.add_pokemon(user.id,pokemons.charmander)
        query.edit_message_text('Charmander? Nice choice! He will be with you for the rest of your journey. Good luck!') 


def ballshopcallback(update, context):
    query = update.callback_query
    uid = str(query.from_user.id)
    if query.data == 'buyballs:tfpokeballs':
        if inventory.userinventory[uid]['pokecoins'] < 1250:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-1250)
            inventory.add_balls(uid,'pokeballs',25)
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['pokeballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:ftypokeballs':
        if inventory.userinventory[uid]['pokecoins'] < 2000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-2000)
            inventory.add_balls(uid,'pokeballs',50)            
            query.edit_message_text('Purchase sucsessful! You now have %s pokeballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['pokeballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:tgreatballs':
        if inventory.userinventory[uid]['pokecoins'] < 1250:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-1250)
            inventory.add_balls(uid,'greatballs',10)            
            query.edit_message_text('Purchase sucsessful! You now have %s greatballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['greatballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:tfgreatballs':
        if inventory.userinventory[uid]['pokecoins'] < 3000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-3000)
            inventory.add_balls(uid,'greatballs',25)            
            query.edit_message_text('Purchase sucsessful! You now have %s greatballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['greatballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:fultraballs':
        if inventory.userinventory[uid]['pokecoins'] < 2000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-2000)
            inventory.add_balls(uid,'ultraballs',5)            
            query.edit_message_text('Purchase sucsessful! You now have %s ultraballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['ultraballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:fteultraballs':
        if inventory.userinventory[uid]['pokecoins'] < 5000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-5000)
            inventory.add_balls(uid,'ultraballs',15)            
            query.edit_message_text('Purchase sucsessful! You now have %s ultraballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['ultraballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:omasterballs':
        if inventory.userinventory[uid]['pokecoins'] < 10000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-10000)
            inventory.add_balls(uid,'masterballs',1)            
            query.edit_message_text('Purchase sucsessful! You now have %s masterballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['masterballs'],inventory.userinventory[uid]['pokecoins']))
    elif query.data == 'buyballs:fmasterballs':
        if inventory.userinventory[uid]['pokecoins'] < 45000:
            query.edit_message_text('Sorry, but you cannot afford this item.')
        else:
            inventory.add_pokecoins(uid,-45000)
            inventory.add_balls(uid,'masterballs',5)            
            query.edit_message_text('Purchase sucsessful! You now have %s masterballs and %s pokecoins!'%(inventory.userinventory[uid]['balls']['masterballs'],inventory.userinventory[uid]['pokecoins']))

def add_travelcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('travel', travel)) 
    dp.add_handler(CallbackQueryHandler(choosestartercallback,pattern="^choose:[A-Za-z0-9_:]*"))
    dp.add_handler(CallbackQueryHandler(travelcallback,pattern="^location:[A-Za-z0-9_:]*"))
    dp.add_handler(CallbackQueryHandler(ballshopcallback,pattern="^buyballs:[A-Za-z0-9_:]*"))