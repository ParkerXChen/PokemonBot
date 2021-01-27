from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import inventory
import random
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton

buycommoncratebutton = InlineKeyboardButton('Poke Crate (500 pokecoins)',callback_data='buycrate:poke')
buyuncommoncratebutton = InlineKeyboardButton('Great Crate (1000 pokecoins)',callback_data='buycrate:great')
buyrarecratebutton = InlineKeyboardButton('Ultra Crate (5000 pokecoins)',callback_data='buycrate:ultra')
buylegendarycratebutton = InlineKeyboardButton('Master Crate (20000 pokecoins)',callback_data='buycrate:master')

buycrateskb = InlineKeyboardMarkup([[buycommoncratebutton],[buyuncommoncratebutton],[buyrarecratebutton],[buylegendarycratebutton]])

def crateshop(update, context):
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    update.message.reply_text(f"Hello {update.message.from_user.first_name}! Welcome to the Crate Shop! Here you can buy crates, that contain things for your adventure!  \n\nYou have {inventory.userinventory[uid]['pokecoins']} pokecoins.\n\nClick on an item to buy it.",reply_markup=buycrateskb)

def crateshopcallback(update, context):
    query = update.callback_query
    uid = str(query.from_user.id)
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    print (uid)
    if query.data == 'buycrate:poke':
        if not inventory.userinventory[uid]['pokecoins'] < 500:
            pokeballsnum = random.randint(3,8)
            greatballsnum = random.randint(1,5)
            query.message.edit_text('You purchased a Poke Crate! Inside were:\n\nx%s Pokeballs\nx%s Greatballs'%(pokeballsnum,greatballsnum))
            inventory.add_pokecoins(uid,-500)
            inventory.add_balls(uid,'pokeballs',pokeballsnum)
            inventory.add_balls(uid,'greatballs',greatballsnum) 
        else:
            query.edit_message_text('Sorry, but you cannot afford this item.')
    elif query.data == 'buycrate:great':
        if not inventory.userinventory[uid]['pokecoins'] < 1000:
            pokeballsnum = random.randint(10,20)
            greatballsnum = random.randint(5,10)
            query.message.edit_text('You purchased an Great Crate! Inside were:\n\nx%s Pokeballs\nx%s Greatballs'%(pokeballsnum,greatballsnum))
            inventory.add_pokecoins(uid,-1000)
            inventory.add_balls(uid,'pokeballs',pokeballsnum)
            inventory.add_balls(uid,'greatballs',greatballsnum)
        else:
            query.edit_message_text('Sorry, but you cannot afford this item.')
    elif query.data == 'buycrate:ultra':
        if not inventory.userinventory[uid]['pokecoins'] < 5000:
            pokeballsnum = random.randint(15,25)
            greatballsnum = random.randint(10,15)
            ultraballsnum = random.randint(1,5)
            query.message.edit_text('You purchased an Ultra crate! Inside were:\n\nx%s Pokeballs\nx%s Greatballs\nx%s Ultraballs'%(pokeballsnum,greatballsnum,ultraballsnum))
            inventory.add_pokecoins(uid,-5000)
            inventory.add_balls(uid,'pokeballs',pokeballsnum)
            inventory.add_balls(uid,'greatballs',greatballsnum)
            inventory.add_balls(uid,'ultraballs',ultraballsnum)
        else:
            query.edit_message_text('Sorry, but you cannot afford this item.')
    elif query.data == 'buycrate:master':
        if not inventory.userinventory[uid]['pokecoins'] < 50000:
            pokeballsnum = random.randint(20,30)
            greatballsnum = random.randint(15,25)
            ultraballsnum = random.randint(5,15)
            masterballsnum = random.randint(1,3)
            query.message.edit_text('You purchased an Master crate! Inside were:\n\nx%s Pokeballs\nx%s Greatballs\nx%s Ultraballs\nx%s Masterballs'%(pokeballsnum,greatballsnum,ultraballsnum,masterballsnum))
            inventory.add_pokecoins(uid,-50000)
            inventory.add_balls(uid,'pokeballs',pokeballsnum)
            inventory.add_balls(uid,'greatballs',greatballsnum)
            inventory.add_balls(uid,'ultraballs',ultraballsnum)
            inventory.add_balls(uid,'masterballs',ultraballsnum)
        else:
            query.edit_message_text('Sorry, but you cannot afford this item.')




def add_crateshopcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('crateshop', crateshop)) 
    dp.add_handler(CallbackQueryHandler(crateshopcallback,pattern="^buycrate:[A-Za-z0-9_:]*"))