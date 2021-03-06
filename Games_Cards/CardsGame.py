from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.DecksOfCards import DecksOfCards
from random import randint

class CardsGame:

    def __init__(self,name,numcards):
    # המתודה מגדירה ארבע שחקנים וחבילת קלפים אחת
        if type (numcards)!=int:
            numcards=5
        if numcards>13:
            numcards=13
        if numcards<1:
            numcards=5
        self.numcards=numcards
        self.deck = DecksOfCards()
        self.players=[]
        scum=randint(5000,10000)
        for i in range(4):
            self.players.append(Player(name[i],scum,numcards))
        self.newGame()

    def newGame(self):
    # המתודה מקבלת חפיסה חדשה, מערבבת אותה ומחלקת קלפים לכל השחקנים
        self.deck.newGame()
        for player in self.players:
            player.setHand(self.deck)

    def __repr__(self):
        return f'{self.players}'

#cards1=CardsGame('d' 'e' 'a' 'r',5)
#print(cards1)