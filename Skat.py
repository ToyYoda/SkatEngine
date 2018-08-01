
from random import randint

class Card:

    #init-Funktion. Legt eine Karte in der übergebenen Farbe mit dem übergebenen Wert an
    def __init__(self,farbe,wert):
        self.__farbe = farbe
        self.__wert = wert

    #Gibt die Farbe der Karte zurück
    def farbe(self):
        return self.__farbe

    #Gibt den Wert der Karte zurück
    def wert(self):
        return self.__wert

    #Gibt den Reizwert der Karte zurück
    def reizwert(self):
        if self.__farbe == "Karo":
            return 9
        if self.__farbe == "Herz":
            return 10
        if self.__farbe == "Pik":
            return 11
        if self.__farbe == "Kreuz":
            return 12

    @staticmethod
    def __getzw(wert):
        return {
            "7":0,
            "8":0,
            "9":0,
            "10":10,
            "Bube":2,
            "Dame":3,
            "König":4,
            "As":11
        }.get(wert)

    def zaehlwert(self):
        return Card.__getzw(self.__wert)

class CardSet():


    def __init__(self, full_deck = False):
        self.__cards=[]
        farben = ["Kreuz","Pik","Herz","Karo"]
        werte = ["7","8","9","10","Bube","Dame","König","As"]
        if full_deck:
            self.__cards = [Card(c,v) for c in farben for v in werte]

    def shuffle(self):
        self.__cards.sort(key=lambda zufall: randint(0,1000))

    def show(self):
        return self.__cards

    def add(self,card):
        self.__cards.append(card)

    def give(self):
        return self.__cards.pop()

    def deal(self):
        if len(self.__cards)<32:
            raise ValueError("Es kann nur ein vollständiges Deck ausgeteilt werden")
        stacks = []
        for i in range(0,3):
            stacks.append(CardSet(False))
            for j in range(0,10):
                stacks[i].add(self.__cards.pop())
        stacks.append(CardSet())
        stacks[3].add(self.give())
        stacks[3].add(self.give())

        return stacks


my_cards = CardSet(True)
my_cards.shuffle()
decks = my_cards.deal()
#this is a commit test
print(decks[0].show()[0].zaehlwert())







