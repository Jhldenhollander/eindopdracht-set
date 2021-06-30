import random


class Set:  # één set_kaart (1)
    def __init__(self, kleur, aantal, symbool, vulling):
        self.kleur = kleur
        self.aantal = aantal
        self.symbool = symbool
        self.vulling = vulling

    def __str__(self):
        return str((self.kleur, self.aantal, self.symbool, self.vulling))

    # def setCOLOR(NEWCOLOR):
    #       self.kleur=NEWCOLOR

    def return_infolist(self):
        return [int(self.kleur), int(self.aantal), int(self.symbool), int(self.vulling)]

    kleuren = {0: 'groen', 1: 'paars', 2: 'rood'}
    aantallen = {0: '1', 1: '2', 2: '3'}
    symbolen = {0: '♢', 1: '∼', 2: '◦'}
    vullingen = {0: 'open', 1: 'gestreept', 2: 'solide'}


# creëert 81 gerandomiseerde kaarten
def create_deck():
    kaartenstapel = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    kaartenstapel.append(Set(i, j, k, l))
    return random.sample(kaartenstapel, len(kaartenstapel))


# neemt eerste 12 kaarten van de kaartenstapel
def table():
    tafelkaarten = []
    for i in range(12):
        tafelkaarten.append(create_deck()[i])
    return (tafelkaarten)


def kaartencombi(tafelkaarten):
    vergeleken_kaartencombi = []
    for i in range(12):
        for j in range(i + 1, 12):
            for k in range(j + 1, 12):
                vergeleken_kaartencombi.append([i, j, k])
    return vergeleken_kaartencombi


def eigenschappen_vergelijken(stapel):
    sets = []
    combinatie = kaartencombi(stapel)
    for i in range(220):
        counter = 0
        j = 0
        while j < 4:
            if stapel[combinatie[i][0]].return_infolist()[j] == stapel[combinatie[i][1]].return_infolist()[j]:
                if stapel[combinatie[i][2]].return_infolist()[j] == stapel[combinatie[i][1]].return_infolist()[j]:
                    if stapel[combinatie[i][0]].return_infolist()[j] == stapel[combinatie[i][2]].return_infolist()[j]:
                        counter += 1
            elif stapel[combinatie[i][0]].return_infolist()[j] != stapel[combinatie[i][1]].return_infolist()[j]:
                if stapel[combinatie[i][2]].return_infolist()[j] != stapel[combinatie[i][1]].return_infolist()[j]:
                    if stapel[combinatie[i][0]].return_infolist()[j] != stapel[combinatie[i][2]].return_infolist()[j]:
                        counter += 1
            j = j + 1
        if counter == 4:
            sets.append(combinatie[i])
    return sets

#dikke yeet 2,0
print(str(eigenschappen_vergelijken(table())))
# klasse schrijven die vgl van eigenschappen ondersteundt
# algoritme dat sets kan opsporen
# eentje die alle geeft
# eentje die er 1 geeft

# spel eromheen bouwen


# lossekaart=Set(0,1,2,0)
# print(lossekaart.return_infolist())

'''

class Set:

#create deck
#plek maken voor die tafelkaarten die 12
#random kaart kiezen uit deck

#visualiseer/print huidige 12
#ik zie set-> controleer en als goed, voeg 3 nieuwe toe
#check of het capset
#computer zoeken na x tijd

'''















