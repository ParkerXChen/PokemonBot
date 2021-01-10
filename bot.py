from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import searchcmd, inventorycmd, codecmd, buddycmd, travelcmd, helpcmd, resetcmd, ballshopcmd, pokemonscmd, despawncmd, crateshopcmd

def start(update, context):
    update.message.reply_text('Welcome to the Epic Pokemon Game Bot! Use the /help command to see all of my commands!')

def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handlers:
start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

searchcmd.add_searchhandler(dispatcher)

inventorycmd.add_inventorycmdhandler(dispatcher)

codecmd.add_codecmdhandler(dispatcher)

buddycmd.add_buddycmdhandler(dispatcher)

travelcmd.add_travelcmdhandler(dispatcher)

helpcmd.add_helpcmdhandler(dispatcher)

resetcmd.add_resetcmdhandler(dispatcher)

ballshopcmd.add_ballshopcmdhandler(dispatcher)

despawncmd.add_despawncmdhandler(dispatcher)

pokemonscmd.add_pokemonscmdhandler(dispatcher)

crateshopcmd.add_crateshopcmdhandler(dispatcher)

updater.start_polling() 