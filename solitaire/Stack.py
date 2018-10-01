import random

from .Card import *
from clint.textui import puts


class Stack:
    name = ''

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
        top_card = self.top()
        if not top_card:
            return False

        if column.can_place(top_card):
            column.place(top_card)
            self.pop()
            return True

        return False


class Foundation(Stack):
    _MAX_CARDS = 13

    def __init__(self, suit):
        self.suit = suit
        self.full = False
        self.name = suit.name + 'S'
        super(Foundation, self).__init__()

    def add(self, card):
        super(Foundation, self).add(card)
        if len(self.cards) == self._MAX_CARDS:
            self.full = True

    def can_place(self, card):
        if self.full:
            return False

        top_card = self.top()
        if self.suit.name != card.suit_text():
            return False

        if (not top_card and card.rank == 1) or top_card.rank == card.rank - 1:
            return True

        return False

    def can_remove(self):
        return False


class Column(Stack):
    def __init__(self, index):
        self.first_visible_index = -1
        self.name = 'Column %s' % index
        super(Column, self).__init__()

    def deal(self, card):
        self.place(card)
        self.first_visible_index += 1

    def can_place(self, card):
        top_card = self.top()
        if not top_card:
            return card.rank == Rank.K

        return card.color() != self.top().color() and card.rank == self.top().rank - 1

    def move_top_to(self, column):
        if self.first_visible_index == -1:
            return False

        if isinstance(column, Foundation):
            # If moving to a foundation pile, ONLY take the top card.
            top_card = self.top()

            if column.can_place(top_card):
                column.place(top_card)
                self.pop()

                # Update first visible and visibility of top card if it's the only visible on stack.
                if self.first_visible_index == len(self.cards):
                    self.first_visible_index -= 1
                    new_top = self.top()
                    if new_top:
                        self.top().flip()

                return True

            return False

        first_visible = self.cards[self.first_visible_index]
        puts(first_visible.as_text())

        if column.can_place(first_visible):

            initial_num_cards = len(self.cards)
            index_diff = initial_num_cards - self.first_visible_index
            for i in range(self.first_visible_index, initial_num_cards):
                column.place(self.cards[i])
            for i in range(index_diff):
                self.pop()

            top_card = self.top()
            if top_card:
                top_card.flip()
                self.first_visible_index -= 1

            return True

        return False

    def print(self):
        card_list = ''
        for index, card in enumerate(self.cards):
            card_list += card.as_text()

        return card_list


class Stock(Stack):
    waste = []
    name = 'Stock'

    def draw(self):
        if len(self.cards) > 3:
            top_card = self.top()
            self.pop()
            self.waste.append(top_card)
            return True
        else:
            self.cards.extend(self.waste)
            random.shuffle(self.cards)
            self.waste = []
            return False


    def can_place(self, card):
        return False

    def can_remove(self):
        if self.cards:
            return True
        return False

    def move_top_to(self, column):
        top_card = self.top()
        if not top_card:
            return False

        if column.can_place(top_card):
            column.place(top_card)
            self.pop()
            return True

        return False

    def print(self):
        num_cards = len(self.cards)
        text = ''
        if num_cards >= 3:
            # Always show first three cards
            for i in range(num_cards - 3, num_cards):
                text += self.cards[i].as_text()
        else:
            for i in num_cards:
                text += self.cards[i].as_text()

        return text