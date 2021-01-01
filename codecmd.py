import codelist
from telegram.ext import Dispatcher,CommandHandler
import inventory


def code(update, context):
    uid = str(update.message.from_user.id)
    if not len(context.args) == 0:
        if not '%s'%(context.args[0]) in inventory.userinventory[uid]['codesredeemed']:
            if context.args[0] in codelist.codes:
                amount = codelist.codes[context.args[0]]['amount']
                rtype = codelist.codes[context.args[0]]['rtype']
                inventory.add_coderedeemed(uid,context.args[0])
                if rtype == 'pokedollars':
                    inventory.add_pokedollars(uid,amount)
                    update.message.reply_text('Code redeemed! You got %s %s!'%(amount,rtype))
            else: 
                update.message.reply_text('Sorry, that code either does\'t exist or is expired.')
        else: 
            update.message.reply_text('Sorry, you already redeemed that code!')
    else:
            update.message.reply_text('Enter the /code command followed by a code you got from the official bot channel (https://t.me/PokemonEpicGameBotCh) to get free rewards!\n\nThe codes you have redeemed are: %s'%(inventory.userinventory['codesredeemed']))

def add_codecmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('code', code)) 