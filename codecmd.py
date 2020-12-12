import codelist
from telegram.ext import Dispatcher,CommandHandler
import inventory


def code(update, context):
    amount = codelist.codes[context.args[0]]['amount']
    rtype = codelist.codes[context.args[0]]['rtype']
    if context.args[0] in codelist.codes:
        update.message.reply_text('Code redeemed! You got %s %s!'%(amount,rtype))
        inventory.userinventory[rtype] += amount 

def add_codecmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('code', code)) 