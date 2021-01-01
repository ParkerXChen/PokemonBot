from telegram.ext import Dispatcher,CommandHandler
import inventory

def pokemonscmd(update, context):
    uid = str(update.message.from_user.id)
    pokemonslist = ''
    for i in inventory.userinventory[uid]['pokemons']:
        pokemonslist += f"{i.capitalize()},"
    update.message.reply_text(f'Your pokemon are: \n{pokemonslist}')

def add_pokemonscmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pokemons', pokemonscmd))