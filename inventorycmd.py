from telegram.ext import Dispatcher,CommandHandler
import inventory

def inventorycmd(update, context):
    pokemonslist = ''
    pokemonslist += 'Your pokemon are:'
    
    if not inventory.userinventory['pokemons'] == []:
        for i in inventory.userinventory['pokemons']:
            pokemonslist += '%s,'%(i)
    else:
        pokemonslist = 'You have no pokemons'

    itemlist = 'Some other items you have are: '
    if len(inventory.userinventory['otheritems']) == 0:
        itemlist = 'You have no other items.'
    else:
        for i in inventory.userinventory['otheritems']:
            itemlist += '%s,'%(i)
    
    buddy = ''
    if inventory.userinventory['buddy'] == '':
        buddy = 'You do not have a buddy equipped'
    else:
        buddy = inventory.userinventory['buddy']


    update.message.reply_text(
        'XP: You have %s XP.\n\nBalls: You have %s Pokeballs, %s Greatballs, %s Ultraballs, and %s Masterballs.\n\nBuddy: %s.\n\nPokedollars: You have %s Pokedollars.\n\nOther Items: %s'%(
        inventory.userinventory['XP'],
        inventory.userinventory['balls']['pokeballs'],
        inventory.userinventory['balls']['greatballs'],
        inventory.userinventory['balls']['ultraballs'],
        inventory.userinventory['balls']['masterballs'],
        buddy,
        inventory.userinventory['pokedollars'],
        itemlist)
    )

def add_inventorycmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('inventory', inventorycmd)) 