from .Card import *

class Stack:
    def __init__(self):
        self.cards = []

    def top(self):
        if self.cards:
            return self.cards[-1]
        return False

    def place(self, card):
        self.cards.append(card)

    def add(self, card):
        if self.can_place(card):
            self.cards.append(card)
            return True
        return False

    def pop(self):
        if self.can_remove():
            self.cards.pop(-1)
            return True
        return False

    def can_place(self, card):
        return True

    def can_remove(self):
        return True

    def print(self):
        top_card = self.top()
        if top_card:
            return top_card.as_text()

        return 'None'

    def move_top_to(self, column):
        if column is self:
            return False
        if column is Waste:
            return True

        return False


class Foundation(Stack):
    _MAX_CARDS = 13

    def __init__(self, suit):
        self.suit = suit
        self.full = False
        super(Foundation, self).__init__()

    def add(self, card):
        super(Foundation, self).add(card)
        if len(self.cards) == self._MAX_CARDS:
            self.full = True

    def can_place(self, card):
        if self.full:
            return False

        top_card = self.top()
        if not self.suit == card.suit():
            return False

        if (not top_card and card.rank() == 1) or top_card.rank() == card.rank() - 1:
            return True

        return False

    def can_remove(self):
        return False


class Column(Stack):
    def __init__(self):
        self._visible_index = 0
        super(Column, self).__init__()

    def can_place(self, card):
        top_card = self.top()
        if not top_card:
            return True

        return card.color() != self.top().colour() and card.rank() == self.top().rank() - 1

    def move_top_to(self, column):
        top_card = self.top()
        if not top_card:
            return False

        if column.can_place(top_card):
            self.pop()
            column.place(top_card)
            return True

        return False

    def print(self):
        card_list = ''
        for index, card in enumerate(self.cards):
            card_list += card.as_text()

        return card_list


class Stock(Stack):
    def can_place(self, card):
        return False

    def can_remove(self):
        if self.cards:
            return True
        return False


class Waste(Stack):
    def can_place(self, card):
        return True

    def can_remove(self):
        return True