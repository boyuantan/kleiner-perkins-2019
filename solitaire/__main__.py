import argparse
import sys
import os

from clint.arguments import Args
from clint.textui import puts, colored, indent

from .Card import *
from .Deck import *
from .Game import Game

def main():
    game = Game()