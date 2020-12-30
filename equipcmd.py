import inventory
from telegram.ext import Dispatcher,CommandHandler

def buddy(update, context):
    if len(context.args) == 0:
        update.message.reply_text('Use the /buddy command followed by the name of a to set that pokemon as your buddy.\n\nYour current buddy is: %s'%(inventory.userinventory['buddy']))
    else:
        if context.args[0] in inventory.userinventory['pokemons']:
            msg = ('%s has been set as your buddy!'%(context.args[0]))
            inventory.set_buddy(context.args[0])
        else: 
            msg = ('Sorry, either you don\'t own that pokemon or that pokemon does not exist.')    
        update.message.reply_text(msg)


def add_equipcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('buddy', buddy)) 