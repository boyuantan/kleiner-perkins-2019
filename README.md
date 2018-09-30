# Kleiner Perkins Fellows Application

This repository contains my Summer 2019 application for the Kleiner Perkins fellowship.

## Solitaire

CLI app for Solitaire, written using Python. 

### Start-up

Within the base directory:
```bash
pip install -e .
solitaire
```

### Gameplay

The image below is an example of the gameplay board.

![](./board.PNG)

To see all available commands and pile identifiers, simply type `help`.

### The Piles
- **Stock**: This pile contains the additional cards that have yet to been dealt.
In order to view the next card of this pile, `mv st w`, where `st` is the id for the stock pile
and `w` is the id for the waste pile.
- **Waste**: This pile contains the discarded cards.
- **Columns**: There are seven columns, identified by their ids (from 1 to 7).  To move all visible cards
from one column to another, use `mv x y`, where `x` is the id of the origin pile
and `y` is the id of the target pile.
- **Foundations**: There are four "foundation" piles, one for each suit.
One wins the game by filling all four foundation piles.

### Bugs
To my regret I was not able to start this application early enough, and realized too late that I did not understand the
rules of Solitaire as well as I had imagined.  Thus, this implementation of the gameplay is yet incomplete with the 
following issues that I should seek to resolve upon continuing this implementation:
- The user only has the availability to either move all visible cards off a column, OR move a single card.
The user should ideally be able to move any number of cards from a column to another. 
Although with the current implementation it would be easy to allow the user to specify an index at which all cards
should be moved, it is not ideal from the user experience perspective.
- No test suites were set up for this game.  

### Discussion and Justification
I chose to implement the game in Python as it is a language that I have had limited experience with and am only now 
using at work.  Since implementing Solitaire is a good way to learn a language, I chose to do this in Python to support
this learning.  Furthermore, as Python is less restricted with its levels of class privacy, it forces one to think 
harder about class structure and best practices with regards to naming conventions, etc.--which is always a good 
challenge to have.