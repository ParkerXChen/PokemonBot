import inventory,pokemons 
from telegram.ext import Dispatcher,CommandHandler

def pokedex(update, context):
    pokemonchosen = context.args[0].lower()
    if len(context.args) == 0:
        allpokemons = ''
        for i in pokemons.pokemons:
            allpokemons += '%s,'%(i) 
        update.message.reply_text('Use the /pokedex command followed by the name of a pokemon to search it up on your pokedex! A list of all of the pokemon in the game:\n%s'%(allpokemons))
    else:
        if context.args[0].lower() in pokemons.pokemons:

            Types = ''
            for i in pokemonchosen.type:
                if len(pokemonchosen.type) == 1:
                    Types += '%s'%(i)
                else:
                    Types += '%s,'%(i)
            evolutionline = ''
            for i in pokemonchosen.evolutionline:
                    evolutionline += '%s➡'%(i)
            evolutionline = evolutionline[:-1]
            msg = '''%s\nThe %s\n\nDescription:\n%s\n\nStats:\nType(s):%s\nWeight: %s\nHeight: %s\n\nEvolution line:\n%s
            '''%(pokemonchosen.capitalize(),pokemonchosen.nickname,pokemonchosen.description,Types,pokemonchosen.weight,pokemonchosen.height,evolutionline)
            update.message.reply_animation(pokemonchosen.giflink,caption=msg)
        else:
            update.message.reply_text('Sorry, that is not a real pokemon.')

def add_pokedexcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pokedex', pokedex)) 