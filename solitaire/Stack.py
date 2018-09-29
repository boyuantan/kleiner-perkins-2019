from .Card import *

class Stack:
    def __init__(self):
        self.cards = []

    def top(self):
        if self.cards:
            return self.cards[-1]
        return False

    def deal(self, card):
        self.cards.append(card)

    def add(self, card):
        if self._can_place(card):
            self.cards.append(card)
            return True
        return False

    def pop(self):
        if self._can_remove():
            self.cards.pop(-1)
            return True
        return False

    def _can_place(self, card):
        return True

    def _can_remove(self):
        return True

    def print(self):
        list = ''
        for index, card in enumerate(self.cards):
            list += card.as_text()

        return list

class Foundation(Stack):
    def _can_place(self, card):
        top_card = self.top()
        if not top_card and card.rank() == 1:
            return True

        if top_card.suit() == card.suit() and top_card.rank() == card.rank() - 1:
            return True

        return False

    def _can_remove(self):
        return False

class Column(Stack):
    def __init__(self):
        self._visible_index = 0
        super(Column, self).__init__()

    def _can_place(self, card):
        pass

class Stock(Stack):
    def _can_place(self, card):
        return False

    def _can_remove(self):
        if self.cards:
            return True
        return False

class Waste(Stack):
    def _can_place(self, card):
        return True

    def _can_remove(self):
        return True