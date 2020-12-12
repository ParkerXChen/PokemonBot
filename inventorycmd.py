import inventory
from telegram.ext import Dispatcher,CommandHandler

def inventorycmd(update, context):
    update.message.reply_text(
        'Balls: You have %s Pokeballs, %s Greatballs, %s Ultraballs, and %s Masterballs. \n\nPokemons: Your pokemon are: %s.\nPokedollars: You have %s Pokedollars'
        %(inventory.userinventory['balls']['pokeballs'],inventory.userinventory['balls']['greatballs'],inventory.userinventory['balls']['ultraballs'],inventory.userinventory['balls']['masterballs'], inventory.userinventory['pokemons'], inventory.userinventory['pokedollars'])
    )

def add_inventorycmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('inventory', inventorycmd)) 