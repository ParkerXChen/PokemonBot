from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import searchcmd
import inventorycmd

def start(update, context):
    msg = "Hello %s! Welcome To: \nPOKEMON BATTLE ARENA"%(
        update.message.from_user.first_name,
    )
    update.message.reply_text(msg)

def read_file_as_str(file_path):

    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

searchcmd.add_searchhandler(dispatcher)
inventorycmd.add_inventorycmdhandler(dispatcher)

updater.start_polling()