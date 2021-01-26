from telegram.ext import Dispatcher,CommandHandler
import inventory, pokemons

def boxcmd(update, context):
    uid = str(update.message.from_user.id)
    inventory.check_uid(uid,update.message.from_user.first_name,update.message.from_user.username)
    for i in pokemons.pokemons:
        for j in inventory.userinventory[uid]['pokemons']:
            if j['name'] == i.name:  
                if not j['name'] in inventory.userinventory[uid]['pokemonsdict']:
                    inventory.userinventory[uid]['pokemonsdict'][j['name']] = 1
                else:
                    inventory.userinventory[uid]['pokemonsdict'][j['name']] += 1

    for i in inventory.userinventory[uid]['pokemonsdict'].keys():
        inventory.userinventory[uid]['pokemonslist'] += f"{i} x{inventory.userinventory[uid]['pokemonsdict'][i]} \n"

    update.message.reply_text(f'{update.message.from_user.first_name}\'s box: \n\n{inventory.userinventory[uid]["pokemonslist"]}')
    inventory.userinventory[uid]['pokemonsdict'] = {}
    inventory.userinventory[uid]['pokemonslist'] = ''

def add_boxcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('box', boxcmd))