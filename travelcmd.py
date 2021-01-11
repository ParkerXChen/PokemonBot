from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import locationslist, inventory, pokemons
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

squritlebutton = InlineKeyboardButton('Squirtle',callback_data='choose:Squirtle')
bulbasourbutton = InlineKeyboardButton('Bulbasaur',callback_data='choose:Bulbasaur')
charmanderbutton = InlineKeyboardButton('Charmander',callback_data='choose:Charmander')
choosestarterkb = InlineKeyboardMarkup([[squritlebutton, bulbasourbutton, charmanderbutton]])

professorshousebutton = InlineKeyboardButton('Professor Maple\'s House',callback_data='location:professorshouse')
chooselocationkb = InlineKeyboardMarkup([[professorshousebutton]])

def travel(update, context):
    update.message.reply_text("Use the /travel command to travel to different locations! Click on a location to travel there!",reply_markup=chooselocationkb)

def travelcallback2(update, context):
    query = update.callback_query
    uid = str(query.from_user.id)
    inventory.check_uid(uid)
    if query.data == 'location:professorshouse':
        if inventory.userinventory[uid]['started'] == False:
            inventory.check_uid
            query.edit_message_text("Hello %s! I\'m Pokemon professor Maple! heard you wanted to become a pokèmon trainer, so I\'m here to help you! Here is are 6 pokeballs and 10000 pokedollars. Also, you can choose your starter pokemon:"%(query.from_user.first_name),reply_markup=choosestarterkb)
            inventory.add_pokedollars(uid,10000)
            inventory.add_balls(uid,'pokeballs',6)
            inventory.userinventory[uid]['started'] = True
            inventory.save()
        else: 
            query.edit_message_text('Hello again! Are you making good progress on your journey?')

def travelcallback1(update, context):
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

def add_travelcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('travel', travel)) 
    dp.add_handler(CallbackQueryHandler(travelcallback1,pattern="^choose:[A-Za-z0-9_:]*"))
    dp.add_handler(CallbackQueryHandler(travelcallback2,pattern="^location:[A-Za-z0-9_:]*"))