from telegram.ext import Dispatcher,CommandHandler
import inventory

def inventorycmd(update, context):
    uid = str(update.effective_user.id)
    inventory.check_uid(uid)
    pokemonslist = ''
    pokemonslist += 'Your pokemon are:'

    if not inventory.userinventory[uid]['pokemons'] == []:
        for i in inventory.userinventory[uid]['pokemons']:
            pokemonslist += '%s,'%(i)
    else:
        pokemonslist = 'You have no pokemons'

    itemlist = 'Some other items you have are: '
    if len(inventory.userinventory[uid]['otheritems']) == 0:
        itemlist = 'You have no other items.'
    else:
        for i in inventory.userinventory[uid]['otheritems']:
            itemlist += '%s,'%(i)
    
    buddy = ''
    if inventory.userinventory[uid]['buddy'] == '':
        buddy = 'You do not have a buddy equipped'
    else:
        buddy = inventory.userinventory[uid]['buddy']


    update.message.reply_text(
        'XP: You have %s XP.\n\nBalls: You have %s Pokeballs, %s Greatballs, %s Ultraballs, and %s Masterballs.\n\nBuddy: %s.\n\nPokedollars: You have %s Pokedollars.\n\nOther Items: %s'%(
        inventory.userinventory[uid]['XP'],
        inventory.userinventory[uid]['balls']['pokeballs'],
        inventory.userinventory[uid]['balls']['greatballs'],
        inventory.userinventory[uid]['balls']['ultraballs'],
        inventory.userinventory[uid]['balls']['masterballs'],
        buddy,
        inventory.userinventory[uid]['pokedollars'],
        itemlist
    ))

def add_inventorycmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('inventory', inventorycmd)) 