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

alakazam = pokemon('Alakazam','https://professorlotus.com/Sprites/Alakazam.gif', 
                    ['Physcic'], ['Abra', 'Kadabra','Alakazam'], 0, 30,'s',75,125,75,150)

alomomola = pokemon('Alomomola','https://cdn.bulbagarden.net/upload/a/aa/Spr_5b_594.png', 
                    ['Water'], ['Alomomola'], 0, 40,'r',50,75,50,75)   

altaria = pokemon('Altaria','https://professorlotus.com/Sprites/Altaria.gif', 
                    ['Dragon','Flying'], ['Swablu','Altaria'], 0, 40,'r',75,100,50,100)   

amaura = pokemon('Amaura','https://www.pkparaiso.com/imagenes/xy/sprites/animados/amaura.gif', 
                    ['Dragon','Flying'], ['Swablu','Altaria'], 0, 40,'r',75,100,75,125)     

ambipom = pokemon('Ambipom','https://professorlotus.com/Sprites/Ambipom.gif', 
                    ['Normal'], ['Aipom','Ambipom'], 1, 30,'r',50,75,75,125)   

amoongus = pokemon('Amoonguss','https://cdn.bulbagarden.net/upload/d/d2/Spr_5b_591.png', 
                    ['Grass','Poison'], ['Foongus','Amoongus'], 1, 45,'u',50,125,50,125)  

ampharos = pokemon('Ampharios','hhttps://professorlotus.com/Sprites/Ampharos.gif', 
                    ['Electric'], ['Mareep','Flaafy','Ampharos'], 1, 30,'r',75,150,75,150)   

anorith = pokemon('Ampharios','hhttps://professorlotus.com/Sprites/Ampharos.gif', 
                    ['Electric'], ['Mareep','Flaafy','Ampharos'], 1, 30,'r',75,150,75,150)   
 
bulbasaur = pokemon('Bulbasaur','https://professorlotus.com/Sprites/Bulbasaur.gif8', 
                    ['Grass','Poison'], ['Bulbasaur','Ivysaur','Venosaur'], 0, 45,'u',50,75,35,65)   

charmander = pokemon('Charmander','https://professorlotus.com/Sprites/Charmander.gif', 
                    ['Fire'], ['Charmander','Charmander','Charizard'], 0, 45,'u',50,75,35,65)  

squirtle = pokemon('Squirtle','https://professorlotus.com/Sprites/Squirtle.gif', 
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
  aeigslash,
  amoongus
]

superrarepokemons = [
  abomasnow,
  aerodactyl,
  aggron,
  alakazam,
  alomomola,
  altaria,
  absol,
  ampharos
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