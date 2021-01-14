from telegram.ext import Dispatcher,CommandHandler
import inventory, pokemons

def boxcmd(update, context):
    uid = str(update.message.from_user.id)
    pokemonslist = ''
    inventory.check_uid(uid)
    for i in pokemons.pokemons:
        for j in inventory.userinventory[uid]['pokemons']:
            if j['name'] == i.name:  
                if not j['name'] in inventory.userinventory[uid]['pokemonsdict']:
                    inventory.userinventory[uid]['pokemonsdict'][j['name']] = 1
                else:
                    inventory.userinventory[uid]['pokemonsdict'][j['name']] += 1

    pokemonslist = pokemonslist[:-1]
    update.message.reply_text(f'Your box is: \n\n{inventory.userinventory[uid]}')

def add_boxcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('box', boxcmd))