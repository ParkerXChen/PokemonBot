from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import locationslist, inventory
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

squritlebutton = InlineKeyboardButton('Squirtle',callback_data='choose:Squirtle')
bulbasourbutton = InlineKeyboardButton('Bulbasour',callback_data='choose:Bulbasaur')
charmanderbutton = InlineKeyboardButton('Charmander',callback_data='choose:Charmander')
choosestarterkb = InlineKeyboardMarkup([[squritlebutton, bulbasourbutton, charmanderbutton]])

professorshousebutton = InlineKeyboardButton('Professor Parker\'s House',callback_data='location:professorshouse')
chooselocationkb = InlineKeyboardMarkup([[professorshousebutton]])

def travel(update, context):
    update.message.reply_text("Use the /travel command to travel to different locations! Click on a location to travel there!",reply_markup=chooselocationkb)

def travelcallback2(update, context):
    query = update.callback_query
    user = update.effective_user
    inventory.check_uid(user.id)
    if query.data == 'location:professorshouse':
        if inventory.userinventory[user.id]['started'] == False:
            query.edit_message_text("Hello %s! I\'m Pokemon professor Parker! heard you wanted to become a pokèmon trainer, so I\'m here to help you! Here is a pokedex, 6 pokeballs, and 100 pokedollars. Also, you can choose your starter pokemon:"%(user.first_name),reply_markup=choosestarterkb)
            inventory.add_pokedollars(user.id,100)
            inventory.add_pokeballs(user.id,6)
            inventory.add_item(user.id,'pokedex')
            inventory.userinventory[user.id]['started'] = True
            inventory.save()
        else: 
            query.edit_message_text('Hello again! Are you making good progress on your journey?')

def travelcallback1(update, context):
    user = update.effective_user
    query = update.callback_query
    if query.data == 'choose:Squirtle':
        inventory.add_pokemon(user.id,'Squirtle')
        query.edit_message_text('Squirtle? Nice choice! He will be with you for the rest of your journey. Good luck!')
    elif query.data == 'choose:Bulbasaur':
        inventory.add_pokemon(user.id,'Bulbasaur')
        query.edit_message_text('Bulbasaur? Nice choice! He will be with you for the rest of your journey. Good luck!')
    elif query.data == 'choose:Charmander':
        inventory.add_pokemon(user.id,'Charmander')
        query.edit_message_text('Charmander? Nice choice! He will be with you for the rest of your journey. Good luck!') 

def add_travelcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('travel', travel)) 
    dp.add_handler(CallbackQueryHandler(travelcallback1,pattern="^choose:[A-Za-z0-9_:]*"))
    dp.add_handler(CallbackQueryHandler(travelcallback2,pattern="^location:[A-Za-z0-9_:]*"))