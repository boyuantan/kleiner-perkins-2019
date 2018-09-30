from clint.textui import colored
from enum import Enum, IntEnum, auto


class Suit(Enum):
    HEART = 1
    DIAMOND = 2
    CLUB = 3
    SPADE = 4

SUIT_IMAGES = {
    Suit.HEART: '♥',
    Suit.DIAMOND: '♦',
    Suit.CLUB: '♣',
    Suit.SPADE: '♠'
}

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
        self.rank = rank
        self._face_up = face_up

        if suit is Suit.HEART or suit is Suit.DIAMOND:
            self._color = Color.RED
        else:
            self._color = Color.BLACK

    def suit_text(self):
        return self._suit.name

    def color(self):
        return self._color

    def rank_text(self):
        if isinstance(self.rank, Rank):
            return self.rank.name

        return str(self.rank)

    def as_text(self):
        if self._face_up:
            if self._color == Color.RED:
                return colored.red(self.rank_text() + SUIT_IMAGES[self._suit])
            else:
                return colored.black(self.rank_text() + SUIT_IMAGES[self._suit])
        else:
            return '?'

    def flip(self, face_up=True):
        self._face_up = face_up
