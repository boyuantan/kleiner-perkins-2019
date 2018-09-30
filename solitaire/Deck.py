import random
from .Card import *


class Deck:
    def __init__(self):
        self.cards = []
        self.index = 0
        for suit in Suit:
            for rank in range(2, 11):
                self.cards.append(Card(suit, rank))
            for rank in Rank:
                self.cards.append(Card(suit, rank))

    def get_next(self):
        if self.index >= len(self.cards):
            return False

        card = self.cards[self.index]
        self.index += 1
        return card

    def shuffle(self):
        random.shuffle(self.cards)