import inventory,pokemons 
from telegram.ext import Dispatcher,CommandHandler

def pokedex(update, context):
    if len(context.args) == 0:
        allpokemons = ''
        for i in pokemons.pokemons:
            allpokemons += '%s,'%(i.name) 
        update.message.reply_text('Use the /pokedex command followed by the name of a pokemon to search it up on your pokedex! A list of all of the pokemon in the game:\n%s'%(allpokemons))
    else:
        Types = ''
        evolutionline = 'evolutionline'
        pokemonchosen = context.args[0].capitalize()
        for i in pokemons.pokemons:
            if pokemonchosen == i.name:
                pokemonobject = i
                if pokemonchosen in pokemons.pokemons:
                    for i in pokemonchosen.type:
                        Types = Types + f'{i},'
                        print(Types)
                    
                    for i in pokemonchosen.evolutionline:
                        evolutionline += '%s➡'%(i)
                    evolutionline = evolutionline[:-1]
                msg = '''%s\nThe %s\n\nDescription:\n%s\n\nStats:\nType(s): %s\nWeight: %s\nHeight: %s\n\nEvolution line:\n%s
                '''%(pokemonchosen.capitalize(),pokemonobject.nickname,pokemonobject.description,Types,pokemonobject.weight,pokemonobject.height,evolutionline)
                update.message.reply_animation(pokemonobject.giflink,caption=msg)
                break
        else:
            update.message.reply_text('Sorry, that is not a real pokemon.')

def add_pokedexcmdhandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pokedex', pokedex)) 