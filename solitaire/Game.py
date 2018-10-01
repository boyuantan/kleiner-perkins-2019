from clint.textui import puts, colored, indent, columns, prompt

from .Stack import Foundation, Stock, Column
from .Deck import Deck
from .Card import Suit, Rank, Color

_NUM_COLUMNS = 7


class Game:

    def __init__(self):
        self.setup()
        self.print()

        # Start game
        self.game_loop()

    def _error(self, error):
        puts(colored.magenta(error, False, True))

    def _is_int(self, string):
        try:
            int(string)
        except:
            return False
        return True

    def _validate_index(self, index):
        if index < 0 or index >= len(self.columns):
            return False
        return True

    def game_loop(self):
        while True:
            command = prompt.query('>')
            if command == 'restart':
                self.setup()
                self.print()
            elif command == 'print':
                self.print()
            elif command == 'help':
                puts('Pile Ids:')
                for pile_id, pile in self.ids_to_piles.items():
                    puts(colored.blue("%s: " % pile_id) + pile.name)
                puts('All commands:')
                with indent(3, '>'):
                    puts(colored.cyan('restart') + ': restarts the game.')
                    puts(colored.cyan('print') + ': print the current state of the board.')
                    puts(colored.cyan('draw')) + ': draw a card from stock.'
                    puts(colored.cyan('mv x y') + ': moves the top card from pile x to pile y, where x and y are pile ids.')
                    puts(colored.cyan('discard') + ': puts the top card of the stock pile into discards.')
                    puts(colored.cyan('quit') + ': quits the game.')
            elif command == 'draw':
                self.stock.draw()
                self.print()
            elif command.startswith('mv'):
                params = command.split(' ')
                if len(params) != 3:
                    self._error('Invalid: mv must have 2 params.')
                elif not self.ids_to_piles.get(params[1], False) or not self.ids_to_piles.get(params[2], False):
                    self._error('Invalid: params must be valid ids. Type ' + colored.cyan('help') + ' to see the list of valid ids.')
                else:
                    move_from = self.ids_to_piles[params[1]]
                    move_to = self.ids_to_piles[params[2]]
                    if not move_from.move_top_to(move_to):
                        self._error('Invalid play.')
                    else:
                        self.print()
                        win = True
                        for _, foundation in self.foundations.items():
                            if not foundation.full:
                                win = False
                                break

                        if win:
                            puts(colored.green('Congratulations, you have won the game!'))
                            again = prompt.query('Type "y" to play again!')
                            if again == 'y':
                                self.setup()
                            else:
                                break
            elif command == 'quit':
                break
            else:
                self._error('Invalid command.')
                puts('Type ' + colored.cyan('help') + ' to see all available commands.')

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()

        # Setup foundations
        self.foundations = dict()
        self.foundations[Suit.HEART] = Foundation(Suit.HEART)
        self.foundations[Suit.DIAMOND] = Foundation(Suit.DIAMOND)
        self.foundations[Suit.CLUB] = Foundation(Suit.CLUB)
        self.foundations[Suit.SPADE] = Foundation(Suit.SPADE)

        # Setup column piles
        self.columns = []
        for i in range(_NUM_COLUMNS):
            self.columns.append(Column(i + 1))

        # Deal cards
        for start_index in range(_NUM_COLUMNS):
            next_card = self.deck.get_next()
            next_card.flip()
            self.columns[start_index].deal(next_card)
            for index in range(start_index + 1, _NUM_COLUMNS):
                next_card = self.deck.get_next()
                self.columns[index].deal(next_card)

        # Setup stock pile
        self.stock = Stock()
        card = self.deck.get_next()
        while card:
            card.flip()
            self.stock.place(card)
            card = self.deck.get_next()

        # Setup ids
        self.ids_to_piles = {
            'st': self.stock,
            '1': self.columns[0],
            '2': self.columns[1],
            '3': self.columns[2],
            '4': self.columns[3],
            '5': self.columns[4],
            '6': self.columns[5],
            '7': self.columns[6],
            'h': self.foundations[Suit.HEART],
            'd': self.foundations[Suit.DIAMOND],
            'c': self.foundations[Suit.CLUB],
            's': self.foundations[Suit.SPADE]
        }

    def print(self):
        puts(colored.blue("Stock: ", False, True) + self.stock.print())
        for index, column in enumerate(self.columns):
            puts(colored.blue("Column %d: " % (index + 1)) + column.print())
        for key, foundation in self.foundations.items():
            puts(colored.blue("%s: " % key.name) + foundation.print())