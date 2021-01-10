import inventory
from telegram.ext import Dispatcher,CommandHandler

def buddy(update, context):
    uid = str(update.effective_user.id)
    if len(context.args) == 0:
        update.message.reply_text('Use the /buddy command followed by the name of a to set that pokemon as your buddy.\n\nYour current buddy is: %s'%(inventory.userinventory[uid]['buddy']))
    else:
        if context.args[0] in inventory.userinventory[uid]['pokemons']:
            msg = ('%s has been set as your buddy!'%(context.args[0]))
            inventory.set_buddy(uid,context.args[0])
        else: 
            msg = ('Sorry, either you don\'t own that pokemon or that pokemon does not exist.')    
        update.message.reply_text(msg)


def add_buddycmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('buddy', buddy)) 