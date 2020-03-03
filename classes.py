import random
import itertools


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.suit} of {self.rank}'


class Deck:
    def __init__(self):
        self.cards = []
        ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
        suits = ('\u2660', '\u2663', '\u2665', '\u2666')
        for suit, rank in itertools.product(suits, ranks):
            self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        try:
            return str(self.cards.pop())
        except IndexError:
            self.__init__()
            return "error"

    def index(self, value):
        try:
            return str(self.cards[int(value) - 1])
        except ValueError:
            return "error"
        except IndexError:
            return "error"

    def get_random(self):
        try:
            return str(random.choice(self.cards))
        except IndexError:
            self.__init__()
            return "error"

