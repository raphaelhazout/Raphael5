from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.DecksOfCards import DecksOfCards
from random import randint

class CardsGame:

    def __init__(self,numcards):
    # המתודה מגדירה ארבע שחקנים וחבילת קלפים אחת
        self.numcards=numcards
        self.deck = DecksOfCards()
        self.players=[]
        a=randint(5000,10000)
        for i in range(4):
            self.players.append(Player(input('Whats the name of the player?'),a))
        self.newGame()

    def newGame(self):
    # המתודה מקבלת חפיסה חדשה, מערבבת אותה ומחלקת קלפים לכל השחקנים
        self.deck.newGame()
        for player in self.players:
            player.setHand(self.deck,self.numcards)

    def __repr__(self):
        return f'{self.players}'