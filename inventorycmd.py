from telegram.ext import Dispatcher,CommandHandler
import inventory

def inventorycmd(update, context):
    uid = str(update.effective_user.id)
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    pokemonslist = ''
    pokemonslist += 'Your pokemon are:'

    if not inventory.userinventory[uid]['pokemons'] == []:
        for i in inventory.userinventory[uid]['pokemons']:
            pokemonslist += '%s,'%(i)
    else:
        pokemonslist = 'You have no pokemons'

    update.message.reply_text(
        'XP: You have %s XP.\nYou have %s pokecoins.\n\n\n\n Balls:\n\n x%s Pokeballs\n x%sGreatballs\n x%s Ultraballs\n x%s Masterballs.'%(
        inventory.userinventory[uid]['XP'],
        inventory.userinventory[uid]['pokecoins'],
        inventory.userinventory[uid]['balls']['pokeballs'],
        inventory.userinventory[uid]['balls']['greatballs'],
        inventory.userinventory[uid]['balls']['ultraballs'],
        inventory.userinventory[uid]['balls']['masterballs']
    ))

def add_inventorycmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('inventory', inventorycmd)) 