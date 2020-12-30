from telegram.ext import Dispatcher,CommandHandler
import inventory

def pokemonscmd(update, context):
    pokemonslist = ''
    for i in inventory.userinventory['pokemons']:
        pokemonslist += f"{i.capitalize()},"
    update.message.reply_text(f'Your pokemon are: {pokemonslist}')

def add_pokemonscmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pokemons', pokemonscmd))