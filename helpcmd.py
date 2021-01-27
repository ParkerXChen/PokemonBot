import inventory
from telegram.ext import Dispatcher,CommandHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup

def helpcmd(update, context):
    keyboard=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/search@EpicPokemonGameBot")],[KeyboardButton(text="/leaderboard@EpicPokemonGameBot")],[KeyboardButton(text="/box@EpicPokemonGameBot")],[KeyboardButton(text="/despawn@EpicPokemonGameBot")],[KeyboardButton(text="/code@EpicPokemonGameBot")],[KeyboardButton(text="/help@EpicPokemonGameBot")]])
    update.message.reply_text('Welcome to Epic Pokemon Game Bot! Here are all of the commands you can use:\n\n/search - Search for a pokemon to try and capture it!\n/despawn - Despawn all of your current wild pokemons to catch new ones!\n/inventory - See your inventory!\n/code (code) - Use a code from the Epic Pokemon Game Bot Channel (https://t.me/PokemonEpicGameBotCh) to get free rewards!\n/buddy (pokemon name) - Set a pokemon as your buddy!\n/travel - travel to a different location!\n/box - See your box (The pokemons you have)!\n/help - See all of these commands again!\n\nHave fun!',reply_markup=keyboard)


def add_helpcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('help', helpcmd)) 