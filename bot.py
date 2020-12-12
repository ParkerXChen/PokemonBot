from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import searchcmd, inventorycmd, startcmd, codecmd

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

searchcmd.add_searchhandler(dispatcher)
inventorycmd.add_inventorycmdhandler(dispatcher)
startcmd.add_startcmdhandler(dispatcher)
codecmd.add_codecmdhandler(dispatcher)

updater.start_polling() 