import inventory

def check_if_lvl_up(uid):
    level = inventory.userinventory[uid]['level']
    xp = inventory.userinventory[uid]['XP']

    xpfornextlevel = level + 1 * 1000

    if xp >= xpfornextlevel:
        return 'yes'
    else:
        return 'no'
    