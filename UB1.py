from numpy import random

Players = ['Luke', 'David', 'Hugo', 'Sam', 'Aaron', 'Rhys']

Origin = {
        'Dawnbringer':['riven','garen', 'karma', 'khazix','nidalee','soraka','gragas'],
        'Sentinel':['Akshan','Galio', 'Irelia', 'Lucian','Olaf','Pyke','Rakan','Senna'],
        'Revenant':['Fiddlesticks','Volibear', 'Ivern', 'Nocturne'],
        'Nightbringer':['Yasuo','Sejuani', 'Vladamir', 'LeeSin','Diana','Aphelious',],
        'Ironclad':['Jax','Nautilus', 'Rell'],
        'Draconic':['Ashe','Sett', 'Galio', 'Udyr','Heimerdinger'],
        'Redeemed':['Aatrox', 'Kayle', 'Leona', 'Lex', 'Rell', 'Syndra', 'Varus', 'Velkoz'],
        'Abomination':['Brand', 'Nunu', 'Kalista', 'Fiddlesticks'],
        'Forgotten':['Draven', 'Hecarim', 'Miss Fortune', 'Thresh', 'Vayne', 'Viego'],
        'Hellion':['Kennen', 'Kled', 'Lulu', 'Poppy', 'Teemo', 'Tristana', 'Ziggs']
        }

OriginKeys = list(Origin)

Class = {
        'Assassin':['Diana','Khazix', 'Nocturne', 'Pyke', 'Viego'],
        'Brawler':['Gragas', 'Nunu', 'Sejuani', 'Sett', 'Volibear'],
        'Cannoneer':['Lucian', 'Miss Fortune', 'Senna', 'Tristana'],
        'Cavalier':['Hecarim', 'Kled', 'Rell', 'Sejuani'],
        'Invoker':['Ivern', 'Karma', 'Syndra', 'Teemo'],
        'Spellweaver':['brand', 'velkoz', 'ziggs', 'zyra'],
        'Skirmisher':['Irelia', 'Jax', 'Kennen', 'Lee Sin', 'Nidalee', 'Olaf', 'Udyr', 'Viego'],
        'Renewer':['Heimerdinger', 'Ivern', 'Rakan', 'Soraka', 'Vladimir'],
        'Ranger':['Akshan', 'Aphelios', 'Ashe', 'Varus', 'Vayne'],
        'Mystic':['Fiddlesticks','Gwen', 'Lulu', 'Lux'],
        'Legionnaire':['Aatrox', 'Draven', 'Hecarim', 'Irelia', 'Kalista', 'Kayle'],
        'Knight':['Galio', 'Garen', 'Leona', 'Nautilus', 'Poppy', 'Thresh']
        }

ClassKeys = list(Class)

for i in range(len(Players)):
    player = Players[i]
    rand_origin = random.randint(len(Origin))
    rand_class = random.randint(len(Class))

    origin = OriginKeys[rand_origin]
    clasS = ClassKeys[rand_class]
    originClass = Origin[origin] + Class[clasS]

    carry = originClass[random.randint(len(originClass))]

    print('Player: ', player)
    print('Origin: ', origin)
    print('Class: ', clasS)
    print('Carry: ', carry)
    print( )