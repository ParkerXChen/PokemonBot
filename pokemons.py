class pokemon:
  def __init__(self, name, Nickname, giflink, Type, Description, Pronounciation, Height, Weight, EvolutionLine, EvolutionLevel, CatchRate,Rarity, canmegaevolve):
    self.name = name
    self.nickname = Nickname
    self.giflink = giflink
    self.type = Type
    self.description = Description
    self.pronounciation = Pronounciation
    self.height = Height
    self.weight = Weight
    self.evolutionline = EvolutionLine
    self.EvolutionLevel = EvolutionLevel
    self.catchRate = CatchRate
    self.rarity = Rarity
    self.canmegaevolve = canmegaevolve

abomasnow = pokemon('Abomasnow','Frost Tree Pokemon', 'https://professorlotus.com/Sprites/Abomasnow.gif', 
                    ['Grass','Ice'], 'Abomasnows mainly live on snow-covered mountains. They create blizzards to hide themselves and keep others away',
                     'ah-BOM-ah-snow', '2.2m', '135.5kg', ['Snover', 'Abomansnow'], 1, 20, 's', True)

abra = pokemon('Abra','Psi Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/a/aa/Abra-Attackanimation-XY-1.gif/revision/latest/scale-to-width-down/340?cb=20160625005201', 
                    ['Physcic'], 'Abra sleeps for 18 hours a day. However, it can sense the presence of foes even while it is sleeping. In such a situation, this Pokémon immediately teleports to safety.',
                    'AH-bra', '0.9m', '19.5kg', ['Abra', 'Kadabra','Alakazam'], 0, 65, 'c', False)

absol = pokemon('Absol','Disaster Pokemon', 'https://25.media.tumblr.com/70d7556faa226805d27ec8f2110febd4/tumblr_mpxv74KloG1rumlrno3_500.gif', 
                    ['Dark'], 'Every time Absol appears before people, it is followed by a disaster such as an earthquake or a tidal wave. As a result, it came to be known as the disaster Pokémon.',
                     'AB-sol', '1.19m', '47kg', ['Absol'], 0, 40, 'r', False)

accelgor = pokemon('Accelgor','Shell-Out Pokemon', 'https://64.media.tumblr.com/6154f785bc65a2992ec80679851a6e1b/tumblr_pcp4qkD8Om1uh3x51o3_500.gifv', 
                    ['Bug'], 'When its body dries out, it weakens. So, to prevent dehydration, it wraps itself in many layers of thin membrane.',
                     'ak-SELL-gohr', '0.8m', '25.3kg', ['Shelmet', 'Accelgor'], 1, 50, 'u', False)

aeigslash = pokemon('Aegislash','Royal Sword Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/0/07/Aegislash_Blade_SS.gif/revision/latest/top-crop/width/220/height/220?cb=20200108225953', 
                    ['Steel', 'Ghost'], 'Generations of kings were attended by these Pokémon, which used their spectral power to manipulate and control people and Pokémon.',
                     'EE-jih-SLASH', '1.7m', '53kg', ['Honedge', 'Doublade', 'Aegislash'], 2, 40, 'r', False)

aerodactyl = pokemon('Aerodactyl','Fossil Pokemon', 'https://orig00.deviantart.net/88aa/f/2015/345/3/0/aerodactyl_by_pokemon3dsprites-d9jn3cx.gif', 
                    ['Rock', 'Flying'], 'Aerodactyl is a Pokémon from the age of dinosaurs. It was regenerated from genetic material extracted from amber. It is imagined to have been the king of the skies in ancient times',
                     'AIR-row-DACK-tyl', '1.8m', '59kg', ['Aerodactyl'], 0, 30, 's', True)

aggron = pokemon('Aggron','Fossil Pokemon', 'https://cdn.staticneo.com/w/pokemon/c/c1/306.gif', 
                    ['Steel', 'Rock'], 'Aggron claims an entire mountain as its own territory. It mercilessly beats up anything that violates its environment. This Pokémon vigilantly patrols its territory at all times.',
                     'AGG-ron', '2.11m', '360kg', ['Aron','Lairon','Aggron'], 2, 20,'s', True)
    


commonpokemons = [
    abra
]

uncommonpokemons = [
    accelgor
]

rarepokemons = [
  aeigslash,
  absol
]

superrarepokemons = [
  abomasnow,
  aerodactyl,
  aggron
]

legendarypokemons = [

]