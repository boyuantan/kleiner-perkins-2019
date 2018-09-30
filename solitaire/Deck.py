import random

from clint.textui import puts, colored, indent
from .Card import *

class Deck:
    def __init__(self):
        self.cards = []
        self.index = 0
        for suit in Suit:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def get_next(self):
        if self.index >= len(self.cards):
            return False

        card = self.cards[self.index]
        self.index += 1
        return card

    def shuffle(self):
        random.shuffle(self.cards)