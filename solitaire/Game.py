from clint.textui import puts, colored, indent, columns, cols

from .Stack import Foundation, Stock, Waste, Column
from .Deck import Deck
from .Card import Suit, Rank, Color

_NUM_COLUMNS = 7

class Game:
    def __init__(self):
        self.setup()
        self.print()

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()

        # Setup foundations
        foundations = dict()
        foundations[Suit.HEART] = []
        foundations[Suit.DIAMOND] = []
        foundations[Suit.CLUB] = []
        foundations[Suit.SPADE] = []

        # Setup waste pile
        self.waste = Waste()

        # Setup column piles
        self.columns = []
        for i in range(_NUM_COLUMNS):
            self.columns.append(Column())

        # Deal cards
        for start_index in range(_NUM_COLUMNS):
            next_card = self.deck.get_next()
            next_card.flip(False)
            self.columns[start_index].deal(next_card)
            for index in range(start_index + 1, _NUM_COLUMNS):
                next_card = self.deck.get_next()
                next_card.flip()
                self.columns[index].deal(next_card)

        # Setup stock pile
        self.stock = Stock()
        card = self.deck.get_next()
        while card:
            self.stock.deal(card)
            card = self.deck.get_next()

        # # Test PRINTING
        # for column in self.columns:
        #     text = column.print()
        #     puts(text)

    def print(self):
        puts(colored.blue("Stock: ", False, True) + self.stock.print())
        puts(colored.blue("Waste: ", False, True) + self.waste.print())