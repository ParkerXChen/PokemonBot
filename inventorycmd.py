import inventory
from telegram.ext import Dispatcher,CommandHandler

def inventorycmd(update, context):
    update.message.reply_text(
        'Pokeballs: You have %s pokeballs. \n Pokemons: Your pokemon are: %s.\n Pokecoins: You have %s Pokecouns'
        %(inventory.userinventory['pokeballs'], inventory.userinventory['pokemons'], inventory.userinventory['pokecoins'])
    )

def add_inventorycmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('inventory', inventorycmd)) 