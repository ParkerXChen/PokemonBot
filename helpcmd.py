import inventory
from telegram.ext import Dispatcher,CommandHandler

def help(update, context):
    update.message.reply_text('Welcome to Epic Pokemon Game Bot! Here are all of the commands you can use:\n\n/search - Search for a pokemon to try and capture it!\n/inventory - See your inventory!\n/code (code) - Use a code from the Epic Pokemon Game Bot Channel (https://t.me/PokemonEpicGameBotCh) to get free rewards!\n/buddy (pokemon name) - Set a pokemon as your buddy!\n/travel - travel to a different location!\n/pokemons - See all of the pokemons you have!\n/despawn - Despawn all of your current wild pokemons to catch new ones! \n/help - See all of these commands again!\n\nHave fun!')


def add_helpcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('help', help)) 