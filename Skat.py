
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

    def __str__(self):
        if self.__farbe == "Karo":
            farbe = "\u2666"
        elif self.__farbe == "Herz":
            farbe = "\u2665"
        elif self.__farbe == "Pik":
            farbe = "\u2660"
        elif self.__farbe == "Kreuz":
            farbe = "\u2663"
        return farbe + str(self.__wert)

    def __repr__(self):
        return self.__str__()


class CardSet():


    def __init__(self, cardlist = [], full_deck = False):
        self.__cards = cardlist
        farben = ["Kreuz","Pik","Herz","Karo"]
        werte = ["7","8","9","10","Bube","Dame","König","As"]
        if full_deck:
            self.__cards = [Card(c,v) for c in farben for v in werte]

    def shuffle(self):
        self.__cards.sort(key=lambda zufall: randint(0,1000))

    def show(self):
        return self.__cards

    def cards(self):
        return self.__cards

    def add(self,cards):
        self.__cards += cards.show()

    def give(self):
        return self.__cards.pop()

    def deal(self):
        if len(self.__cards)<32:
            raise ValueError("Es kann nur ein vollständiges Deck ausgeteilt werden")
        stacks = []
        for i in range(0,3):
            cardlist = []
            for j in range(0,10):
                #print(cardlist)
                #print(self.__cards)
                cardlist.append(self.__cards.pop())
            stacks.append(CardSet(cardlist, False))
                #stacks[i].add(CardSet[self.__cards.pop()])

        skat = CardSet([self.give()])
        skat.add(CardSet([self.give()]))
        stacks.append(skat)

        return stacks

    def __str__(self):
        return str(self.__cards)

    def __repr__(self):
        return self.__str__()

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = CardSet()
        self.stack = CardSet()


class Game_variant():
    def __init__(self,hand = False, schneider = False, schwarz = False, ouvert = False):
        self.hand = hand
        self.schneider = schneider
        self.schwarz = schwarz
        self.ouvert = ouvert

class Game_variant_null(Game_variant):
    def __init__(self, hand = False, schneider = False, schwarz = False, ouvert = False):
        super().__init__(hand, schneider, schwarz, ouvert)

    def playable_cards(startcard, player):
        if startcard.farbe() in [card.farbe() for card in player.hand]:
            returndeck = CardSet()
            returndeck.add([card for card in player.hand if card.farbe() == startcard.farbe()])
            return returndeck
        else:
            return player.hand
            #gib alle Karten in einem cardstack zurück, die die gleiche Farbei wie startcard haben
            #sonst gib den ganzen stack zurück. Wenn man nicht bedienen kann, kann man alles spielen

    def finish_stich(self, stich):
        farbe = stich.cards()[0].farbe
        valueorder = ["7", "8", "9", "10", "Bube", "Dame", "König", "As"]
        maxvalue = valueorder.index(stich.cards()[0].wert())
        winner = stich[0]
        for card in stich:
            if valueorder.index(card.wert()) > maxvalue:
                winner = card
        #TODO: Sticht dem Gewinner zuordnen. In den Stack




class Game():
    def __init__(self):
        self.cards = CardSet(full_deck = True)
        self.cards.shuffle()
        self.skat = CardSet()
        #print("Please enter name for Player 1:")
        #self.p1 = Player(input().rstrip())
        #print("Please enter name for Player 2:")
        #self.p2 = Player(input().rstrip())
        #print("Please enter name for Player 3:")
        #self.p3 = Player(input().rstrip())
        self.p1 = Player("a")
        self.p2 = Player("b")
        self.p3 = Player("c")
        stacks = self.cards.deal()
        self.p1.hand = CardSet(stacks[0])
        self.p2.hand = CardSet(stacks[1])
        self.p3.hand = CardSet(stacks[2])
        self.skat = CardSet(stacks[3])


    def showhands(self):
        print(self.p1.name + ": " + str(self.p1.hand.show()))
        print(self.p2.name + ": " + str(self.p2.hand.show()))
        print(self.p3.name + ": " + str(self.p3.hand.show()))
        print("Skat:" + str(self.skat.show()))

game = Game()
game.showhands()