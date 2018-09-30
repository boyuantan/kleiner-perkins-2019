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
        puts("MY SUIT: %s, their suit_text: %s" % (str(self.suit.name), card.suit_text()))
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
            return True

        return card.color() != self.top().color() and card.rank == self.top().rank - 1

    def move_top_to(self, column):
        if self.first_visible_index == -1:
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
    name = 'Stock'

    def can_place(self, card):
        return False

    def can_remove(self):
        if self.cards:
            return True
        return False

    def move_top_to(self, column):
        # Probably should refactor such that each pile as a 'receive' function
        top_card = self.top()
        # puts('wtf')
        if not top_card:
            # puts('wtf1')
            return False

        if column.can_place(top_card):
            # puts('no way')
            column.place(top_card)
            self.pop()
            return True
        # puts('gaws')

        return False


class Waste(Stack):
    name = 'Discard'

    def can_place(self, card):
        return True

    def can_remove(self):
        return True

    def move_top_to(self, column):
        top_card = self.top()
        if not top_card:
            return False

        if column.can_place(top_card):
            column.place(top_card)
            self.pop()
            return True

        return False
