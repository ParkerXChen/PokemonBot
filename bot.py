from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import searchcmd
import inventorycmd
import startcmd

def read_file_as_str(file_path):

    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

searchcmd.add_searchhandler(dispatcher)
inventorycmd.add_inventorycmdhandler(dispatcher)
startcmd.add_startcmdhandler(dispatcher)

updater.start_polling() 