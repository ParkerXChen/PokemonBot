class pokemon:
  def __init__(self, name, Nickname, giflink, Type, EvolutionLine, EvolutionLevel, CatchRate, Rarity,minhp, maxhp, mindp, maxdp):
    self.name = name
    self.nickname = Nickname
    self.giflink = giflink
    self.type = Type
    self.evolutionline = EvolutionLine
    self.EvolutionLevel = EvolutionLevel
    self.catchRate = CatchRate
    self.rarity = Rarity
    self.minhp = minhp
    self.maxhp = maxhp
    self.mindp = mindp
    self.maxdp = maxdp

abomasnow = pokemon('Abomasnow','Frost Tree Pokemon', 'https://professorlotus.com/Sprites/Abomasnow.gif', 
                    ['Grass','Ice'],['Snover', 'Abomansnow'], 1, 20, 's',75,150,75,150)

abra = pokemon('Abra','Psi Pokemon', 'https://static.myshinylist.com/img/sprites/all/abra.gif', 
                    ['Physcic'], ['Abra', 'Kadabra','Alakazam'], 0, 50, 'c',25,75,25,50)

absol = pokemon('Absol','Disaster Pokemon', 'https://professorlotus.com/Sprites/Absol.gif', 
                    ['Dark'], ['Absol'], 0, 40, 'r',75,135,75,100)

accelgor = pokemon('Accelgor','Shell-Out Pokemon', 'https://64.media.tumblr.com/6154f785bc65a2992ec80679851a6e1b/tumblr_pcp4qkD8Om1uh3x51o3_500.gifv', 
                    ['Bug'], ['Shelmet', 'Accelgor'], 1, 50, 'u',50,100,50,75)

aeigslash = pokemon('Aegislash','Royal Sword Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/0/07/Aegislash_Blade_SS.gif/revision/latest/top-crop/width/220/height/220?cb=20200108225953', 
                    ['Steel', 'Ghost'], ['Honedge', 'Doublade', 'Aegislash'], 2, 40, 'r',75,100,75,100)

aerodactyl = pokemon('Aerodactyl','Fossil Pokemon', 'https://orig00.deviantart.net/88aa/f/2015/345/3/0/aerodactyl_by_pokemon3dsprites-d9jn3cx.gif', 
                    ['Rock', 'Flying'], ['Aerodactyl'], 0, 30, 's',75,150,100,150)

aggron = pokemon('Aggron','Fossil Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/e/e2/Aggron_BW.gif/revision/latest/scale-to-width-down/81?cb=20120622080242', 
                    ['Steel', 'Rock'], ['Aron','Lairon','Aggron'], 2, 20,'s',75,150,100,150)

aipom = pokemon('Aipom','Long Tail Pokemon', 'https://professorlotus.com/Sprites/Aipom.gif', 
                    ['Normal'], ['Aipom','Ambipom'], 0, 40,'u',25,75,25,75)

alakazam = pokemon('Alakazam','Psi Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/9/99/Alakazam-AttackAnimation-XY-2.gif/revision/latest/scale-to-width-down/180?cb=20160625012653', 
                    ['Physcic'], ['Abra', 'Kadabra','Alakazam'], 0, 30,'s',75,125,75,150)

alomomola = pokemon('Alomomola','Caring Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/8/8d/Alomomola_BW.gif/revision/latest/scale-to-width-down/38?cb=20120415140141', 
                    ['Water'], ['Alomomola'], 0, 40,'r',50,75,50,75)   

altaria = pokemon('Altaria','Humming Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/d/d7/Altaria_BW.gif/revision/latest/top-crop/width/220/height/220?cb=20120622080947', 
                    ['Dragon','Flying'], ['Swablu','Altaria'], 0, 40,'r',75,100,50,100)   

amaura = pokemon('Amaura','Tundra Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/4/4e/Amaura_XY.gif/revision/latest/scale-to-width-down/52?cb=20140608154517', 
                    ['Dragon','Flying'], ['Swablu','Altaria'], 0, 40,'r',75,100,75,125)     

ambipom = pokemon('Ambipom','Long Tail Pokemon', 'https://static.wikia.nocookie.net/pokemon/images/8/89/Ambipom_XY.gif/revision/latest/top-crop/width/220/height/220?cb=20150201050425', 
                    ['Normal'], ['Aipom','Ambipom'], 1, 30,'r',50,75,75,125)   

commonpokemons = [
    abra,
    aipom
]

uncommonpokemons = [
    accelgor,
    ambipom
]

rarepokemons = [
  aeigslash,
  absol
]

superrarepokemons = [
  abomasnow,
  aerodactyl,
  aggron,
  alakazam,
  alomomola,
  altaria
]

legendarypokemons = [

]

pokemons = [
  abomasnow,
  abra, 
  absol,
  accelgor,
  aeigslash,
  aerodactyl,
  aggron,
  aipom,
  alakazam,
  alomomola,
  altaria,
  amaura,
  ambipom
]