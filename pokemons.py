class pokemon:
  def __init__(self, name, giflink, Type, EvolutionLine, EvolutionLevel, CatchRate, Rarity,minhp, maxhp, mindp, maxdp):
    self.name = name
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

abomasnow = pokemon('Abomasnow','https://professorlotus.com/Sprites/Abomasnow.gif', 
                    ['Grass','Ice'],['Snover', 'Abomansnow'], 1, 20, 's',75,150,75,150)

abra = pokemon('Abra','https://professorlotus.com/Sprites/Abra.gif', 
                    ['Physcic'], ['Abra', 'Kadabra','Alakazam'], 0, 50, 'c',25,75,25,50)

absol = pokemon('Absol','https://professorlotus.com/Sprites/Absol.gif', 
                    ['Dark'], ['Absol'], 0, 40, 'r',75,135,75,100)

accelgor = pokemon('Accelgor','https://static.wikia.nocookie.net/pokemon/images/3/30/Accelgor_XY.gif/revision/latest/scale-to-width-down/92?cb=20140819074254', 
                    ['Bug'], ['Shelmet', 'Accelgor'], 1, 50, 'u',50,100,50,75)

aeigslash = pokemon('Aegislash','https://static.wikia.nocookie.net/pokemon/images/0/07/Aegislash_Blade_SS.gif/revision/latest/top-crop/width/220/height/220?cb=20200108225953', 
                    ['Steel', 'Ghost'], ['Honedge', 'Doublade', 'Aegislash'], 2, 40, 'r',75,100,75,100)

aerodactyl = pokemon('Aerodactyl','https://professorlotus.com/Sprites/Aerodactyl.gif', 
                    ['Rock', 'Flying'], ['Aerodactyl'], 0, 30, 's',75,150,100,150)

aggron = pokemon('Aggron','https://professorlotus.com/Sprites/Aggron.gif', 
                    ['Steel', 'Rock'], ['Aron','Lairon','Aggron'], 2, 20,'s',75,150,100,150)

aipom = pokemon('Aipom','https://professorlotus.com/Sprites/Aipom.gif', 
                    ['Normal'], ['Aipom','Ambipom'], 0, 40,'u',25,75,25,75)

alakazam = pokemon('Alakazam','https://static.wikia.nocookie.net/pokemon/images/9/99/Alakazam-AttackAnimation-XY-2.gif/revision/latest/scale-to-width-down/180?cb=20160625012653', 
                    ['Physcic'], ['Abra', 'Kadabra','Alakazam'], 0, 30,'s',75,125,75,150)

alomomola = pokemon('Alomomola','https://static.wikia.nocookie.net/pokemon/images/8/8d/Alomomola_BW.gif/revision/latest/scale-to-width-down/38?cb=20120415140141', 
                    ['Water'], ['Alomomola'], 0, 40,'r',50,75,50,75)   

altaria = pokemon('Altaria','https://static.wikia.nocookie.net/pokemon/images/d/d7/Altaria_BW.gif/revision/latest/top-crop/width/220/height/220?cb=20120622080947', 
                    ['Dragon','Flying'], ['Swablu','Altaria'], 0, 40,'r',75,100,50,100)   

amaura = pokemon('Amaura','https://static.wikia.nocookie.net/pokemon/images/4/4e/Amaura_XY.gif/revision/latest/scale-to-width-down/52?cb=20140608154517', 
                    ['Dragon','Flying'], ['Swablu','Altaria'], 0, 40,'r',75,100,75,125)     

ambipom = pokemon('Ambipom','https://static.wikia.nocookie.net/pokemon/images/8/89/Ambipom_XY.gif/revision/latest/scale-to-width-down/104?cb=20150201050425', 
                    ['Normal'], ['Aipom','Ambipom'], 1, 30,'r',50,75,75,125)   

amoongus = pokemon('Amoonguss','https://static.wikia.nocookie.net/pokemon/images/d/dd/Amoonguss_XY.gif/revision/latest/scale-to-width-down/78?cb=20140816055327', 
                    ['Grass','Poison'], ['Foongus','Amoongus'], 1, 45,'u',50,125,50,125)  

ampharos = pokemon('Ampharios','https://static.wikia.nocookie.net/pokemon/images/c/cb/Ampharos_XY.gif/revision/latest/scale-to-width-down/69?cb=20150201050425', 
                    ['Electric'], ['Mareep','Flaafy','Ampharos'], 1, 30,'r',75,150,75,150)   
 
bulbasaur = pokemon('Bulbasaur','https://static.wikia.nocookie.net/pokemon/images/9/9b/Bulbasaur_LGPE.gif/revision/latest/scale-to-width-down/178?cb=20191102161018', 
                    ['Grass','Poison'], ['Bulbasaur','Ivysaur','Venosaur'], 0, 45,'u',50,75,35,65)   

charmander = pokemon('Charmander','https://static.wikia.nocookie.net/pokemon/images/f/f5/Charmander_XY.gif/revision/latest/scale-to-width-down/48?cb=20150201050431', 
                    ['Fire'], ['Charmander','Charmander','Charizard'], 0, 45,'u',50,75,35,65)  

squirtle = pokemon('Squirtle','https://static.wikia.nocookie.net/pokemon/images/4/44/Squirtle_XY_Shiny_Sprite.gif/revision/latest/scale-to-width-down/53?cb=20141031154331', 
                    ['Water'], ['Squirtle','Wartortle','Blastoise'], 0, 45,'u',50,75,35,65)  



commonpokemons = [
    abra,
    aipom
]

uncommonpokemons = [
    accelgor,
    ambipom,
    bulbasaur,
    
    squirtle
]

rarepokemons = [
  aeigslash
]

superrarepokemons = [
  abomasnow,
  aerodactyl,
  aggron,
  alakazam,
  alomomola,
  altaria,
  absol
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