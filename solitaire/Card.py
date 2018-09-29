from clint.textui import colored
from enum import Enum, IntEnum, auto

class Suit(Enum):
    HEART = 1
    DIAMOND = 2
    CLUB = 3
    SPADE = 4

class Color(Enum):
    RED = auto()
    BLACK = auto()

class Rank(IntEnum):
    A = 1
    J = 11
    Q = 12
    K = 13

class Card:
    def __init__(self, suit, rank, face_up=False):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

        if suit is Suit.HEART or suit is Suit.DIAMOND:
            self._color = Color.RED
        else:
            self._color = Color.BLACK

    def suit(self):
        return self._suit.name

    def color(self):
        return self._color

    def rank(self):
        if isinstance(self._rank, Rank):
            return self._rank.name

        return self._rank

    def as_text(self):
        if self._face_up:
            if self._color == Color.RED:
                return colored.red(self.rank())
            return colored.black(self.rank())
        else:
            return '?'

    def flip(self, face_up=True):
        self._face_up = face_up