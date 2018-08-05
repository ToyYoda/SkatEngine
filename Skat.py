
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

    def getValue(self):
        ret = 0
        for card in self.__cards:
            ret += card.zaehlwert()
        return ret

    def is_empty(self):
        return len(self.__cards) == 0

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = CardSet()
        self.stack = CardSet()


class Game_variant():
    def __init__(self,game,hand = False, schneider = False, schwarz = False, ouvert = False):
        self.hand = hand
        self.schneider = schneider
        self.schwarz = schwarz
        self.ouvert = ouvert
        self.game = game

class Game_variant_null(Game_variant):
    def __init__(self, game, hand = False, schneider = False, schwarz = False, ouvert = False):
        super().__init__(game, hand, schneider, schwarz, ouvert)

    def playable_cards(startcard, player):
        if startcard.farbe() in [card.farbe() for card in player.hand]:
            returndeck = CardSet()
            returndeck.add(CardSet([card for card in player.hand if card.farbe() == startcard.farbe()]))
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
        #Spielernummer des Gewinners herausfinden
        winnerindex = (self.game.getStartPlayer() + stich.index(winner)) % 3
        self.game.players[winnerindex].stack.add(stich)
        #Sieger spielt auf
        self.game.setStartPlayer(winnerindex)
        if winnerindex == game.reindex:
            self.finish_game()


    def finish_game(self):
        if self.game.players[self.game.reindex].stack.isempty():
            won = True
        else:
            won = False
        #TODO: Tupel zurückliefern in dem steht, wer wie viele Punkte bekommt




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
        self.players = [Player("a"),Player("b"),Player("c")]
        self.startPlayer = 0
        stacks = self.cards.deal()
        for i in range(len(self.players)):
            self.players[i].hand = CardSet(stacks[i])
        self.skat = CardSet(stacks[len(self.players)])
        self.reindex = 0

    def getStartPlayer(self):
        return self.startPlayer

    def setStartPlayer(self, startplayerindex):
        self.startPlayer = startplayerindex




    def showhands(self):
        for player in self.players:
            #TODO: an Playerarray anpassen
            print(player.name + ": " + str(player.hand.show()))
        print("Skat:" + str(self.skat.show()))

game = Game()
game.showhands()